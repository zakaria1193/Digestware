---
project: gcc
subsystem: gcc/rs6000
patch_id: null
tags:
- _BitInt
- C23
- ABI
- rs6000
- libgcc
lesson_id: gcc:2026-W37
commit_hash: 83998f47450c088493c971d46ae3b6dadb7242b3
source_type: github
headline: 'What It Takes to Port a Type: _BitInt Arrives on PowerPC'
hook: C23 gave you _BitInt(729). The middle end has known how to lower it for two
  years. Learn why it still did nothing on PowerPC until a target hook answered "what
  is a limb?"
tldr: rs6000 now implements TARGET_C_BITINT_TYPE_INFO, an ABI by-reference threshold,
  and libgcc conversion helpers — the three things a target owes a new integer ty…
concept: 'A new integer type is not a front-end feature. It becomes real only when
  a target answers three questions: what is a limb, how do limbs sit in memory, and
  when does the value stop travelling in registers.'
prerequisites:
- what a target hook is in GCC
- machine modes (QImode, DImode) as a concept
- how arguments are passed in registers vs. by hidden pointer
- what libgcc provides at runtime
- endianness of multi-word integers
code_tour:
- path: gcc/config/rs6000/rs6000-call.cc
  symbol: rs6000_bitint_large_p
  lines: 400-410
  why: The by-reference threshold and, in its comment, the reason it exists as one
    function instead of two copies.
- path: gcc/config/rs6000/rs6000.cc
  symbol: rs6000_bitint_type_info
  lines: 1116-1140
  why: The new hook implementation's home in the backend's forward declarations and
    definitions.
- path: gcc/config/rs6000/rs6000.cc
  symbol: TARGET_C_BITINT_TYPE_INFO
  lines: 6608-6610
  why: The hook macro definition that flips _BitInt from unsupported to supported
    on this target.
- path: libgcc/config/rs6000/fixtfbitint-ibm128.c
  symbol: __fixtfbitint
  lines: 1-120
  why: 'Shows the double-double conversion strategy: convert the high double, then
    add the low double into the limb array with carries.'
- path: libgcc/config/rs6000/floatbitinttf-ibm128.c
  symbol: __floatbitinttf
  lines: 1-120
  why: The reverse direction, including the overflow-to-infinity path and the careful
    undoing of the sticky low bit from FP_FROM_BITINT.
- path: gcc/testsuite/gcc.target/powerpc/bitint-abi-call.c
  symbol: id128 / id129
  lines: 1-120
  why: 'A readable ABI specification: noipa identity and combining functions straddling
    the _BitInt(129) transition.'
- path: gcc/config/rs6000/rs6000-call.cc
  symbol: rs6000_return_in_memory
  lines: 1240-1270
  why: The surrounding argument-accumulation and TARGET_DEBUG_ARG tracing that shows
    how the backend tracks registers and stack words per argument.
takeaways:
- 'A front-end feature can be fully implemented and still absent on a target: an unanswered
  target hook makes it invisible, not buggy.'
- Wide integers live as arrays of limbs; the limb mode a target picks decides both
  code size and memory layout.
- When padding bits above a type's precision are unspecified, bytewise comparison
  and hashing of that type are wrong by construction.
- An ABI threshold used by two hooks belongs in one function — divergence between
  pass and return rules is a silent cross-TU bug.
- ABI tests need optimisation barriers like noipa, and must probe immediately above
  and below every numeric threshold.
further_reading:
- title: 'rs6000: Add ABI and libgcc support for C23 _BitInt [PR117584]'
  url: https://github.com/gcc-mirror/gcc/commit/83998f47450c088493c971d46ae3b6dadb7242b3
primer_expert: 'rs6000 is the last major Linux target to wire up TARGET_C_BITINT_TYPE_INFO.
  Two details are rs6000-specific and easy to miss: the by-reference threshold differs
  by ABI (16 bytes ELFv2, 8 bytes AIX32/V4), now centralised in rs6000_bitint_large_p
  so rs6000_return_in_memory and rs6000_pass_by_reference cannot diverge; and __ibm128
  forces a hand-written double-double path, so bitinttofp_optab/bitintfromfp_optab
  get distinct libfuncs from init_float128_ibm (__floatbitinttf/__fixtfbitint) and
  init_float128_ieee (__floatbitintkf/__fixkfbitint). Note also rs6000_function_value
  must exempt BITINT_TYPE…'
