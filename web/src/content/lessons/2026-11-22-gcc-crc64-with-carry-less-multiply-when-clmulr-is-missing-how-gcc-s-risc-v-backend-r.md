---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- crc
- carry-less-multiply
- zbkc
- backend-expansion
lesson_id: gcc:2026-W47
commit_hash: 2d5b266733b5bd4157a4be05868ce1f070458e20
source_type: github
headline: 'CRC64 with carry-less multiply when clmulr is missing: how GCC''s RISC-V
  backend rebuilds the full-width step from clmulh and an XOR'
hook: The x^64 term of a CRC64 polynomial doesn't fit in a 64-bit register. Here is
  how GCC's RISC-V backend handles that bit when the ISA lacks the instruction meant
  for it.
tldr: On RV64 with Zbkc, GCC now computes 32- and 64-bit CRC64 updates with clmul
  and clmulh, and uses one XOR to restore the polynomial bit that clmulr would have
  h…
concept: A reflected CRC update is two carry-less multiplies, one by a precomputed
  quotient and one by the polynomial. If a register can't hold the 65-bit polynomial,
  a missing top bit contributes exactly the multiplicand to the high half, so one
  XOR restores it.
prerequisites:
- what a CRC computes and what a generator polynomial is
- bitwise XOR as addition without carries
- RISC-V base ISA and the idea of optional ISA extensions
- roughly how GCC lowers builtins to RTL through named patterns
code_tour:
- path: gcc/config/riscv/bitmanip.md
  symbol: crc_rev<ANYI1:mode><ANYI:mode>4
  lines: 1468-1498
  why: The expander that chooses between the clmul sequence and the table loop, including
    the new clause for Zbkc, a DImode CRC and SImode-or-wider data.
- path: gcc/config/riscv/bitmanip.md
  symbol: riscv_clmul_<mode>
  lines: 1440-1466
  why: The insn conditions showing that clmul and clmulh exist under Zbkc or Zbc while
    clmulr is Zbc-only, which is why the fix-up is needed.
- path: gcc/config/riscv/riscv.cc
  symbol: expand_reversed_crc_using_clmul
  lines: 16200-16220
  why: Compile-time quotient computation, where the implicit x^64 bit of CRC64 is
    reappended at the lsb after reflection.
- path: gcc/config/riscv/riscv.cc
  symbol: expand_reversed_crc_using_clmul
  lines: 16221-16277
  why: 'The emitted sequence: the polynomial shifted by one, the new TARGET_ZBC requirement
    on use_clmulr, and the clmulh-plus-XOR branch for odd polynomials.'
- path: gcc/config/riscv/riscv.cc
  symbol: riscv_optab_supported_p
  lines: 13722-13737
  why: The separate size-optimization gate that still keeps full-width Zbkc CRCs on
    the table loop when not optimizing for speed.
takeaways:
- A reflected CRC update is a multiply by a precomputed quotient followed by a multiply
  by the polynomial, and carry-less multiply does both in a few instructions instead
  of one table lookup per byte.
- 'If a constant loses its top bit to register width, distributivity over XOR tells
  you the missing piece: for a bit worth 2^XLEN, the high half gains exactly the multiplicand.'
- An ISA extension that lacks one instruction from a generic sequence doesn't always
  mean you must fall back. Check whether the missing instruction can be rebuilt from
  the ones that are present.
- 'Faster instructions don''t help on every input: building constants costs cycles
  and bytes, so clmul pays off only when one update replaces enough table lookups.'
- In GCC backends, TARGET_OPTAB_SUPPORTED_P and the define_expand condition are two
  separate gates. Size and speed builds can reach different expansions.
further_reading:
- title: 'GCC commit 2d5b266: RISC-V: Use Zbkc for wide CRC64 updates on RV64'
  url: https://github.com/gcc-mirror/gcc/commit/2d5b266733b5bd4157a4be05868ce1f070458e20
