---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- builtins
- internal-functions
- optabs
- x86-pclmul
- _BitInt
lesson_id: gcc:2026-W45
commit_hash: 58f804554996fe057e5ca4fc814449640a6e816c
source_type: github
headline: 'Carry-less multiplication in GCC: how one builtin goes from keyword to
  internal function to optab to pclmulqdq'
hook: CRCs, GHASH and Reed-Solomon all depend on a multiply that XORs where ordinary
  multiplication adds. GCC now has a builtin for it, and how GCC lowers that builtin
  is a tour of the middle end.
tldr: __builtin_clmulg becomes IFN_CLMUL or IFN_CLMUL_WIDEN. GCC folds it at compile
  time, uses a target optab such as x86 pclmulqdq where one exists, and otherwise…
concept: GCC carries an operation the source can't spell portably as an internal function.
  Constant folding, _BitInt lowering and RTL expansion each handle it in their own
  way. Expansion tries target optabs first and then a generic software sequence, so
  hardware support is opt-in per target.
prerequisites:
- binary polynomial / XOR arithmetic basics
- GCC's split into front end, GIMPLE middle end and RTL backend
- what a compiler builtin is
- rough idea of SIMD registers on x86
code_tour:
- path: gcc/builtins.cc
  symbol: fold_build_builtin_clmulg
  lines: 10738-10782
  why: 'Front-end folding: constants go through wi::clmul, and everything else becomes
    IFN_CLMUL or a save_expr''d IFN_CLMUL_WIDEN split with REALPART_EXPR/IMAGPART_EXPR.'
- path: gcc/c/c-parser.cc
  symbol: c_parser_postfix_expression
  lines: 13560-13600
  why: Shows the RID_BUILTIN_CLMULG keyword sharing a case with bswapg/bitreverseg
    and accepting 2 or 3 arguments.
- path: gcc/internal-fn.cc
  symbol: expand_clmul
  lines: 6026-6113
  why: The expansion order (0/1 shortcut, clmul_optab, clmul_widen_optab) and the
    documented Kronecker substitution fallback with its choice of S.
- path: gcc/internal-fn.cc
  symbol: expand_CLMUL_WIDEN
  lines: 6190-6240
  why: How get_min_precision drives path selection and how results are masked to the
    source type's precision.
- path: gcc/config/i386/sse.md
  symbol: clmul_widendi3
  lines: 28882-28923
  why: The x86 expanders that put DI operands into V2DI lanes, run pclmulqdq, and
    extract lane 0 and lane 1 as the low and high halves.
- path: gcc/gimple-lower-bitint.cc
  symbol: bitint_large_huge::lower_clmul
  lines: 6309-6360
  why: Limb-by-limb shift-and-XOR lowering for large _BitInt, with the sparser operand
    swapped in to drive the loop.
takeaways:
- When source code can't spell an operation portably, GCC gives it an internal function,
  and folding, lowering and expansion each handle it separately.
- 'Optabs separate ''what'' from ''how'': a backend adds one named pattern (clmuldi3)
  and the generic expander finds it automatically.'
- Returning two results as a COMPLEX_TYPE, as IFN_MUL_OVERFLOW and IFN_CLMUL_WIDEN
  do, lets one call produce a low and a high half.
- Kronecker substitution computes the carry-less product with ordinary integer multiplies
  by spacing bits far enough apart that carries can't reach the bits that are kept.
- Value-range facts such as get_min_precision and get_nonzero_bits feed directly into
  instruction selection, so masking your inputs can make the generated code cheaper.
further_reading:
- title: 'P3642R7: std::clmul and std::widening_clmul'
  url: https://wg21.link/P3642R7
- title: 'The commit: Introduce __builtin_clmulg builtin [PR128111]'
  url: https://github.com/gcc-mirror/gcc/commit/58f804554996fe057e5ca4fc814449640a6e816c
primer_expert: '`__builtin_clmulg` is a keyword builtin (RID_BUILTIN_CLMULG), not
  a DEF_BUILTIN. `fold_build_builtin_clmulg` lowers it straight to IFN_CLMUL, or to
  IFN_CLMUL_WIDEN with a complex result in the IFN_MUL_OVERFLOW style, so no BUILT_IN_*
  code exists for passes to match on. Expansion uses new clmul/clmul_widen optabs,
  and only i386 implements them (via pclmulqdq). Other targets get the Kronecker fallback.
  Large _BitInt is lowered earlier, in gimple-lower-bitint.cc, and never reaches the
  optab path.'
