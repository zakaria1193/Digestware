---
project: gcc
subsystem: analyzer (-fanalyzer region model / store)
patch_id: null
tags:
- static-analysis
- symbolic-execution
- memory-model
- hash-consing
- gcc-analyzer
lesson_id: gcc:2026-W46
commit_hash: 7647c00b77ee1aefcd3dbd7aed9c1a7553d83f94
source_type: github
headline: 'Memory as a function from bits: how -fanalyzer''s store now models what
  your program wrote'
hook: GCC's static analyzer has dropped typed key→value bindings and now tracks simulated
  memory bit by bit. The design shows how to build a symbolic store that holds up
  under memcpy, unions and casts.
tldr: -fanalyzer's store now maps (base region, symbolic bit range) to immutable,
  hash-consed bit vectors. Types are handled at a higher layer.
concept: A symbolic memory model is easier to get right when its bottom layer is untyped.
  Each cluster's contents form a total, purely functional map from symbolic bit offsets
  to bit vectors. Types, bounds and scalar values sit on top of that layer and are
  never mixed into it.
prerequisites:
- what a static analyzer's symbolic execution does
- pointer arithmetic and why it is undefined across objects
- hash-consing / interning of immutable values
- the difference between a typed value and its byte representation
code_tour:
- path: gcc/analyzer/symbolic-bit-contents.h
  symbol: symbolic::bit_contents
  lines: 33-65
  why: 'The design document in comment form: contents as a total, purely functional
    map from bit ranges to bit vectors, plus the full subclass hierarchy.'
- path: gcc/analyzer/symbolic-memory-ranges.h
  symbol: symbolic::memory_range
  lines: 30-79
  why: The (base region, symbolic bit range) pair that every symbolic read and write
    is reduced to; note the granularity is bits.
- path: gcc/analyzer/store.cc
  symbol: store::get_bit_contents
  lines: 1253-1266
  why: 'Read path: an existing cluster returns its stored bit_contents, and an untouched
    region falls back to implicit contents.'
- path: gcc/analyzer/store.cc
  symbol: store::set_bit_contents_raw
  lines: 1386-1400
  why: 'Write path: only tracked base regions get a cluster, and the whole bit_contents
    value is replaced in one step.'
- path: gcc/analyzer/store.cc
  symbol: store::bits_live_p
  lines: 1727-1744
  why: Liveness decided by pointer identity, which is only valid because immutable
    nodes are consolidated.
takeaways:
- Keep the bottom layer of a symbolic memory model untyped, and interpret types and
  check bounds above it.
- Model memory contents as a total function so that every bit, even at a negative
  offset, has a defined answer.
- With immutable nodes and hash-consing, pointer equality can replace deep structural
  comparison.
- Give offsets and sizes unit-safe types so that bits and bytes cannot be mixed by
  accident.
- 'Untouched memory should cost nothing: derive its contents implicitly instead of
  storing them.'
further_reading:
- title: 'analyzer: rewrite of symbolic value handling (commit 7647c00b77ee)'
  url: https://github.com/gcc-mirror/gcc/commit/7647c00b77ee1aefcd3dbd7aed9c1a7553d83f94
primer_expert: In gcc/analyzer, the `store` (store.cc), which sits under `region_model`,
  now holds one immutable `symbolic::bit_contents` per `binding_cluster` in place
  of a `binding_map` of keys→svalues. Symbolic accesses lower to `symbolic::memory_range`
  (base region plus symbolic bit range), and `svalue`s enter only through `bit_vector_from_svalue`.
  Liveness (`store::bits_live_p`) and equality depend on manager-level consolidation.
  Call summaries are stubbed in this rewrite.
primer_glossary:
- term: -fanalyzer
  definition: GCC's built-in static analyzer. It symbolically executes each function
    along many paths and reports problems such as leaks, double-frees, uninitialized
    reads and out-of-bounds accesses.
- term: store
  definition: The part of the analyzer's state that records what is in simulated memory
    at a given program point on a given path.
- term: binding cluster
  definition: The analyzer's unit of memory tracking, one per base region (for example
    each local variable). Pointer arithmetic is meaningful within a cluster and undefined
    between clusters.
- term: base region
  definition: The outermost object a memory access belongs to, such as a whole variable
    or a heap allocation, as opposed to a field or element inside it.
- term: region
  definition: The analyzer's symbolic description of a piece of memory, such as a
    declaration, a frame, the stack or the heap, arranged in a parent/child hierarchy.
- term: svalue
  definition: The analyzer's symbolic value, for example a constant, the initial value
    of a variable, or a binary operation on other svalues, possibly with known value
    ranges.
- term: binding_map
  definition: The pre-rewrite per-cluster data structure (GCC 11-16) that mapped concrete
    or symbolic byte-range keys to svalues.
