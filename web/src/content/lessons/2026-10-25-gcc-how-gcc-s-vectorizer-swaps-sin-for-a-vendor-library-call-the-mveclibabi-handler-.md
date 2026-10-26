---
project: gcc
subsystem: gcc/config/i386
patch_id: null
tags:
- vectorization
- x86
- math-libraries
- fast-math
- target-hooks
lesson_id: gcc:2026-W43
commit_hash: 5db04303f76bc4c5705b753e0b1377c117ff9f19
source_type: github
headline: 'How GCC''s Vectorizer Swaps sin() for a Vendor Library Call: the -mveclibabi
  Handler Pattern'
hook: A loop of sinf() calls can compile to calls to a symbol you never wrote, such
  as hvml_vs16_sin. This lesson covers who picks that name, when the swap is refused,
  and why.
tldr: The x86 backend turns scalar math calls in vectorized loops into calls to an
  external vector library through a handler function. HVML is the newest handler.
concept: A vector math ABI in GCC is a function that takes a scalar math operation
  plus a vector type and returns either an external declaration with the library's
  naming convention, or NULL_TREE to refuse. Each refusal makes the vectorizer try
  something else.
prerequisites:
- what loop auto-vectorization does
- SIMD register widths (SSE 128, AVX 256, AVX-512 512 bits)
- the difference between a declaration and a definition at link time
- what -ffast-math loosens
code_tour:
- path: gcc/config/i386/i386-builtins.cc
  symbol: ix86_vectorize_builtin
  lines: 1702-1711
  why: The fallthrough point where the x86 backend hands a vectorization request to
    the selected library handler.
- path: gcc/config/i386/i386-options.cc
  symbol: ix86_option_override_internal
  lines: 2824-2846
  why: The switch that binds the -mveclibabi value to a handler pointer once, at option-override
    time.
- path: gcc/config/i386/i386.opt
  symbol: mveclibabi
  lines: 570-588
  why: The .opt records that map the user-facing strings svml/acml/aocl/hvml to enum
    values.
- path: gcc/config/i386/i386.cc
  symbol: ix86_veclibabi_hvml
  lines: 20821-20866
  why: The guards (TARGET_64BIT, flag_unsafe_math_optimizations), the mode and lane-count
    checks, and the GET_VW_INFO macro.
- path: gcc/config/i386/i386.cc
  symbol: ix86_veclibabi_hvml
  lines: 20866-20959
  why: The per-function {single, double} width tables and the membership check on
    the requested lane count.
- path: gcc/config/i386/i386.cc
  symbol: ix86_veclibabi_hvml
  lines: 20961-21012
  why: Symbol-name construction from the scalar builtin's identifier, the log-to-ln
    rewrite, and arity-driven function type building.
- path: gcc/testsuite/gcc.target/i386/vectorize-hvml-3.c
  symbol: ''
  lines: 1-23
  why: Shows -mno-avx limiting output to 128-bit hvml_vs4_sin/hvml_vd2_sin.
- path: gcc/testsuite/gcc.target/i386/vectorize-hvml-2.c
  symbol: ''
  lines: 1-21
  why: 'Negative test: without unsafe math, no hvml_v symbols are emitted.'
takeaways:
- 'A vector math library ABI in GCC is a decision function: return an external decl
  with the library''s mangled name, or NULL_TREE to refuse.'
- 'Vendor vector math calls only appear when every check passes: target word size,
  math-relaxation flags, element mode, operation, and lane count.'
- GCC emits calls to vector math libraries but never provides them, so the linker
  must find the vendor's library.
- Deriving names from existing builtin identifiers keeps a mapping tied to the compiler's
  own function list and avoids a parallel string table that can drift.
- Keeping per-case data inside each case label, as GET_VW_INFO does, keeps the data
  from drifting out of sync with the switch.