primer_glossary:
- term: carry-less multiplication
  definition: 'Multiplication of bit strings treated as polynomials over GF(2): partial
    products are combined with XOR instead of addition, so no carries propagate. It
    underlies CRCs, GHASH and many error-correcting codes.'
- term: type-generic builtin
  definition: A compiler builtin whose argument and result types are taken from the
    call site instead of a fixed prototype, like the GCC builtins ending in 'g' (__builtin_popcountg,
    __builtin_bswapg).
- term: internal function (IFN)
  definition: An operation the GCC middle end represents as a special call (IFN_*)
    with no user-visible symbol. It stays opaque through GIMPLE optimisation and is
    expanded to RTL by a dedicated expand_* routine.
- term: optab
  definition: GCC's table mapping an abstract operation and a machine mode to a backend
    instruction pattern. The middle end queries it with optab_handler, and CODE_FOR_nothing
    means the target has no pattern.
- term: machine mode
  definition: GCC's name for a hardware-level data size and kind, such as DImode (64-bit
    integer) or V2DImode (vector of two 64-bit integers). RTL operations are typed
    by mode.
- term: define_expand
  definition: A machine-description construct that tells the backend how to emit RTL
    for a named pattern, such as an optab entry, often as a sequence of other instructions.
- term: RTL
  definition: Register Transfer Language, GCC's low-level intermediate representation
    used after GIMPLE for instruction selection, register allocation and scheduling.
- term: GIMPLE
  definition: GCC's three-address, SSA-based middle-end IR, where most target-independent
    optimisation happens.
- term: 'wide_int / wi::'
  definition: GCC's arbitrary-precision integer class and helper namespace, used to
    evaluate integer operations on constants at compile time at any precision.
- term: INTEGER_CST
  definition: The tree node GCC uses for an integer constant in the front end and
    middle end.
landing_slug: 2026-11-07-middle-end-58f80455
url: https://github.com/gcc-mirror/gcc/commit/58f804554996fe057e5ca4fc814449640a6e816c
week_start: '2026-11-02'
week_end: '2026-11-08'
commit_date: '2026-11-07'
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

## A multiply without carries, and why the compiler has to own it

Carry-less multiplication treats each unsigned integer as a polynomial over GF(2): bit *i* is the coefficient of x^i. You multiply the way you would on paper, except that partial products are combined with XOR instead of addition, so nothing carries into the next column. The commit message gives the reference definition:

```c
T clmul_naive (T x, T y) {
  T r = 0;
  for (int i = 0; i < __builtin_popcountg ((T) ~(T) 0); ++i)
    if ((unsigned) (y >> i) & 1)
      r ^= x << i;
  return r;
}
```

This operation sits at the core of CRC computation, GCM/GHASH authentication and BCH/Reed-Solomon codes. Many ISAs implement some size of it in hardware. The commit lists x86 `pclmulqdq` (64x64->128), assorted arm/aarch64 `vmul*`/`pmul*` forms, powerpc `vpsum*`, riscv `clmul`/`clmulh`, sparc `xmulx`, and s390x `vgfm`. Until now a C or C++ programmer had two options: a portable loop the compiler could not recognise reliably, or a target intrinsic like `_mm_clmulepi64_si128` that ties the code to x86.

Jakub Jelinek's commit argues that pattern-matching the many possible hand-written loops is "of limited use". It also points to wg21 paper P3642R7, which proposes `std::clmul` and `std::widening_clmul` for C++. Both are reasons to give the operation a name inside the compiler. The new builtin is `__builtin_clmulg`, and its two shapes are described as if they were templates:

```c++
template <__unsigned_integer T> T __builtin_clmulg (T, T);
template <__unsigned_integer T> T __builtin_clmulg (T, T, T *);
```

The two-argument form returns the low `__builtin_popcountg ((T) ~(T) 0)` bits of the product. The three-argument form returns those same low bits and also stores the high half through the pointer, the same shape as `__builtin_mul_overflow`. The commit explains why it avoids a builtin that returns a type twice as wide: such a type doesn't always exist. A 32-bit target without `_BitInt` has nothing wider than `unsigned long long`, and a 64-bit target without `_BitInt` has nothing wider than `unsigned __int128`. Returning the high half through a pointer of the same type works on every target.