- term: symbolic::memory_range
  definition: A pair of a base region and a possibly symbolic range of bits within
    it. It identifies exactly which bits an access touches.
- term: symbolic::bit_vector
  definition: An immutable, possibly symbolically sized sequence of bits, such as
    the target encoding of a value, a run of zeros, or a slice of a region's initial
    contents.
- term: symbolic::bit_contents
  definition: An immutable total function from bit offset to bit value that describes
    everything in a cluster, for example "uninitialized except bytes [0,4)".
landing_slug: 2026-11-13-analyzer-7647c00b
url: https://github.com/gcc-mirror/gcc/commit/7647c00b77ee1aefcd3dbd7aed9c1a7553d83f94
week_start: '2026-11-09'
week_end: '2026-11-15'
commit_date: '2026-11-13'
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

## What the analyzer's store is for

`-fanalyzer` runs a path-sensitive symbolic execution over GCC's internal representation of your function. At every point on every explored path it keeps a `program_state`, and inside that sits a region model and a **store**. The store answers one question: "if the program reads these bytes here, what does it get?" Every other check depends on that answer, including use of uninitialized memory, leaks, out-of-bounds accesses and unterminated strings.

The commit message describes the store's layout. Simulated memory is split into *binding clusters*, one per base region. A local variable, for example, gets its own cluster. The split follows C's rules: pointer arithmetic is well-defined inside a cluster and undefined between clusters, so the analyzer never has to work out how two clusters are laid out relative to each other.

From GCC 11 through 16, each cluster's contents lived in a `binding_map`, a mapping from "binding keys" (concrete or symbolic byte ranges) to `svalue`s, the analyzer's symbolic values. The commit message lists the problems with that design: sloppy use of type nodes, sloppy numeric types, typed expressions mixed with the values of raw chunks of memory, weak support for low-level memory manipulation, and "unclear semantics for all of the above, making fixing bugs impossible". A key→svalue map works while the program writes and reads whole typed objects. It breaks down once the program writes an `int`, reads two `short`s, `memset`s half a struct, or scans a buffer for a NUL.

## The new mechanism: ranges of bits, vectors of bits, contents as a total function

The rewrite adds a layer below types. Every read or write of a symbolic region, such as accessing a struct field, is converted into a `symbolic::memory_range`:

```c++
/* A (base_region, symbolic bit range) pair.
   Note that the range has a granularity of *bits*.  */
class memory_range
{
  ...
  const region &m_base_reg;
  symbolic_bit_range m_bit_range;
};
```

The base region names the cluster. The `symbolic_bit_range` exposes `get_start_offset()`, `get_next_offset()` and `get_size()`, and each of these can be symbolic. The offsets and sizes come from a new `symbolic::scalar<T>` family that the commit message calls "unit-safe": the type system distinguishes bits from bytes, so an expression like "(64 bytes) + (32 bytes * n)" cannot be silently combined with a bit count. `memory_offset` (a specific bit within a cluster) and `memory_pointer` (a specific byte within a cluster) are built on the same scalars.

What gets stored at a range is a `symbolic::bit_vector`, not an `svalue`. The commit message's examples are "the bit-level representation of (int)42 on the target", "1024 bytes of zeros" and "bits [16...19) of the initial value of buf". Bit vectors can have symbolic length, for example "the first n bytes of str plus m copies of '_' plus a zero byte". A scalar value enters this layer through `bit_vector_from_svalue`, which represents the target encoding of an `svalue`.

A whole cluster's contents form a `symbolic::bit_contents`. The header defines it as "a total function from symbolic bit ranges to symbolic bit vectors":

```text
symbolic::bit_contents (abstract)
  symbolic::uniform_bit_contents (abstract): something that ignores the input range
    symbolic::uninit_contents (concrete singleton): uninitialized everywhere
    symbolic::untracked_bit_contents (concrete): unknown everywhere, ...
    symbolic::zero_contents (concrete singleton): zero everywhere
  symbolic::unfoldable_bit_contents (abstract): unfoldable; hands out bit_vector_from_ubc instances
    symbolic::baseline_bit_contents (concrete): the initial contents of regions without known sizes
    symbolic::conjured_bit_contents (concrete): a bit_contents arising from a stmt
  symbolic::bit_overlay (abstract): a baseline overridden at some places
    symbolic::concrete_bit_overlay (concrete)
    symbolic::symbolic_bit_overlay (concrete)
  symbolic::offset_bit_contents (concrete): offsets the coordinates of another bit_contents
```

