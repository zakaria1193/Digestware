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
headline: 'Porting a Language Feature Means Answering the ABI''s Questions: _BitInt
  Arrives on PowerPC'
hook: C23's _BitInt has been in GCC's front end for years, yet it did not compile
  on PowerPC until this week. The reason is a lesson in what "target support" actually
  costs.
tldr: GCC's rs6000 backend now implements TARGET_C_BITINT_TYPE_INFO, the by-reference
  threshold for large _BitInt, and the libgcc conversion routines C23 _BitInt nee…
concept: 'A language feature is only "supported" on a target once that target''s backend
  answers the ABI questions the middle end asks it: how wide is a limb, where does
  a value live in registers, when does it move to memory. Front-end machinery is portable;
  the answers are not.'
prerequisites:
- what a target hook is in GCC
- how arguments are passed in registers vs by reference
- what libgcc provides at runtime
- basic ELF symbol versioning
- endianness of multi-word integers
code_tour:
- path: gcc/config/rs6000/rs6000-call.cc
  symbol: rs6000_bitint_large_p
  lines: 400-420
  why: The entire by-reference decision for _BitInt in six lines, including the variable-length
    case and the ELFv2-versus-AIX32/V4 thresholds.
- path: gcc/config/rs6000/rs6000-call.cc
  symbol: rs6000_return_in_memory
  lines: 400-420
  why: The comment immediately above rs6000_bitint_large_p names this hook and rs6000_pass_by_reference
    as the two callers the shared predicate keeps in sync.
- path: gcc/config/rs6000/rs6000.cc
  symbol: rs6000_bitint_type_info
  lines: ''
  why: 'Where the backend answers the middle end''s three questions: limb mode by
    precision, ABI limb mode equal to the internal one, and bitint_ext_undef padding.'
- path: gcc/config/rs6000/rs6000.cc
  symbol: init_float128_ibm
  lines: ''
  why: Sets bitinttofp_optab and bitintfromfp_optab to __floatbitinttf and __fixtfbitint
    for the IBM double-double long double format.
- path: gcc/config/rs6000/rs6000.cc
  symbol: init_float128_ieee
  lines: ''
  why: The IEEE binary128 counterpart, naming __floatbitintkf and __fixkfbitint.
- path: gcc/config/rs6000/rs6000.cc
  symbol: rs6000_function_value
  lines: ''
  why: Excludes BITINT_TYPE from sub-word integer return promotion so the backend
    and the middle end agree on the return mode.
- path: libgcc/config/rs6000/libgcc-glibc.ver
  symbol: GCC_17.0.0
  lines: ''
  why: The new version node inheriting GCC_4.2.0 that exports the eight new _BitInt
    conversion symbols.
- path: libgcc/config/rs6000/t-float128
  symbol: fp128_softfp_funcs
  lines: ''
  why: Shows how floatbitintkf and fixkfbitint plus the new rs6000_bitint_bin_* and
    rs6000_bitint_dec_* lists enter LIB2ADD and LIB2ADD_ST.
takeaways:
- A language feature is unsupported on a target until that target's hook answers the
  ABI questions — front-end machinery alone compiles nothing.
- When two hooks must agree on a threshold, compute it once in a shared predicate;
  drift between rs6000_return_in_memory and rs6000_pass_by_reference is a silent ABI
  break.
- 'Test the type predicate, not the TREE_CODE: BITINT_TYPE_P also catches enums whose
  underlying type is a _BitInt.'
- Declaring padding bits above the precision unspecified (bitint_ext_undef) is cheaper
  than promising an extension nobody needs.
- New public libgcc symbols belong in a new version node, so a too-old libgcc_s fails
  at load time instead of mid-execution.
further_reading:
- title: 'rs6000: Add ABI and libgcc support for C23 _BitInt [PR117584]'
  url: https://github.com/gcc-mirror/gcc/commit/83998f47450c088493c971d46ae3b6dadb7242b3
primer_expert: 'The gate is `TARGET_C_BITINT_TYPE_INFO` in `config/rs6000/rs6000.cc`:
  unimplemented meant `_BitInt` diagnosed as unsupported, regardless of the target-independent
  bitint lowering. `rs6000_bitint_type_info` sets limb mode by precision (QI/HI/SImode,
  then one GPR: DImode on ppc64, SImode on ppc32), ABI limb mode equal to internal,
  and `bitint_ext_undef`. Non-obvious neighbours: `rs6000_function_value`''s sub-word
  promotion had to stop applying to BITINT_TYPE, and both `init_float128_ibm` and
  `init_float128_ieee` need their own `bitinttofp_optab`/`bitintfromfp_optab` libfuncs
  because TFmode and K…'
primer_glossary:
- term: _BitInt
  definition: A C23 integer type, `_BitInt(N)`, with exactly N value bits for any
    N the implementation supports. Unlike `int` or `long` its width comes from the
    declaration, so the compiler must synthesise arithmetic for widths no register
    holds.
- term: target hook
  definition: A function pointer in GCC's `targetm` structure that target-independent
    code calls to ask the backend a machine-specific question. Each hook has a default;
    a backend overrides it by defining the corresponding `TARGET_*` macro.
- term: TARGET_C_BITINT_TYPE_INFO
  definition: The target hook through which GCC asks a backend how `_BitInt` is represented
    on this machine — limb mode, ABI limb mode, and padding-bit semantics. If a backend
    does not implement it, `_BitInt` is rejected on that target.
- term: limb
  definition: One fixed-size integer chunk of a multi-precision value, the term borrowed
    from bignum libraries. A wide `_BitInt` is stored as an array of limbs, and the
    limb mode determines how many limbs a given precision needs.
- term: bitint_ext_undef
  definition: The setting a backend returns to declare that bits above the declared
    precision in the most significant limb of a `_BitInt` hold unspecified values,
    as opposed to being zero- or sign-extended. Code must mask before relying on them.
- term: QImode / HImode / SImode / DImode
  definition: GCC's machine modes for 8-, 16-, 32- and 64-bit integers respectively.
    A mode names the size and class of a value in RTL, independent of the source-level
    type.
- term: TFmode / KFmode
  definition: Two of GCC's 128-bit floating-point modes. On PowerPC, TFmode is used
    for the IBM double-double `long double` format and KFmode for IEEE binary128,
    which is why conversion helpers come in `tf` and `kf` pairs.
- term: ELFv2
  definition: The PowerPC 64-bit ELF ABI used by little-endian Linux distributions,
    superseding the older ELFv1. Among other differences it allows larger values to
    be passed in registers before falling back to memory.
- term: optab
  definition: GCC's table mapping an operation and mode combination to either an instruction
    pattern or a library function name. Setting a libfunc on an optab is how a backend
    tells the compiler which runtime routine to call when no instruction exists.
- term: libgcc
  definition: The low-level support library GCC links into every program, holding
    routines the compiler emits calls to when hardware lacks the operation — soft-float
    arithmetic, wide-integer helpers, unwinding.
landing_slug: 2026-09-11-rs6000-83998f47
url: https://github.com/gcc-mirror/gcc/commit/83998f47450c088493c971d46ae3b6dadb7242b3
week_start: '2026-09-07'
week_end: '2026-09-13'
commit_date: '2026-09-11'
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

Summary unavailable — see source link.