primer_expert: This is the RISC-V lowering of IFN_CRC_REV via the crc_rev<ANYI1><ANYI>4
  define_expand in bitmanip.md, which dispatches to expand_reversed_crc_using_clmul
  or expand_reversed_crc_table_based in riscv.cc. The quotient comes from gf2n_poly_long_div_quotient
  (expr.cc, shared with aarch64/i386). Zbkc omits clmulr, so full-width CRC64 now
  uses clmulh on (ref_poly<<1), XORing a0 back in when the polynomial is odd. TARGET_OPTAB_SUPPORTED_P
  separately keeps size-optimized builds on the table.
primer_glossary:
- term: carry-less multiplication
  definition: 'Multiplication of two bit strings treated as polynomials over GF(2):
    partial products are combined with XOR instead of addition, so no carries propagate.
    It is the core operation in CRC and GCM-style hashing.'
- term: GF(2)
  definition: The two-element field {0,1}, where addition is XOR and multiplication
    is AND. Polynomials with GF(2) coefficients are the algebra behind CRCs.
- term: reflected CRC
  definition: A CRC variant that processes the least significant bit of each input
    byte first, so the polynomial and register contents are bit-reversed compared
    with the textbook form. Most deployed CRC32 and CRC64 standards are reflected.
- term: generator polynomial
  definition: The fixed polynomial that defines a CRC. An n-bit CRC uses a degree-n
    polynomial with n+1 coefficients, so the leading x^n term is usually left implicit
    when stored.
- term: Zbc
  definition: The RISC-V scalar carry-less multiplication extension. It provides clmul,
    clmulh and clmulr.
- term: Zbkc
  definition: The RISC-V cryptography-oriented carry-less multiply extension. It provides
    only clmul and clmulh, without clmulr.
- term: clmul
  definition: RISC-V instruction returning the low XLEN bits of the carry-less product
    of two registers.
- term: clmulh
  definition: RISC-V instruction returning the high XLEN bits of the 2·XLEN-bit carry-less
    product of two registers.
- term: clmulr
  definition: Zbc-only RISC-V instruction returning a bit slice of the carry-less
    product, offset by one bit from clmulh. It suits reflected arithmetic and lets
    a full-width polynomial be used without shifting.
- term: XLEN
  definition: 'The RISC-V integer register width in bits: 32 on RV32, 64 on RV64.'
landing_slug: 2026-11-20-risc-v-2d5b2667
url: https://github.com/gcc-mirror/gcc/commit/2d5b266733b5bd4157a4be05868ce1f070458e20
week_start: '2026-11-16'
week_end: '2026-11-22'
commit_date: '2026-11-20'
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

## Background: CRC builtins and where the RISC-V backend gets them

GCC exposes CRC computation as builtins such as `__builtin_rev_crc64_data32 (crc, data, POLY)`. The `rev` stands for *reversed*, also called reflected: the bit order used by most real CRC64 and CRC32 protocols, where the least significant bit of each byte is processed first. Each builtin call folds one chunk of data (8, 16, 32 or 64 bits) into a running CRC.

On RISC-V the builtin reaches the backend through one named pattern in `gcc/config/riscv/bitmanip.md`, the `crc_rev<ANYI1:mode><ANYI:mode>4` define_expand. Its operands are the result, the initial CRC (mode `ANYI`), the data (mode `ANYI1`), and the polynomial as a `const_int` with *the leading 1 omitted*. The pattern's condition, `"<ANYI:MODE>mode >= <ANYI1:MODE>mode"`, rejects data wider than the CRC.

The expander can produce two very different code shapes. `expand_reversed_crc_table_based` emits the classic byte-at-a-time loop, with one lookup into a 256-entry table per input byte. `expand_reversed_crc_using_clmul` emits a short straight-line sequence built on *carry-less multiplication*, which RISC-V provides through two scalar extensions:

- **Zbc** provides `clmul`, `clmulh` and `clmulr`.
- **Zbkc**, the cryptography subset, provides only `clmul` and `clmulh`.