## From keyword to internal function

The front end handles the builtin as a keyword, `RID_BUILTIN_CLMULG`. It doesn't go through an ordinary library-style declaration. In `c_parser_postfix_expression` it shares a case with the other type-generic bit builtins, and the argument-count check differs only for clmul:

```c
case RID_BUILTIN_CLMULG:
  ifn = IFN_CLMUL;
  name = "__builtin_clmulg";
  break;
...
if (nargs < (ifn == IFN_CLMUL ? 2 : 1)
    || nargs > (ifn == IFN_CLMUL ? 3 : 1))
  error_at (loc, "wrong number of arguments to %qs", name);
```

The parsed call then goes to `fold_build_builtin_clmulg` in `gcc/builtins.cc`. If both operands are `INTEGER_CST` and neither has `TREE_OVERFLOW` set, it computes the answer at compile time with `wi::clmul`, at precision `prec` for the two-argument form or `prec * 2` for the three-argument form. In the widening case it splits the result with `wide_int::from` and `wi::rshift`, then builds a `COMPOUND_EXPR` that first stores the high half through `arg3` and then yields the low half.

For non-constant operands the builtin becomes one of two new internal functions. `IFN_CLMUL` returns just the low bits. `IFN_CLMUL_WIDEN` follows the convention of `IFN_MUL_OVERFLOW`: it returns a `COMPLEX_TYPE` whose real part is the low half and whose imaginary part is the high half. The excerpt has one detail worth studying:

```c
TREE_SIDE_EFFECTS (call) = 1;
tree tgt = save_expr (call);
tree intres = build1_loc (loc, REALPART_EXPR, type, tgt);
tree ovfres = build1_loc (loc, IMAGPART_EXPR, type, tgt);
```

The call itself is const. The comment explains that without the forced side-effect flag, `save_expr` could treat it as invariant and evaluate it more than once, leaving later passes to CSE the duplicates. Forcing `TREE_SIDE_EFFECTS` guarantees one call, with the real and imaginary parts read from the same saved value. A complex return type is how GCC lets a single internal call produce two results without a memory round-trip.

## The expansion ladder: optab, widening optab, then Kronecker

Internal functions stay opaque through GIMPLE and only turn into RTL at expansion. `expand_CLMUL` in `gcc/internal-fn.cc` first calls `get_min_precision` on each operand, which gives the number of bits that can actually be nonzero, and then passes everything to `expand_clmul`. That function works down a fixed sequence:

1. If either operand is known to fit in one bit (`MIN (prec0, prec1) == 1`), the product reduces to an ordinary multiply, or to an AND when both precisions are 1.
2. Using `FOR_EACH_MODE_IN_CLASS (cmode, MODE_INT)`, it walks the integer modes. For each mode wide enough to hold both operands, it tries `clmul_optab` if the true product width `prec0 + prec1 - 1`, or the requested result width, fits.
3. Failing that, it tries `clmul_widen_optab` in the same mode. That optab produces `reslo` and `reshi` as two outputs, which the code shifts and IORs together in the 2x-wider mode when the caller needs the full product.
4. If no target pattern applies, it uses Kronecker substitution.

Kronecker substitution computes the carry-less product with ordinary integer multiplies. Each operand is split into S copies, each masked to every S-th bit. For S = 4 those masks are `0x1111...`, `0x2222...`, `0x4444...` and `0x8888...`. In each masked copy the set bits are at least S apart, so when two copies are multiplied normally the carries cannot pass the gaps into a bit position the code keeps. XOR the right S of the S\*S partial products together, mask each accumulator back to its residue class, OR the classes, and you have the carry-less result. The excerpt shows the S = 4 case written out in full. The code picks the smallest S in [2, 13] that satisfies `MIN (prec0, prec1) <= S * ((1 << S) - 1)`, or `prec <= S * (1 << S)`, or `prec0 + prec1 - 1 <= S * (1 << S)`. That costs S\*S multiplications, 3\*S ANDs, S\*(S-1) XORs and S-1 IORs.

`get_min_precision` matters at every step. If value-range information shows that an operand has few active bits, the code may choose a narrower hardware mode, take the early `prec0 + prec1 - 1 <= prec` shortcut in `expand_CLMUL_WIDEN` (which writes zero as the high half), or use a smaller S. When the source type is narrower than its machine mode, as with a `_BitInt` that is not mode-sized, both expanders AND the result with `wi::mask` so stray high bits never leak out.

