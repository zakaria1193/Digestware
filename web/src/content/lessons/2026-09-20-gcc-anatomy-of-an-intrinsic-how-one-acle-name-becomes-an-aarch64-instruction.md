---
project: gcc
subsystem: gcc/aarch64
patch_id: null
tags:
- aarch64
- sme
- intrinsics
- machine-description
- unspec
lesson_id: gcc:2026-W38
commit_hash: b610d8cfc8d19c6a156afb26663c2e590f4f1a31
source_type: github
headline: 'Anatomy of an Intrinsic: How One ACLE Name Becomes an AArch64 Instruction'
hook: Every `sv*` name you call is stitched together from four separate tables inside
  GCC. A new SME2.1 outer-product family shows exactly where each seam is — and why
  one table alone is never enough.
tldr: GCC's AArch64 SVE/SME intrinsics are built from a .def table, a shape, an impl
  class and an .md pattern; svtmopa_lane shows all four seams at once.
concept: 'A target intrinsic is not one thing: it is a name in a .def table, a shape
  that type-checks the call, an impl class that picks an UNSPEC, and a machine-description
  pattern. Adding one means completing that whole chain.'
prerequisites:
- what an RTL instruction pattern is
- roughly what a GCC machine description (.md) file contains
- how C intrinsics differ from inline asm
- basic idea of an ISA feature flag (-march=+ext)
code_tour:
- path: gcc/config/aarch64/aarch64-sve-builtins-sme.def
  symbol: svtmopa_lane
  lines: 382-404
  why: 'The declaration table: five type arrays, each wrapped in its own REQUIRED_EXTENSIONS
    block, showing how per-type feature gating is expressed.'
- path: gcc/config/aarch64/aarch64-sve-builtins-sme.def
  symbol: DEF_SME_ZA_FUNCTION_GS
  lines: 130-152
  why: Existing svmla/svdot_lane entries that establish the five-argument convention
    the new svtmopa_lane lines follow.
- path: gcc/config/aarch64/aarch64-sve-builtins-sme.cc
  symbol: svtmopa_lane_za_impl
  lines: 464-497
  why: 'The impl class: unspec_for collapses thirteen typed names onto six UNSPECs,
    and expand turns modes plus UNSPEC into a concrete insn_code.'
- path: gcc/config/aarch64/aarch64-sve-builtins-sme.cc
  symbol: svtmopa_lane_za
  lines: '719'
  why: The FUNCTION line binding the intrinsic name to its implementation class, surrounded
    by the existing SME entries for comparison.
- path: gcc/config/aarch64/iterators.md
  symbol: define_int_attr
  lines: 5500-5653
  why: The int-attribute region where the new UNSPECs get their optab names, alongside
    existing SME examples like hv and has_16bit_form.
takeaways:
- 'An intrinsic in GCC''s AArch64 backend is four artefacts: a .def row, a shape,
  an impl class, and an .md pattern.'
- Put argument-range and immediate checks in the shape so mistakes become diagnostics,
  not bad encodings.
- Fan many typed names into few UNSPECs in C++ rather than writing one machine-description
  pattern per type.
- Feature gating belongs on the declaration (REQUIRED_EXTENSIONS, streaming_only),
  so availability is a compile-time property.
- A feature-test macro deserves a test asserting it is absent by default — silently-defined
  predefines break portable code.
further_reading:
- title: 'aarch64: Add SME2.1 structured sparsity outer product intrinsics (commit
    b610d8cfc8d1)'
  url: https://github.com/gcc-mirror/gcc/commit/b610d8cfc8d19c6a156afb26663c2e590f4f1a31