The patterns in `bitmanip.md` reflect that split. `riscv_clmul_<mode>` and `riscv_clmulh_<mode>` are enabled under `"TARGET_ZBKC || TARGET_ZBC"`, and `riscv_clmulr_<mode>` only under `"TARGET_ZBC"`. The whole commit is about the missing `clmulr`.

## The mechanism: two carry-less multiplies replace the table

A carry-less multiply is a polynomial multiply over GF(2): partial products combine with XOR, so no carries propagate. Multiplying two XLEN-bit values gives a product up to 2·XLEN bits wide. `clmul` returns the low XLEN bits, `clmulh` the high XLEN bits, and `clmulr` a bit-reversed-friendly middle slice suited to reflected arithmetic.

`expand_reversed_crc_using_clmul` first does its arithmetic at compile time. It computes the quotient `q` of polynomial long division over GF(2) with `gf2n_poly_long_div_quotient`, then reflects it to match the reversed bit order. CRC64 needs special care, because the generator polynomial has 65 bits and its x^64 term can't fit in a 64-bit `HOST_WIDE_INT`:

```c
if (crc_size == 64)
  {
    /* Calculate the quotient.
       x^64 is left implicit at the msb to fit in 64 bits.  */
    q = gf2n_poly_long_div_quotient (UINTVAL (polynomial), crc_size);
    /* Reflect the calculated quotient.
       Implicit bit is now missing at the lsb.  */
    q = reflect_hwi (q, crc_size);
    /* Add the implicit bit back at the lsb.
       This is okay because the extra bit falls outside the 64 lsbs output
       by clmul.  */
    q = (q << 1) | 1;
  }
```

The polynomial is then reflected with `reflect_hwi` and loaded into `t1`. The emitted sequence has these steps:

1. `a0 = crc ^ data`, with both zero-extended to `word_mode` when narrower.
2. `a0 = clmul (a0, q)` keeps the low half of the product with the quotient.
3. `a0 <<= BITS_PER_WORD - data_size` moves the data bits to the top of the word.
4. Multiply by the polynomial and keep the high part.

Step 4 is where the extensions differ. With Zbc and a full-width CRC, `clmulr` does it in one instruction with `t1 = ref_polynomial`. Without `clmulr`, the code loads `t1 = ref_polynomial << 1` and uses `clmulh`, because `clmulh` returns the upper XLEN bits and the constant has to be shifted one place to line the result up. For CRCs narrower than a word this costs nothing, since the shifted constant still fits. For a 64-bit CRC it does not fit.

## The change: rebuilding the lost bit with one XOR

Before this commit, the full-width case required `clmulr` outright:

```c
bool use_clmulr = crc_size == BITS_PER_WORD;
gcc_assert (TARGET_ZBC || !use_clmulr);
```

The expander made sure that path was never reached on a Zbkc-only target, so CRC64 on RV64 with Zbkc always fell back to the table loop. The commit turns the assertion into a fallback:

```c
bool use_clmulr = crc_size == BITS_PER_WORD && TARGET_ZBC;
```

A 64-bit CRC on a Zbkc-only target now takes the `clmulh` route with `t1 = ref_polynomial << 1`. In 64 bits, that shift discards the top bit of the reflected polynomial. The code tests `UINTVAL (polynomial) & 1`, the low bit of the unreflected polynomial. Reflection moves that bit to the top, so this is the bit the shift loses. When the bit is set, the commit adds a branch:

```c
else if (crc_mode == DImode && (UINTVAL (polynomial) & 1))
  {
    /* The left shift of the reflected polynomial discarded its top
       bit.  XOR the multiplicand back into the high product.  */
    rtx high = gen_reg_rtx (DImode);
    emit_insn (gen_riscv_clmulh_di (high, a0, t1));
    riscv_expand_op (XOR, DImode, a0, high, a0);
  }
```