## The x86 piece and the _BitInt piece

The only target this commit wires up is x86, through two expanders in `gcc/config/i386/sse.md` guarded by `TARGET_PCLMUL`. Their names follow the optab naming convention, so the generic code above finds them automatically. `clmuldi3` puts each 64-bit operand into lane 0 of a `V2DImode` register with a zero in lane 1, emits `pclmulqdq` with immediate 0, and extracts lane 0 of the 128-bit result with a `VEC_SELECT`. `clmul_widendi3` does the same and also extracts lane 1 into a second output, which supplies both halves of the 64x64->128 product.

That small amount of code works because the optab layer separates the two sides. The middle end only asks whether `optab_handler (clmul_widen_optab, DImode)` has a pattern. The backend only has to describe how to compute the operation. Every other target listed in the commit message can add its own `clmul<mode>3`/`clmul_widen<mode>3` patterns later without touching `internal-fn.cc`. The author says he defers those to the target maintainers.

Large and huge `_BitInt` types go a different way. `gimple-lower-bitint.cc` breaks them into limb arithmetic before RTL expansion, so `bitint_large_huge::lower_clmul` emits a limb loop that implements an optimised version of the naive algorithm. It first swaps the operands so that the one with fewer possibly-set bits (`wi::popcount (get_nonzero_bits (...))`) drives the bit loop. For each set bit it XORs a shifted copy of the other operand into the result limbs, and the complementary right shift `>> k` carries bits across limb boundaries. The commit message reports that on x86_64 this optimised naive loop consistently beat Kronecker substitution when no matching hardware multiply exists, and produced the smallest code.

## What to expect if you write or read code that uses it

- **Portable source, per-target code quality.** `__builtin_clmulg (a, b, &hi)` on `unsigned long long` should compile to `pclmulqdq` plus lane moves on x86 when PCLMUL is enabled. On a target without these optabs, including every non-x86 target at this commit, you get the Kronecker sequence of ordinary multiplies. It is correct but not a single instruction.
- **Constants fold.** `fold_build_builtin_clmulg` folds constant operands with `wi::clmul`, and the research notes say `fold-const.cc` and `fold-const-call.cc` gained `CFN_CLMUL`/`CFN_CLMUL_WIDEN` cases that call the same routine, so the compile-time and runtime results agree. Lookup tables such as CRC tables computed through the builtin can fold away when their inputs are constant.
- **One type for everything.** Both operands and the pointed-to high half must have the same unsigned type. This is stricter than `__builtin_mul_overflow`, and the restriction is deliberate.
- **Value ranges help.** Operands masked or zero-extended from narrower types reach `expand_clmul` with a smaller `get_min_precision`. That can enable a narrower hardware path or a cheaper Kronecker spacing, and in the widening case it can prove that the high half is zero.
- **Not clang's spelling.** Clang provides `__builtin_elementwise_clmul`, which covers only the non-widening `T = clmul (T, T)` form for scalars and vectors. The commit notes that GCC has no `__builtin_elementwise_*` family yet and could add the clang spelling later.

## Seeing it yourself

Write a small function such as

```c
unsigned long long f (unsigned long long a, unsigned long long b,
                      unsigned long long *hi)
{ return __builtin_clmulg (a, b, hi); }
```

and compile it with `-O2 -fdump-tree-optimized`. The GIMPLE dump should show the internal call in the `.CLMUL` style used in `gimple-lower-bitint.cc`'s comments (here `.CLMUL_WIDEN`), followed by `REALPART_EXPR`/`IMAGPART_EXPR` reads. Compile it again for x86-64 with PCLMUL enabled and look for `pclmulqdq` in the assembly. Without PCLMUL, look instead for a run of masks, `imul`s and XORs: that is the Kronecker fallback.

Pass constant arguments and you should see the whole call fold to a constant, plus a store of the high half for the three-argument form. Try `unsigned _BitInt(N)` with N beyond the machine word size to exercise the limb loop from `lower_clmul`.

The commit adds `gcc/testsuite/c-c++-common/builtin-clmulg-1.c`, `builtin-clmulg-2.c`, `g++.dg/ext/builtin-clmulg-1.C` and `gcc.target/i386/pclmul-builtin-clmulg-1.c`. They are good starting points for the expected behaviour on each path.