primer_expert: 'The SVE/SME builtin layer is table-driven rather than pattern-driven:
  `aarch64-sve-builtins-sme.def` rows expand across type and group suffixes, shapes
  in `aarch64-sve-builtins-shapes.cc` own argument grammar and immediate ranges, and
  impl classes in `aarch64-sve-builtins-sme.cc` map resolved suffixes to UNSPECs before
  `code_for_aarch64_sme_lane` resolves an `@`-named `define_insn`. Non-obvious neighbours:
  `read_write_za` models ZA as explicit state, `streaming_only` couples availability
  to per-function streaming status, and `DEF_SME_ZA_FUNCTION_GS_FPM (..., set)` is
  read back as `instance.fp…'
primer_glossary:
- term: ACLE
  definition: Arm C Language Extensions — Arm's specification of the C-callable intrinsic
    names, types and semantics for extensions such as NEON, SVE and SME. It is what
    makes `svmla_lane_za32_f32_vg1x2` mean the same thing across compilers.
- term: SME
  definition: Arm's Scalable Matrix Extension, an ISA extension providing matrix-oriented
    operations, notably outer products accumulating into a dedicated matrix state.
    SME2 and SME2.1 are successive revisions adding further instruction families.
- term: ZA
  definition: The architectural matrix accumulator state introduced by SME. It is
    not a general-purpose register file; instructions address it as tiles or slices,
    and the compiler must model reads and writes of it explicitly.
- term: ZA tile
  definition: A named subdivision of the ZA state that an instruction selects with
    a small immediate. How many tiles exist depends on element width, so the legal
    immediate range differs between 16-bit and 32-bit element forms.
- term: streaming mode
  definition: An SME processor mode in which the effective vector length and the set
    of legal instructions both change. GCC tracks whether each function runs in streaming
    mode and validates SME intrinsic calls against it.
- term: UNSPEC
  definition: 'GCC''s RTL construct for a machine operation with no portable RTL meaning:
    an opaque expression tagged with an integer constant. Optimisers leave it alone;
    machine-description patterns match on the tag to emit the instruction.'
- term: define_insn
  definition: A machine-description entry pairing an RTL pattern with operand constraints
    and an assembly output template. When its name begins with `@`, GCC generates
    a `code_for_...` lookup function so backend C++ can select it by iterator value.
- term: mode iterator
  definition: A machine-description facility that expands one pattern template over
    a list of machine modes, e.g. `SVE_FULL_HF` or `VNx16QI_ONLY`, so a single `define_insn`
    covers many element widths.
- term: machine mode
  definition: GCC's type tag on an RTL value, encoding size and class — `VNx4SI` is
    a variable-length vector of 32-bit integers, `VNx16QI` of 8-bit ones. Pattern
    selection and register allocation both key off it.
- term: register constraint
  definition: A short string in a machine description restricting which registers
    or operand forms the register allocator may choose for an operand. A new one (here
    `Uwo`) is added when an instruction's legal register set is narrower than any
    existing constraint describes.
landing_slug: 2026-09-14-gcc-aarch64-b610d8cf
url: https://github.com/gcc-mirror/gcc/commit/b610d8cfc8d19c6a156afb26663c2e590f4f1a31
week_start: '2026-09-14'
week_end: '2026-09-20'
commit_date: '2026-09-14'
date: '2026-09-20'
is_stub: false
stub_reason: ''
---

## The background: the AArch64 intrinsic factory

When a vendor adds an ISA extension, the compiler work is rarely a single pattern in a machine description. Arm's ACLE (Arm C Language Extensions) specifies hundreds of C-callable functions per extension, each with a mangled name encoding its element types, its predication, and how many vector registers it consumes. GCC's `aarch64` backend does not hand-write a builtin for each one. It generates them from tables.

The tables live in `gcc/config/aarch64/aarch64-sve-builtins-sme.def` and its siblings. Each line is a macro invocation naming a family, and the macro expansion multiplies that family out across a list of type suffixes and group suffixes. Look at the shape of the existing entries the dossier shows:

```
DEF_SME_ZA_FUNCTION_GS (svmla_lane, binary_za_slice_lane, za_s_float,
			vg1x24, none)
DEF_SME_ZA_FUNCTION_GS (svmla_lane, binary_za_slice_lane, za_s_b_integer,
			vg4, none)