The algebra is short. The constant you want is the 65-bit value `2^64 + t1`, but the register holds only `t1`. Carry-less multiplication distributes over XOR, so `a0 · (2^64 ⊕ t1) = (a0 · 2^64) ⊕ (a0 · t1)`. The term `a0 · 2^64` is `a0` shifted up exactly one word, so its high half is `a0` and its low half is zero. The high half of the full product is therefore `clmulh (a0, t1) ⊕ a0`, which is what the branch emits. One extra XOR does the job of the instruction Zbkc lacks.

The expander gate in `bitmanip.md` gains a third clause that sends these cases to the clmul expansion:

```c
|| (TARGET_ZBKC && <ANYI:MODE>mode == DImode
    && <ANYI1:MODE>mode >= SImode))
```

That clause covers a 64-bit CRC with 32- or 64-bit data. 8- and 16-bit data still use the table.

## The consequences: a deliberate cutoff, and a size gate that still applies

The width cutoff is a cost decision based on measurement. The two multiplies need two 64-bit constants, `q` and `t1`, and on RV64 each takes several instructions to build. A 32-bit update replaces four byte table lookups and a 64-bit update replaces eight. An 8-bit update replaces only one, which doesn't pay for the constants. The author's measurements on a SpacemiT K1 and in gem5, using `-O2 -march=rv64gc_zbkc` over a warm 4 KiB buffer, show:

- 8-bit inputs got slower everywhere (+20% to +62% cycles).
- 16-bit inputs were faster when inlined, but +22.3% on K1 when each update was a separate call, because the constants are rebuilt on every call.
- 32-bit inputs took 33% to 69% fewer cycles, and 64-bit inputs 70% to 88% fewer, across K1 and both gem5 models.

These are the author's figures. They explain why the gate stops at `SImode`.

For code optimized for size, `riscv_optab_supported_p` sets a separate gate. When `opt_type != OPTIMIZE_FOR_SPEED`, it reports `crc_rev_optab` as supported only for CRCs narrower than a word, or for word-sized CRCs with Zbc. That logic did not change. Only its comment did, and it now says that "materializing the constants for clmul can take more space than the original loop." When optimizing for speed it returns `true`, and the expander's own condition, including the new Zbkc clause, makes the choice.

In practice:

- On RV64 with Zbkc but not Zbc, speed-optimized 32- and 64-bit CRC64 updates now compile to a `clmul`/`clmulh` sequence instead of a table loop.
- Byte-wise and halfword-wise CRC64 updates on those cores still use the table.
- Whether the extra XOR appears depends on the low bit of the polynomial constant. Common CRC64 polynomials are odd because a generator polynomial normally has a constant term, so expect to see it.

## See it yourself

The new test `gcc.target/riscv/crc-rev-zbkc.c` shows the behaviour directly. It defines four CRC64 functions with the macro `CRC64 (BITS, TYPE, POLY)`, each wrapping `__builtin_rev_crc64_data##BITS`. Compile it with:

```sh
riscv64-unknown-elf-gcc -O2 -march=rv64gc_zbkc -mabi=lp64 -S crc-rev-zbkc.c
```

The 8- and 16-bit functions compile to table code. The 32-bit function uses `POLY = 0x42f0e1eba9ea3693UL`, which is odd, so it gets the `clmulh` plus XOR fix-up. The 64-bit function deliberately uses `POLY - 1`, which is even, so it covers the plain `clmulh` path with no XOR. The test's directives expect exactly two of each instruction:

```c
/* { dg-final { scan-assembler-times {\mclmul\M} 2 } } */
/* { dg-final { scan-assembler-times {\mclmulh\M} 2 } } */
```

This is a compile-only test (`dg-do compile`). It counts instructions but never runs them, so it doesn't check that the CRC values are correct. If you change this code, check the result against a reference CRC64 under a simulator or on hardware. Rebuilding with `-march=rv64gc_zbc` is also useful: there you should see `clmulr` and no `clmulh` for the full-width steps.