further_reading:
- title: 'gcc commit 5db04303f76b: i386: Add -mveclibabi=hvml'
  url: https://github.com/gcc-mirror/gcc/commit/5db04303f76bc4c5705b753e0b1377c117ff9f19
primer_expert: The libcall fallback of the i386 builtin_vectorized_function hook,
  `ix86_vectorize_builtin`, dispatches through `ix86_veclib_handler`, which is chosen
  once from `-mveclibabi` in `ix86_option_override_internal`. Each handler maps a
  `combined_fn` and vector types to a synthesized external decl. HVML reads per-CFN
  lane counts from static tables and copies the operation name out of the `mathfn_built_in`
  decl's identifier. The handler only accepts or rejects the vectorizer's width, so
  `-mprefer-vector-width` and the ISA flags decide which variant is emitted.
primer_glossary:
- term: -mveclibabi
  definition: An x86 GCC option that names the external vector math library whose
    naming and calling convention the vectorizer should target when it vectorizes
    calls to math functions.
- term: combined_fn
  definition: A GCC enumeration that covers both built-in functions and internal functions
    with one set of codes. Backend hooks receive it to identify which math operation
    is being vectorized.
- term: CASE_CFN_*
  definition: Macros that expand to the case labels for every variant of one math
    family (float, double, long double, and so on), so a single switch arm handles
    sin, sinf and sinl.
- term: NULL_TREE
  definition: The null value of GCC's `tree` IR node type. A hook returns it to mean
    "no answer" or "not supported".
- term: tree
  definition: GCC's generic IR node type. Declarations, types and expressions are
    all trees.
- term: FUNCTION_DECL
  definition: The tree node that represents a function declaration. An external one
    with no body tells later passes to emit a call that the linker resolves.
- term: SFmode / DFmode
  definition: GCC machine modes for 32-bit single-precision and 64-bit double-precision
    floating-point values, the backend's view of float and double.
- term: TYPE_VECTOR_SUBPARTS
  definition: A macro that returns the number of elements (lanes) in a vector type,
    for example 4 for a 128-bit vector of floats.
- term: mathfn_built_in
  definition: A GCC helper that returns the scalar builtin declaration (such as __builtin_sinf)
    for a given math function code and floating-point type, or null if none exists.
- term: -funsafe-math-optimizations
  definition: A flag, enabled by -ffast-math, that lets GCC apply transformations
    that may change floating-point results, such as reassociation or calls to less
    accurate math routines.
landing_slug: 2026-10-23-i386-5db04303
url: https://github.com/gcc-mirror/gcc/commit/5db04303f76bc4c5705b753e0b1377c117ff9f19
week_start: '2026-10-19'
week_end: '2026-10-25'
commit_date: '2026-10-23'
date: '2026-10-25'
is_stub: false
stub_reason: ''
---

## Background: who vectorizes a call to sin()?

Take a loop like `dst[i] = sinf (src[i])`. GCC's loop vectorizer can run four, eight or sixteen iterations at once in one SIMD register. It cannot do that with `sinf` itself, because the hardware has no vector sine instruction and `sinf` takes one float. To vectorize the loop, the vectorizer needs a function that takes a whole vector of floats and returns a vector of results.

The vectorizer does not know where to find one, so it asks the target backend. On x86 the backend answers in `ix86_vectorize_builtin` in `gcc/config/i386/i386-builtins.cc`. That function first checks the native x86 vector builtins. If none of them fit, it hands the question to a pluggable handler:

```c
  /* Dispatch to a handler for a vectorization library.  */
  if (ix86_veclib_handler)
    return ix86_veclib_handler (combined_fn (fn), type_out, type_in);

  return NULL_TREE;
```

`ix86_veclib_handler` is a function pointer. When it is non-null, it represents one vendor's vector math library: Intel SVML, AMD ACML, AMD AOCL, and as of this week HYGON's HVML. The user picks one with `-mveclibabi=`. Each library has its own symbol-naming scheme, so each needs its own handler. That is why the option ends in "abi": it chooses a calling and naming convention, not an implementation. GCC ships none of these libraries. It only emits calls to them, and the linker must find the definitions.