primer_glossary:
- term: _BitInt
  definition: A C23 integer type with a programmer-chosen bit width, written `_BitInt(N)`.
    Unlike `int` or `long long`, its precision is exactly N bits, so arithmetic wraps
    at N rather than at a machine word boundary.
- term: limb
  definition: The fixed-size machine integer used as the building block of a wider
    software integer. A 200-bit value stored as four 64-bit limbs behaves like a little
    array; the term comes from arbitrary-precision arithmetic libraries.
- term: target hook
  definition: A function pointer in GCC's `targetm` structure through which the machine-independent
    compiler asks a specific backend a question. If a backend leaves a hook at its
    default, the feature guarded by that hook simply does not exist for that target.
- term: TARGET_C_BITINT_TYPE_INFO
  definition: 'The target hook through which a backend describes `_BitInt` to the
    C front end and middle end: which machine mode a limb uses, whether the ABI limb
    matches the internal one, and what the padding bits above the declared precision
    mean.'
- term: machine mode
  definition: GCC's name for the size-and-class of a value in the RTL layer. QImode,
    HImode, SImode and DImode are 8-, 16-, 32- and 64-bit integers respectively; a
    mode is what the register allocator and instruction patterns actually reason about.
- term: bitint_ext_undef
  definition: The setting a backend chooses when the bits above a `_BitInt`'s declared
    precision in its top limb carry no guaranteed value, so no reader may depend on
    them being zero- or sign-extended.
- term: ELFv2
  definition: The PowerPC 64-bit ELF ABI used by little-endian Linux distributions,
    replacing the older ELFv1/AIX-descended conventions. Among other differences it
    changes how large aggregates are passed and returned.
- term: hidden pointer (return in memory)
  definition: 'An ABI technique for returning objects too large for registers: the
    caller allocates storage and passes its address as an invisible extra first argument,
    which the callee fills in.'
- term: rs6000
  definition: The internal name of GCC's PowerPC backend, kept from the IBM RS/6000
    workstations. Its source lives under `gcc/config/rs6000/`.
- term: libgcc
  definition: The low-level runtime library GCC ships with itself. When a target lacks
    an instruction for some operation, the compiler emits a call to a libgcc helper
    such as a soft-float conversion routine.
landing_slug: 2026-09-11-rs6000-83998f47
url: https://github.com/gcc-mirror/gcc/commit/83998f47450c088493c971d46ae3b6dadb7242b3
week_start: '2026-09-07'
week_end: '2026-09-13'
commit_date: '2026-09-11'
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

## The subsystem: a backend is a witness, not a bystander

GCC's C23 `_BitInt` machinery has existed in the front end and middle end for some time. The parser accepts `_BitInt(N)`, the middle end knows how to lower arithmetic on a value far wider than any register into a loop over pieces, and libgcc carries generic conversion helpers. None of that is target code.

And yet, per the commit message, `_BitInt` was "entirely unsupported" on PowerPC until this week, for one reason: "Previously `TARGET_C_BITINT_TYPE_INFO` was unimplemented on this target." That hook is the question the generic machinery asks each backend before it will admit the type exists. Leave it unanswered and the type does not compile — not badly, not slowly, at all.

This is the general shape of target support in GCC. A backend is not merely a code emitter that receives finished decisions. It is the authority on a set of questions the machine-independent layers cannot answer for themselves: what sizes exist, what the ABI says, which operations need a runtime call. `gcc/config/rs6000/` is where PowerPC answers them, and a feature that depends on an unanswered question is invisible rather than broken.

For a type as unusual as `_BitInt`, three questions matter. What is the storage unit? How do several of those units sit in memory relative to one another? And at what size does the value stop travelling in registers and start travelling as a pointer? This commit answers all three for ppc64le, ppc64 big-endian and ppc32.

## The mechanism: limbs, order, and the padding you may not read

`_BitInt(N)` cannot live in a single machine mode once N exceeds a register width. GCC represents it as an array of *limbs* — fixed-size integers the target nominates. `rs6000_bitint_type_info` in `gcc/config/rs6000/rs6000.cc` picks that limb mode by precision. From the commit message: it "selects the limb mode by precision: QImode, HImode or SImode for n <= 8, 16 or 32 respectively, and above that the widest integer that fits in one general purpose register, i.e. DImode on 64-bit PowerPC and SImode on 32-bit PowerPC."