The function is *total*: every bit has an answer, including bits at negative offsets ("e.g. for the case of negative offsets from a symbolic pointer"). The header says plainly that "Any range checking happens at a higher level." Bounds checking is therefore a separate concern layered on top, not something built into the storage. The function is also **purely functional**: "setters return a reference to a bit_contents instance holding the update." Writing `i += 1` does not mutate anything. It builds a `concrete_bit_overlay` whose baseline is the old contents and which overrides bytes `[0..4)` with a `bit_vector_from_svalue` wrapping `(i + 1)`. The commit message's `__analyzer_dump` tree shows exactly this shape.

## How the store uses it, and why hash-consing matters

In `store.cc` a cluster now holds a single `bit_contents` value. The read path is short:

```c++
const symbolic::bit_contents &
store::get_bit_contents (const region &base_reg,
			 baseline_state bs) const
{
  binding_cluster **cluster_slot
    = const_cast <cluster_map_t &> (m_cluster_map).get (&base_reg);
  if (!cluster_slot)
    {
      auto &bc = get_implicit_contents (base_reg, bs);
      return bc;
    }
  return (*cluster_slot)->get_bit_contents ();
}
```

If a region has never been written, it has no cluster, and its contents are *implicit*, derived from the baseline state. Memory nobody has touched costs nothing to represent. The write path, `store::set_bit_contents_raw`, replaces the whole contents in one step, and only for base regions that report `tracked_p()`:

```c++
if (base_reg.tracked_p ())
  {
    auto *cluster = get_or_create_cluster (&base_reg,
					   model.get_baseline_state ());
    cluster->set_bit_contents (bc);
  }
```

Because nodes are immutable, the commit message says they are "consolidated by manager classes (similar to hash-consing)": structurally equal nodes become the same object. That makes pointer comparison a valid equality test, and `store::bits_live_p` relies on it. To decide whether a `bit_vector_from_ubc`, a slice handed out by a baseline contents, is still live, the function rebuilds the `memory_range` and asks the store what is there now:

```c++
symbolic::memory_range mem_range (*base_reg,
				bv_from_ubc.get_bit_range ());
if (&get_bits (mem_range, model.get_baseline_state ()) == &bv_from_ubc)
  return true;
```

If the region is still untouched at that range, the lookup returns the *same object*, so those bits are implicitly live. Without consolidation this check would need a deep structural comparison, or would simply be wrong.

## What changes for everyone else

The commit message says the rewrite deletes several `svalue` kinds whose semantics were poorly defined: `region_svalue`, `sub_svalue`, `repeated_svalue`, `bits_within_svalue`, `compound_svalue` and `conjured_svalue`. They are replaced by `svalue_from_bit_vector` backed by either a `bit_vector` or a `bit_contents`. Values such as "a repeated byte pattern" or "a sub-range of another value" now live in the untyped bit layer, where their meaning is defined without reference to a C type.

If you use `-fanalyzer`, the commit message says to expect better behaviour on byte-level manipulation. It reports fixes for "numerous cases that didn't work before", several existing xfails resolved, and new string support through a `string_scan` operation that finds the first NUL or terminator byte, aimed at diagnosing unterminated buffers. The message also reports roughly 12% faster wallclock analysis on the integration suite. That figure compares debug builds against debug builds and is self-reported, so treat it as a positive sign, not a benchmark.

There is one regression to know about. The new implementation of call summaries is "somewhat stubbed", and the patch adds xfails for it. Call summaries are off by default, so most users won't notice. If you enable them, expect gaps.

The lesson for people who build analyzers, abstract interpreters or emulators is the layering. Store raw, typed-agnostic bit contents at the bottom and make that layer a total, immutable function. Put type interpretation and bounds checking above it. Once the bottom layer has precise semantics, `memcpy`, unions and type-punning casts become ordinary operations on bit ranges, with no special cases needed.

## Seeing it yourself

The analyzer has debugging builtins, and the commit message shows `__analyzer_dump` printing a `program_state` as an ASCII tree built with `text_art::tree_widget`. Under `Store` you will see each cluster, for example `i_2:`. Under the cluster you will see its `bit_contents`, such as a `concrete bit overlay` with `concrete ranges` like `[bytes 0..4): bit_vector_from_svalue[size: 4 bytes]` above a `baseline: uninitialized contents`. On terminals that support it, colour distinguishes svalues, regions, scalars, bit vectors and bit contents.

The commit message also describes an `__analyzer_hexdump (ptr, size)` builtin. It renders a region as binary, hex and ASCII, with `?` for unknown bits: after `j = i & 0xff00ff00`, the dump shows `00 ?? 00 ??`. The author says it exists mostly to make sure every class has a well-defined meaning, not as an analysis tool. The researcher could not confirm the builtin in the tree, so check that it exists in your build before relying on it.

To read the code, start with the class-hierarchy comment in `gcc/analyzer/symbolic-bit-contents.h`. Then read `memory_range` in `gcc/analyzer/symbolic-memory-ranges.h`, then the three short `store.cc` functions quoted above.