## The mechanism: a handler is a decision function

Every handler has the signature declared in `i386-options.h`:

```c
extern tree (*ix86_veclib_handler) (combined_fn, tree, tree);
```

The first argument is a `combined_fn`, GCC's single enumeration that covers both builtins and internal functions. Each scalar math family, such as `sin`/`sinf`, maps to it through a `CASE_CFN_*` label. The other two arguments are the output and input vector types. The handler has two possible answers. It can return a `tree` that declares an external function with the right vector signature, and the vectorizer then emits a call to it. Or it can return `NULL_TREE`, which means "no such function". The vectorizer then tries a different vector width, or leaves the loop scalar.

The pointer is set once, in `ix86_option_override_internal`, and only when the user passed `-mveclibabi` explicitly (`opts_set->x_ix86_veclibabi_type`):

```c
      case ix86_veclibabi_type_hvml:
	ix86_veclib_handler = &ix86_veclibabi_hvml;
	break;
```

The option spelling comes from GCC's `.opt` machinery. `i386.opt` declares `mveclibabi=` as `Joined Var(ix86_veclibabi_type) Enum(ix86_veclibabi)`, and each `EnumValue` record maps a string to a member of `enum ix86_veclibabi` in `i386-opts.h`. Adding a library takes four plumbing edits: an enum member, an `EnumValue`, a switch case, and an `extern` declaration. The fifth piece, the handler itself, holds all the real logic.

## The change: ix86_veclibabi_hvml, step by step

The new handler in `i386.cc` runs a series of checks, and any of them can refuse the request. The first two are policy checks:

```c
  if (!TARGET_64BIT || !flag_unsafe_math_optimizations)
    return NULL_TREE;
```

The source comment explains why: HVML "is 64-bit only and is suitable only for unsafe math, since it trades off some accuracy for increased performance." Next comes a shape check. The element mode and lane count (`TYPE_VECTOR_SUBPARTS`) of `type_out` and `type_in` must be equal, and the element mode must be `SFmode` (float) or `DFmode` (double).

Then the handler looks up which widths HVML provides for this operation. A local macro, `GET_VW_INFO`, sits inside each `case` and creates a `static const int widths[2][3]`. Row 0 lists the single-precision lane counts, row 1 lists the double-precision ones, and zeros fill unused slots:

```c
    CASE_CFN_SIN:
      GET_VW_INFO ({  4,  8, 16 }, {  2,  4,  8 });
    ...
    CASE_CFN_ERF:
      GET_VW_INFO ({  4, 16,  0 }, {  2,  4,  0 });
```

So `sinf` exists in 128-, 256- and 512-bit forms, while float `erf` has 4- and 16-lane versions but no 8-lane version. The comment explains why the table lives next to each case: "Keep each set with its case so the mapping cannot get out of sync." Any family not listed reaches `default: return NULL_TREE`. The handler then picks the row with `j = el_mode == DFmode` and scans its three entries for the requested `n`. If `n` is missing, the handler refuses.

Last, the handler builds the symbol name in a 30-byte buffer that starts as `"hvml_v"`. It appends `s` or `d` for precision, then the lane count (`2`, `4`, `8`, or `16`), then `_`. It does not keep a separate string table for the operation name. Instead it takes the name from the scalar builtin, which it gets with `mathfn_built_in`:

```c
      const char *bname = IDENTIFIER_POINTER (DECL_NAME (fndecl)) + 10;
```

