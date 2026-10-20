---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- match.pd
- vectors
- VEC_PERM_EXPR
- miscompile
- GIMPLE
lesson_id: gcc:2026-W42
commit_hash: ca6ddc9ecd74b89284ecede2ed90f768f70d88a5
source_type: github
headline: 'A permute''s selector indexes its inputs, not its result: the element-count
  mix-up behind a GCC vector fold'
hook: A vector shuffle can return a different number of lanes than it reads. A GCC
  fold took one count for the other, and the result was silent wrong values or GIMPLE
  that fails verification.
tldr: GCC's BIT_FIELD_REF-of-VEC_PERM_EXPR fold took the lane count from the result
  instead of the inputs, which broke permutes whose inputs and result differ in wid…
concept: A permute selector holds indices into the concatenation of its two inputs,
  so its boundaries (the modulo, the a-or-b test, the rebase into b) come from the
  input length. The selector's own length gives the number of output lanes, which
  is a separate quantity.
prerequisites:
- SIMD vectors and lane shuffles
- what an SSA-form intermediate representation is
- the idea of peephole / pattern-based algebraic simplification
- GCC vector_size attribute types
code_tour:
- path: gcc/match.pd
  symbol: simplify BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3)
  lines: 11035-11044
  why: The pattern header and the setup of elem_size, size, nelts, idx and nelts_op.
- path: gcc/match.pd
  symbol: simplify BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3)
  lines: 11045-11052
  why: 'The fixed guard: nelts now comes from TYPE_VECTOR_SUBPARTS of the input type,
    with a comment stating the concatenation invariant.'
- path: gcc/match.pd
  symbol: simplify BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3)
  lines: 11053-11088
  why: The modulo-(2 * nelts) reduction, plus the same-input, contiguity and alignment
    checks for subvector extraction.
- path: gcc/match.pd
  symbol: simplify BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3)
  lines: 11089-11092
  why: The rewrite that picks @1 or @2 and rebases the bit offset, where a wrong nelts
    turns into wrong code or invalid GIMPLE.
- path: gcc/testsuite/gcc.dg/torture/vec-perm-bitfield-ref-wide-input-1.c
  symbol: f1
  lines: 1-30
  why: 8-lane inputs and a 4-lane result, where selector value 6 must resolve to a[6]
    and not b[2].
- path: gcc/testsuite/gcc.dg/torture/vec-perm-bitfield-ref-narrow-input-1.c
  symbol: f1
  lines: 13-21
  why: 4-lane inputs and an 8-lane result, where selector value 5 must resolve to
    b[1] and not an out-of-range a[5].
takeaways:
- A permute selector has one entry per output lane, and each entry indexes the concatenation
  of the inputs. Don't mix up the two lengths.
- Bound selector arithmetic (modulo, input choice, rebasing) by the input length,
  read from the input's type.
- An index error that stays in range gives silent wrong code, and one that goes out
  of range gives a verifier ICE. The same bug can show either symptom.
- Writing tests in GIMPLE (-fgimple) fixes the IR shape a fold sees, so the test doesn't
  depend on the vectorizer producing that shape.
- When one pattern turns out to have a hidden width assumption, check the patterns
  next to it that match the same shape.
further_reading:
- title: 'Commit ca6ddc9: match.pd: Index BIT_FIELD_REF of VEC_PERM_EXPR inputs by
    their length'
  url: https://github.com/gcc-mirror/gcc/commit/ca6ddc9ecd74b89284ecede2ed90f768f70d88a5
primer_expert: This is the `(BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3) @rsize
  @rpos)` simplifier in `gcc/match.pd`. genmatch turns it into gimple-match code,
  and forwprop reaches it through gimple folding. The non-obvious point is that `VEC_PERM_EXPR`
  allows the input lane count to differ from the result lane count, so `VECTOR_CST_NELTS
  (sel)` is not equal to `TYPE_VECTOR_SUBPARTS (TREE_TYPE (@1))`. According to the
  commit message, generic vector lowering of narrowing permutes produces such shapes,
  which ties this fold to tree-vect-generic output.
primer_glossary:
- term: GIMPLE
  definition: 'GCC''s main middle-end intermediate representation: a simplified, three-address,
    SSA-based form of the program that most optimization passes run on.'
- term: match.pd
  definition: A domain-specific pattern file in GCC that describes algebraic simplifications.
    The genmatch tool compiles it into C++ simplifiers that GIMPLE folding and passes
    such as forwprop call.
- term: simplify pattern
  definition: An entry in match.pd of the form (simplify MATCH RESULT). It can include
    (with { C++ }) blocks for computation and (if COND ...) guards. Operands are bound
    to captures like @0 and @1.