Narrow `_BitInt`s therefore behave like the ordinary sub-word integers a PowerPC programmer already knows. Wide ones become arrays of the natural register-sized limb — DImode under `-m64`, SImode under `-m32`. That choice is not cosmetic: it decides how many loads a wide add costs and what the debugger sees.

The hook also reports two properties that together define the in-memory layout. The ABI limb mode equals the internal limb mode, so — again quoting the commit message — "a `_BitInt` wider than one limb is an array of limbs, ordered least to most significant on little-endian and most to least significant on big-endian, exactly like any other multi-word integer." No new byte-order rule; `_BitInt` inherits the one PowerPC already uses for multi-word integers.

The second property is the one to remember. Bits above the declared precision in the most significant limb are unspecified — `bitint_ext_undef`. If you declare `_BitInt(65)` on ppc64 you get two DImode limbs, 128 bits of storage, and 63 bits at the top whose contents you may not depend on. Code that memcmps two `_BitInt(65)` values, or hashes their bytes, is reading garbage. The commit message is explicit that neither property is conditional on endianness, so "the same rule describes ppc64le, ppc64 big-endian and ppc32."

## The change: one threshold, computed in one place

The second half of the target's obligation is calling convention. Large integers do not fit in the argument registers, so they must be passed the way large aggregates are — through memory, with the callee receiving an address. Where "large" begins depends on the ABI. The new helper in `gcc/config/rs6000/rs6000-call.cc` states it in its own comment:

```c
/* Return true if a _BitInt with byte size SIZE must be passed or returned
   by reference rather than in registers.  SIZE < 0 (variable-length) is
   always large.  ELFv2 threshold is 16 bytes; AIX32/V4 is 8 bytes.
   Centralises the threshold so rs6000_return_in_memory and
   rs6000_pass_by_reference stay in sync.  */
static bool
rs6000_bitint_large_p (HOST_WIDE_INT size)
```

That closing sentence is the engineering lesson. `rs6000_return_in_memory` and `rs6000_pass_by_reference` are separate hooks, called at different moments, for different purposes. If one thinks `_BitInt(128)` fits in registers and the other thinks it does not, you get a caller and callee that disagree about where the value lives — the classic silent ABI bug, which reproduces only across translation units and only at certain widths. Writing the threshold once, in a function both call, makes the divergence unrepresentable rather than merely unlikely. Note also the treatment of a negative size: variable-length is "always large," the conservative answer.

Two further details show the care that an ABI predicate demands. Both call sites use `BITINT_TYPE_P` rather than a `TREE_CODE` test, "so that C2Y bit-precise enums backed by `_BitInt` are handled identically to plain `_BitInt`" — a type that is an enum at the language level but a bit-precise integer underneath must not fall through to the aggregate path by accident. And `rs6000_function_value` now excludes `BITINT_TYPE` from the generic sub-word integer promotion, "so that the mode used for a `_BitInt` return value agrees with the one the middle end computes for the type." PowerPC habitually widens a narrow integer return to a register mode; doing that to a `_BitInt` would make the backend and the middle end describe the same return value with two different modes.

The third obligation is runtime. Converting between a wide `_BitInt` and a floating-point type is not an instruction, so it is a libcall, and the compiler must know the symbol name. `init_float128_ibm` sets the `bitinttofp_optab` and `bitintfromfp_optab` libfuncs to `__floatbitinttf` and `__fixtfbitint`; `init_float128_ieee` sets them to `__floatbitintkf` and `__fixkfbitint`. PowerPC has two distinct 128-bit float formats, so it needs two distinct pairs of helpers.

The IBM double-double pair is hand-written in `libgcc/config/rs6000/floatbitinttf-ibm128.c` and `libgcc/config/rs6000/fixtfbitint-ibm128.c`, built on soft-fp. `__fixtfbitint` has the signature `void __fixtfbitint (UBILtype *r, SItype rprec, __ibm128 a)` — result by pointer, precision passed as a runtime argument, sign encoded in its own representation (`USItype rsigned = rprec < 0`). It converts the high double, writes it into the limb array with `FP_TO_BITINT`, then unpacks the low double and adds it in limb by limb with `__builtin_add_overflow` carrying between limbs. The comment records the invariant that makes this two-step approach safe: "For valid `__ibm128`, `B_e < A_e` except for the NaN and +-0 cases, but those are all `ovf = 1`." Double-double is a sum of two doubles, so a correct conversion is genuinely two conversions plus a shifted big-integer addition.