The `+ 10` skips `__builtin_`. For float it drops the trailing `f`, so `__builtin_sinf` yields `sin`. Natural log is the one exception: HVML calls it `ln`, so `BUILT_IN_LOGF` and `BUILT_IN_LOG` are rewritten to that. The handler counts the scalar decl's `DECL_ARGUMENTS` to find the arity, then builds either a `(type_out, type_in)` or a `(type_out, type_in, type_in)` function type. That covers two-argument operations such as `pow`, `atan2` and `fmod`. The results are names like `hvml_vs4_sin`, `hvml_vd2_ln` and `hvml_vs16_sin`.

## Why the design matters: the builtin is the source of truth

The commit message points out a quiet detail. The table covers 39 families, including the seven C23 pi-based trigonometric functions (`acospi`, `asinpi`, `atanpi`, `atan2pi`, `cospi`, `sinpi`, `tanpi`). These look up their scalar decl through the common `mathfn_built_in` path, "avoiding target-specific builtin declaration handling". The commit says their type-specific lookup was completed only recently, by r17-5176. Because the operation name comes from the builtin's identifier, any family that `mathfn_built_in` can resolve gets a correctly spelled HVML name for free. When the lookup fails, `if (!fndecl) return NULL_TREE;` refuses safely instead of emitting a malformed symbol.

The design has a clear split. The width table is HVML-specific data: which widths exist for which operation. The naming logic is generic, except for the `ln` rewrite. The buffer bound is enforced with `gcc_checking_assert (name_len + bname_len < sizeof (name))`, so a future family with a longer name fails loudly in checking builds rather than overflowing the buffer.

## Consequences for code you build

If you build for 64-bit x86 with `-funsafe-math-optimizations` (which `-ffast-math` turns on) and `-mveclibabi=hvml`, vectorizable loops over the mapped math functions now call `hvml_v*` symbols. Expect these practical effects:

- You must link against a library that defines those names. GCC only emits the calls, and the commit contains nothing that provides them. An undefined `hvml_vs8_exp` at link time means you chose the ABI but did not link the library.
- Results can differ from the scalar libm results. That accuracy trade-off is the reason for the guard. Without unsafe math the handler always refuses, and you get no HVML calls even with `-mveclibabi=hvml` on the command line.
- On 32-bit targets the handler always refuses. The commit also updates `invoke.texi` to state that the ACML and AOCL ABIs have the same 64-bit restriction.
- The width you get depends on the ISA you enable. The handler only accepts or rejects the width the vectorizer asks for. In `vectorize-hvml-3.c`, `-mno-avx` produces only `hvml_vs4_sin` and `hvml_vd2_sin`, the 128-bit forms.
- A missing width is not an error. If HVML lacks a variant, as with float `erf` at 8 lanes, the handler returns `NULL_TREE` and the compiler falls back to something else.

The same reasoning applies to every `-mveclibabi` value. When a math loop did not turn into a vendor call, one of the handler's checks refused it: the 64-bit check, unsafe math, element mode, the operation not being in the table, the width not being in the table, or the scalar builtin lookup failing.

## See it yourself

The positive test, `gcc.target/i386/vectorize-hvml-3.c`, shows the exact recipe:

```sh
gcc -O2 -ftree-vectorize -funsafe-math-optimizations -fno-math-errno \
    -march=c86-4g-m7 -mno-avx -mveclibabi=hvml -S t.c
```

Run it on a 64-iteration `sinf` loop and a 64-iteration `sin` loop, then grep the assembly. You should find `hvml_vs4_sin` and `hvml_vd2_sin`, and none of `hvml_v(s8|s16|d4|d8)_`. Change `-funsafe-math-optimizations` to `-fno-unsafe-math-optimizations`, as `vectorize-hvml-2.c` does, and every `hvml_v` reference disappears, even with `-mprefer-vector-width=512`.

For the full matrix, the commit message says `vectorize-hvml-1.c` checks all 194 operation, precision and width combinations, using `-march=c86-4g-m7 -mprefer-vector-width=512`. To watch the vectorizer accept or reject the call, add `-fopt-info-vec` and compare the output with and without the guard flags.