```

Five arguments: the base name (`svmla_lane`), a *shape* (`binary_za_slice_lane`), a *type array* (`za_s_float`), a *group suffix* list (`vg1x24`), and a mode-suffix field. From one such line the builtin machinery emits every legal combination — `svmla_lane_za32_f32_vg1x2`, `svmla_lane_za32_f32_vg1x4`, and so on — each with its own overload entry for C++ resolution and its own expansion path.

This matters to a reader outside the subsystem because it explains why an intrinsic patch touches ten files and none of them look like "the code for the instruction". The instruction is one file. The other nine are the factory that decides which names exist, what argument types they accept, and which of those arguments must be a compile-time constant.

## The mechanism: shape, impl class, UNSPEC, pattern

Follow one call from source to assembly. Four distinct pieces of the backend take turns.

First the **shape**. A shape is a C++ object that knows the argument grammar for a whole family: how many vectors, which ones are immediates, what the return type is, and how to resolve an overloaded call to a specific typed form. Shapes live in `aarch64-sve-builtins-shapes.cc`; the commit adds `ternary_za_uint_dual_single` there. The name is readable once you know the convention: a ternary operation writing into ZA, with unsigned-typed handling, taking dual (paired) and single vector operands. Shapes are also where argument-range checking happens — an immediate that must lie in `[0, 3]` is rejected here, at compile time, with a diagnostic rather than a silently wrong encoding.

Second the **impl class**, in `aarch64-sve-builtins-sme.cc`. This is where a family with many type combinations collapses onto a small set of internal operations. `svtmopa_lane_za_impl` derives from `read_write_za<function_base>` — a base that tells the rest of the compiler this builtin both reads and writes the ZA state, which is not an ordinary register and needs explicit modelling. Its `unspec_for` method reads the resolved type suffixes and picks the operation:

```c++
if (instance.fpm_mode == FPM_set)
  return UNSPEC_SME_FTMOPA_FP8;
const auto &suffix1 = instance.type_suffix (1);
if (!suffix1.integer_p)
  return UNSPEC_SME_FTMOPA;
const auto &suffix2 = instance.type_suffix (2);
if (suffix1.unsigned_p && suffix2.unsigned_p)
  return UNSPEC_SME_UTMOPA;
else if (!suffix1.unsigned_p && !suffix2.unsigned_p)
  return UNSPEC_SME_STMOPA;
else if (suffix1.unsigned_p && !suffix2.unsigned_p)
  return UNSPEC_SME_USTMOPA;
else
  return UNSPEC_SME_SUTMOPA;
```

That cascade is the whole signed/unsigned/mixed matrix in eight lines. Thirteen documented intrinsic names funnel into six `UNSPEC`s. An `UNSPEC` is GCC's escape hatch in RTL: an opaque operation tagged with an integer, which the optimisers will not try to reason about but which instruction patterns can match on. It is how a backend represents "this machine operation has no portable RTL meaning".

Third the **mode selection**, in the same class's `expand`:

```c++
machine_mode za_mode = e.vector_mode (0);
machine_mode v_mode = e.tuple_mode (1);
if (GET_MODE_UNIT_BITSIZE (za_mode) == GET_MODE_UNIT_BITSIZE (v_mode))
  za_mode = v_mode;
insn_code icode
  = code_for_aarch64_sme_lane (unspec_for (e), za_mode, v_mode);