- term: VEC_PERM_EXPR
  definition: GCC's tree code for a two-input vector shuffle. Each selector lane picks
    one lane from the concatenation of the two input vectors.
- term: selector
  definition: The third operand of a VEC_PERM_EXPR. It is a vector of indices, one
    per result lane, and each index points into the concatenation of the two inputs.
- term: VECTOR_CST
  definition: A compile-time constant vector in GCC's tree representation. When the
    permute selector is a VECTOR_CST, every lane mapping is known statically.
- term: BIT_FIELD_REF
  definition: A GCC tree code that reads a given number of bits at a given bit offset
    from an object. On vectors it is used to extract one lane or a contiguous subvector.
- term: TYPE_VECTOR_SUBPARTS
  definition: A GCC macro that returns the number of elements in a vector type, as
    a poly_uint64 so that scalable vectors are supported.
- term: VECTOR_CST_NELTS
  definition: A GCC macro that returns the number of elements in a constant vector.
    For a permute selector this equals the result's lane count.
- term: is_constant
  definition: A method on GCC's poly_int types that returns true if the value is a
    compile-time constant, and not a runtime multiple as with scalable vectors. It
    optionally stores the constant value through a pointer argument.
landing_slug: 2026-10-18-match-pd-ca6ddc9e
url: https://github.com/gcc-mirror/gcc/commit/ca6ddc9ecd74b89284ecede2ed90f768f70d88a5
week_start: '2026-10-12'
week_end: '2026-10-18'
commit_date: '2026-10-18'
date: '2026-10-18'
is_stub: false
stub_reason: ''
---

## Background: shuffles, extractions, and the pattern folder

GCC's middle end represents a vector shuffle as a `VEC_PERM_EXPR <a, b, sel>`. It takes two input vectors and a selector. Each selector lane says which input lane to copy into that position of the result. When the selector is a compile-time constant (a `VECTOR_CST`), the compiler knows exactly where every output lane comes from, and that is what makes optimization possible.

The opposite operation, pulling one lane or a contiguous run of lanes out of a vector, is a `BIT_FIELD_REF <T> (v, size, pos)`. It reads `size` bits starting at bit `pos` of `v` and reinterprets them as type `T`. With a scalar `T` it extracts one element. With a vector `T` it extracts a subvector.

These two expressions often appear together: a shuffle builds a vector and some later code reads only part of it. If the selector is constant, the shuffle can be skipped by reading the wanted lanes straight from `a` or `b`. GCC does this rewrite in `gcc/match.pd`, a pattern language that generates the simplifiers used both by GIMPLE folding and by passes like forwprop. Each `(simplify PATTERN RESULT)` entry matches a tree shape, binds operands to `@` captures, runs C++ guard code in `(with ...)` blocks, and emits a replacement.

The fold relies on a fact that is easy to lose track of: a `VEC_PERM_EXPR` does not need its inputs and its result to have the same number of lanes. The selector has one entry per *result* lane, but each entry indexes into the *inputs*. This week's fix is about keeping those two lengths separate.

## The mechanism: how the fold reasons about the selector

The pattern lives at `gcc/match.pd` lines 11035-11092:

```
(simplify
 (BIT_FIELD_REF (vec_perm@0 @1 @2 VECTOR_CST@3) @rsize @rpos)
```

`@0` is the permute, `@1` and `@2` are the inputs `a` and `b`, and `@3` is the constant selector. The guard computes `elem_size` from the element type of the permute result and `size` from the extracted type. It then turns the bit position into a lane number, using `constant_multiple_p (tree_to_poly_uint64 (@rpos), elem_size, &idx)`. When the extraction is a subvector, it also computes `nelts_op`, the number of lanes extracted, and requires it to be a power of two.

The key variable is `nelts`. Selector values index the concatenation `a ++ b`. A value `i < nelts` names `a[i]`, and a value in `[nelts, 2*nelts)` names `b[i - nelts]`. Every selector read is therefore reduced modulo `2 * nelts`:

```
if (known_eq (size, elem_size))
  idx = TREE_INT_CST_LOW (VECTOR_CST_ELT (@3, idx)) % (2 * nelts);
```

For a subvector, the rule reads selector entries `idx` through `idx + nelts_op - 1` and checks three things. All of them must land in the same input (`(start < nelts) != (end < nelts)` rejects a run that crosses from `a` into `b`). They must be consecutive. And `start % nelts_op` must be zero, so the alignment is no worse than before. If the checks pass, the rewrite picks an input and rebases the offset:

```
(if (idx < nelts)
 (BIT_FIELD_REF @1 @rsize { bitsize_int (idx * elem_size); })
 (BIT_FIELD_REF @2 @rsize { bitsize_int ((idx - nelts) * elem_size); }))
```

`nelts` appears in all three decisions: the modulo, the `a`-or-`b` test, and the rebase into `b`. Each of those boundaries is the length of one input.

## The change: take nelts from the inputs

Before this commit, the guard filled `nelts` from the selector:

```
&& VECTOR_CST_NELTS (@3).is_constant (&nelts)
```

`VECTOR_CST_NELTS (@3)` is the number of selector entries, which equals the number of result lanes. The commit keeps that call only as a check that the selector length is constant, and fills `nelts` from the type of the first input instead:

```
&& VECTOR_CST_NELTS (@3).is_constant ()
&& TYPE_VECTOR_SUBPARTS (TREE_TYPE (@1)).is_constant (&nelts)
```

A new comment states the invariant: *"NELTS is the number of elements in each input, which may differ from that of the result; the selector indexes their concatenation."*

The new tests show both failure directions. In the wide-input test, `a` and `b` are `v8hi` (8 lanes) and the result is `v4hi`. The selector is `{ 13, 6, 2, 9 }`, and the code extracts lane 1, which holds selector value 6. With the correct `nelts = 8`, 6 is below 8, so the value is `a[6]`, which the test sets to 7. The old code used `nelts = 4`, so 6 was at or above 4 and the fold rewrote the read as `b[2]`. That is a valid GIMPLE expression with the wrong value: a silent miscompile.

The narrow-input test reverses the shapes. The inputs are `v4hi`, the result is `v8hi`, the selector is `{ 0, 5, 2, 3, 4, 5, 6, 7 }`, and the code extracts lane 1 (value 5). With `nelts = 4`, 5 means `b[1]` (102). With the old `nelts = 8`, 5 was below 8, so the fold emitted `BIT_FIELD_REF` of `a` at lane 5. `a` has only four lanes, so that reference falls outside the vector, and the commit message says it fails GIMPLE verification. Each test also has a two-lane subvector case (`f2`) that goes through the contiguity and alignment checks.

## Consequences for everyone else

If you write vector intrinsics or code that auto-vectorizes, you probably never write a width-changing `VEC_PERM_EXPR` yourself. According to the commit message, though, the compiler makes them for you. Explicit element extraction is one source. Vector lowering is another: when it lowers an unsupported narrowing permute whose input is a narrowing permute the target supports, it emits `BIT_FIELD_REF`s that forwprop then folds with this rule. The dossier did not trace that lowering path in the source, so take it as the author's description. What it means is that the bug could be reached from ordinary C, not only from hand-written GIMPLE.

The two symptoms point in different directions when you debug. The wide-input case gives wrong lane values and no diagnostic, the kind of bug that shows up as a checksum mismatch in a SIMD kernel at `-O2`. The narrow-input case is louder: an internal compiler error from the GIMPLE verifier. If you have hit either on code that extracts lanes from a shuffle that changes width, this commit is a candidate fix.

The bug is worth remembering beyond this rule. Any code that interprets a permute selector has two lengths in scope, and only the input length is the right boundary for selector values. The research notes point out that `match.pd` has at least two other patterns with the same selector shape (near lines 12948 and 13010) that were not reviewed here. Whether they make the same assumption is still an open question.

## See it yourself

Both tests are written directly in GIMPLE, using GCC's `-fgimple` front-end extension. Functions marked `__GIMPLE()` contain `__VEC_PERM (a_, b_, _Literal (v4hi) { ... })` and `__BIT_FIELD_REF <short> (c_, 16, 16)`. This fixes the exact IR shape, so the vectorizer's heuristics can't steer around the rule. `__attribute__((noipa))` stops interprocedural passes from propagating the global inputs into the function.

The tests live in `gcc.dg/torture/`, so the harness runs them across the standard matrix of optimization levels. Run them with:

```
make check-gcc RUNTESTFLAGS="dg-torture.exp=vec-perm-bitfield-ref-*"
```

To watch the fold work, compile a test by hand with `-fgimple -O2 -fdump-tree-forwprop-details` (or `-fdump-tree-all`) and compare the IR before and after the forwprop dump. The `c_ = VEC_PERM_EXPR <...>` followed by a `BIT_FIELD_REF` of `c_` should become a single `BIT_FIELD_REF` of `a_` or `b_`. Check which input it picks against your own calculation of `selector[idx] % (2 * nelts_input)`.