On the deployment side, `libgcc/config/rs6000/libgcc-glibc.ver` gains a `GCC_17.0.0` version node inheriting `GCC_4.2.0`, exporting `__floatbitintkf`, `__fixkfbitint`, `__floatbitinttf`, `__fixtfbitint`, `__floatbitintsf`, `__fixsfbitint`, `__floatbitintdf` and `__fixdfbitint`. New symbols under a new node: existing binaries keep resolving against the old ones.

## The consequences for everyone else

If you write PowerPC code, `_BitInt(N)` now works, and the mental model is the one you already have for multi-word integers. A value wider than one limb is an array of register-sized limbs in the target's natural byte order. `_BitInt` larger than 16 bytes under ELFv2 — 8 bytes otherwise — is passed and returned by reference, exactly as aggregates of those sizes already are. The commit's own test file, `gcc.target/powerpc/bitint-abi-call.c`, is organised around that boundary: it declares `_BitInt(128)` and `_BitInt(129)` typedefs and documents its purpose as exercising the "ABI transition at `_BitInt(129)`".

The padding rule is the part that will bite library authors. Bits above the precision are unspecified. Do not compare `_BitInt` values bytewise, do not hash their storage, do not serialise them by `memcpy` and expect a canonical form on the other end. Compare them as integers; the middle end knows the precision, your `memcmp` does not.

If you maintain a distribution or a cross toolchain, note that `_BitInt`-to-float conversion pulls in fresh libgcc symbols. The build plumbing reflects this: `libgcc/config/rs6000/t-float128` adds `floatbitintkf` and `fixkfbitint` to `fp128_softfp_funcs` and adds new binary-float sources to `LIB2ADD` unconditionally, with decimal-float sources going to `LIB2ADD_ST` only when decimal float is enabled; `libgcc/config/rs6000/t-linux` adds the `__ibm128` pair. The `float128-sed` and `float128-sed-hw` scripts gain substitution rules for `__floatbitinttf`/`__floatbitintkf` and `__fixtfbitint`/`__fixkfbitint`. A program using `_BitInt` needs a libgcc built with these rules present.

One caveat is stated in the commit itself rather than inferred: after bootstrap and regression testing on powerpc64le-linux and powerpc64-linux across both multilibs, "One known failure remains on big endian: `gcc.dg/torture/bitint-16.c` fails its `-O2` execution test with `-m32`." New ABI support landing with a documented exception is normal; what matters is that the exception is named.

## Seeing it yourself

The thirteen new tests under `gcc/testsuite/gcc.target/powerpc/` are the readable specification of what the backend now promises, and their names map to the questions above: `bitint-sizes-powerpc.c` and `bitint-alignments-powerpc.c` for layout, `bitint-endian-powerpc.c` for limb order, `bitint-args-powerpc.c` and `bitint-abi-call.c` for calling convention, `bitint-varargs.c` and `bitint-struct-layout.c` for the composition cases, `bitint-bitint-to-ibm128.c` and `bitint-ibm128-to-bitint.c` for the new libgcc routines.

`bitint-abi-call.c` is the one to read first. It is short, it is a `dg-do run` guarded by `target bitint`, and its shape is instructive: a family of `__attribute__((noipa))` identity functions — `id8`, `id16`, `id32`, `id65`, `id128`, `id129` — plus `combine65`/`combine128`/`combine129` for multiple arguments and `mix65`/`mix128` for `_BitInt` interleaved with plain `int` and `long`. The `noipa` attribute is what makes it an ABI test rather than a constant-folding test: it forbids inter-procedural optimisation, so the call really happens and the arguments really travel through the convention under test.

The `id128`/`id129` pair straddles the ELFv2 threshold. One side of that boundary is registers, the other is a hidden pointer, and an off-by-one in `rs6000_bitint_large_p` would show up there and nowhere else. That is the test-design lesson worth carrying: when a rule has a numeric threshold, test the value below it, the value above it, and nothing in between for credit.

To inspect the decisions rather than the results, `rs6000` still honours `TARGET_DEBUG_ARG`, whose tracing in `rs6000-call.cc` prints the argument accumulator state — `words`, `fregno`, `gregno`, `nargs_prototype`, `prototype` — as each argument is processed. It is the backend narrating its own calling convention, one argument at a time.