return e.use_exact_insn (icode);
```

`code_for_aarch64_sme_lane` is generated code: for a `define_insn` named with the `@` prefix, GCC emits a lookup function taking the iterator values as arguments. So the `(unspec, za_mode, v_mode)` triple *is* the address of a pattern. The `GET_MODE_UNIT_BITSIZE` normalisation exists because the ZA accumulator's element width and the input vector's element width sometimes agree and sometimes do not; when they agree, one mode is enough to name the pattern.

Fourth the **patterns** in `aarch64-sme.md`. The commit adds five `define_insn`s, and their names show which mode pairs are legal: `@aarch64_sme_lane_<optab><VNx4SI_ONLY:mode><SVE_FULL_BHI:mode>` for 32-bit ZA with byte/halfword integer inputs, `@aarch64_sme_lane_<optab><VNx4SI_ONLY:mode><SVE_FULL_HF:mode>` for half-precision, `@aarch64_sme_lane_<optab><SME_TMOPA_FP8:mode><VNx16QI_ONLY:mode>` for the FP8 forms, and so on. The `<optab>` substitution is driven by the new `optab` entries for the six `UNSPEC`s, which is what makes one pattern template cover signed, unsigned and mixed variants.

## The change: a family, a shape, a constraint, two predicates

The commit adds the `svtmopa_lane` intrinsics for `FEAT_SME_TMOP`, gated behind `+sme-tmop`. The `.def` entries are the clearest statement of what is now callable:

```
#define REQUIRED_EXTENSIONS streaming_only (AARCH64_FL_SME_TMOP)
DEF_SME_ZA_FUNCTION_GS (svtmopa_lane, ternary_za_uint_dual_single, tmop_base, none, none)
#undef REQUIRED_EXTENSIONS
```

Read that block carefully, because three separate policies are encoded in it. `streaming_only` says these functions may only be called from streaming mode — SME's alternate execution mode in which the vector length and the legal instruction set both change. `AARCH64_FL_SME_TMOP` is the feature bit that must be enabled. And `tmop_base` names one of the five new `DEF_SVE_TYPES_ARRAY`s added in `aarch64-acle-builtins.h` (`TYPES_tmop_base`, `TYPES_tmop_h_bfloat`, `TYPES_tmop_h_float`, `TYPES_tmop_h_mf8`, `TYPES_tmop_s_mf8`), each listing the type-suffix triples that expand into concrete names.

The type arrays are split rather than merged precisely so the extension gating can differ per type. Half-precision float needs a second flag; so does bfloat16; the FP8 forms need a third:

```
#define REQUIRED_EXTENSIONS streaming_only (AARCH64_FL_SME_TMOP \
					    | AARCH64_FL_SME_B16B16)
DEF_SME_ZA_FUNCTION_GS (svtmopa_lane, ternary_za_uint_dual_single, tmop_h_bfloat, none, none)
#undef REQUIRED_EXTENSIONS

#define REQUIRED_EXTENSIONS streaming_only (AARCH64_FL_SME_TMOP \
					    | AARCH64_FL_SME_F8F16)
DEF_SME_ZA_FUNCTION_GS_FPM (svtmopa_lane, ternary_za_uint_dual_single, tmop_h_mf8, none, none, set)
#undef REQUIRED_EXTENSIONS
```

Note the different macro on the last line: `DEF_SME_ZA_FUNCTION_GS_FPM`, with a trailing `set`. That is the FPM (floating-point mode register) handling — FP8 arithmetic reads format and rounding configuration from a mode register rather than from the opcode, so those intrinsics must be modelled as depending on it. That `set` is the same signal `unspec_for` tests as `instance.fpm_mode == FPM_set` when it returns `UNSPEC_SME_FTMOPA_FP8`. One declaration flag, read back on the expansion path.

Below the intrinsic layer the commit adds the low-level vocabulary the new patterns need. `constraints.md` gains `Uwo`, a register constraint for the Control Vector Register in TMOP operations — a constraint restricts which registers RA may pick for an operand, and a new one exists because this operand's legal register set is narrower than any existing constraint describes. `predicates.md` gains `aarch64_imm1` and `aarch64_imm4`, which the commit message describes as tightening "the immediates selecting ZA tiles based on tile width": ZA is addressed as tiles, and how many tiles exist depends on element width, so a 16-bit-element form accepts a wider tile index range than a 32-bit-element one. Encoding that in two predicates means an out-of-range tile number is a compile error, not a truncated encoding.

`aarch64-c.cc` gains the `__ARM_FEATURE_SME_TMOP` predefine, `aarch64.h` gains `TARGET_STREAMING_SME_TMOP`, and `iterators.md` gains the `SME_TMOPA_BHSF` and `SME_TMOPA_FP8` mode iterators, the six `UNSPEC`s, the `SME_TMOP_INT` / `SME_TMOP_INT_CROSS` / `SME_TMOP_FP` / `SME_TMOP_FP8` int iterators, and a `za_imm_bits` mode attribute. Each of those is one row in the factory. Remove any one and the chain breaks at a different place.

## The consequences: what to expect outside this corner

If you write AArch64 code, the practical surface is small and sharply bounded. `__ARM_FEATURE_SME_TMOP` is now the portable way to ask whether these intrinsics exist, and the testsuite addition to `pragma_cpp_predefs_6.c` explicitly checks that the predefine is *off* by default and that the feature dependencies hold. Feature-test macros that appear unconditionally are a recurring class of bug; the test exists to stop that.

The `streaming_only` gating is the constraint most likely to surprise someone reading a patch that uses these. A call to `svtmopa_lane_za32[_s8_s8]` from a function that is not `__arm_streaming` is a compile-time error, not a runtime fault. Streaming mode changes the effective vector length and the legal opcode set, so GCC tracks per-function streaming status and validates every SME builtin against it. The same goes for the FP8 forms: they carry an FPM dependency, so the compiler treats the mode register as part of their input, which restricts how freely they can be reordered relative to code that writes it.

If you maintain a different backend, the transferable observation is the layering. Argument grammar and immediate range live in the shape, where errors can be reported against source locations. Type-to-operation mapping lives in the impl class, as ordinary C++ over resolved type suffixes — not as a combinatorial explosion of `.md` patterns. Only the final encoding lives in the machine description, parameterised by iterators so one template serves signed, unsigned and mixed forms. Thirteen names, six `UNSPEC`s, five `define_insn`s: the fan-in is deliberate, and it is what keeps a several-hundred-intrinsic extension tractable.

One honest limit on this reading: the dossier does not include the bodies of the new `define_insn`s, so nothing here describes the assembly text they emit or the operand order in the encoding. The pattern *names* tell you which mode combinations are covered; the output templates would tell you the rest.

## How to see it yourself

The testsuite is the documentation. `gcc/testsuite/lib/target-supports.exp` gains a `check_effective_target` entry for `sme-tmop`, which is the standard mechanism by which DejaGnu decides whether to run a test at all — it compiles a probe snippet and skips the test if the assembler or compiler rejects it. That is why the thirteen new `acle-asm` tests can assert exact assembly without breaking on toolchains that lack the extension.

The tests themselves live under `gcc.target/aarch64/sme2/acle-asm/`, one file per type combination: `tmopa_lane_za32_s8_u8.c`, `tmopa_lane_za16_mf8_mf8.c`, and so on. They are built on a new macro, `TEST_ZA_TMOP`, added to `test_sme2_acle.h`. The `acle-asm` convention is to invoke the intrinsic in a minimal wrapper and then scan the assembly output for the expected instruction with `dg-final` directives — so reading one of these files tells you, per type combination, exactly what the compiler is contracted to emit.

For the error paths, read `gcc.target/aarch64/sve/acle/general-c/ternary_za_uint_dual_single_1.c`. Files under `general-c` test diagnostics rather than codegen: wrong argument counts, out-of-range immediates, mismatched types. If you want to know what the new shape and the new `aarch64_imm1` / `aarch64_imm4` predicates actually reject, that file is the specification.

One small mercy in the commit worth noting for anyone who reads this code later: it also fixes a stale comment on `function_resolver::resolve_to` in `aarch64-acle-builtins.cc`, which described "the type suffixes given by TYPE0 and TYPE1" when the function had grown a third. The new `svtmopa_lane` forms are the ones that need three type suffixes, so the comment and the caller arrived together.
