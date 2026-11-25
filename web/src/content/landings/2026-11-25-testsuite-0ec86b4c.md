---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- aarch64
- hardware
commit_hash: 0ec86b4c9d3b66be6750a3e015c4a6e37890c666
source_type: github
author: Igor Shevlyakov
headline: AArch64 hardware checks for complex, dotprod, and i8mm fixed
tldr: Corrected AArch64 hardware feature checks in the testsuite to accurately verify
  complex, dot product, and i8mm instructions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit addresses issues in AArch64 testsuite hardware checks:
  `check_effective_target_arm_v8_3a_complex_neon_hw` used an incorrect expected value
  for `FCADD` due to an inverted return; `check_effective_target_arm_v8_2a_dotprod_neon_hw`
  and `check_effective_target_arm_v8_2a_i8mm_neon_hw` had incorrect accumulation logic
  for `UDOT`/`USDOT`. The fixes involve adjusting expected values, using zero addends
  for `FCADD` to ensure predictable results across endianness, and modifying accumulation
  to match instruction behavior. Additionally, `pr126592.c` now uses `-save-temps`
  to ensure an assembl…'
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, which includes advanced SIMD (Advanced
    SIMD) and Scalable Vector Extension (SVE) instruction sets that support vector
    processing.
- term: FCADD
  definition: AArch64 Advanced SIMD instruction for fused complex number multiplication
    and addition. It performs operations like (a + ib) * (c + id) + (e + if).
- term: UDOT
  definition: AArch64 Advanced SIMD instruction for unsigned dot product accumulation.
    It computes the dot product of two vectors and accumulates the result into a destination
    vector.
- term: i8mm
  definition: Integer 8-bit Matrix Multiply. Refers to instructions like `UMMLA` (unsigned
    matrix multiply accumulate) on AArch64, which efficiently perform 8-bit integer
    matrix multiplications.
- term: testsuite
  definition: A collection of tests used to verify the correctness and performance
    of the compiler. It includes various test cases, configurations, and expected
    output comparisons.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ec86b4c9d3b66be6750a3e015c4a6e37890c666
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

Several hardware feature checks for AArch64 in the GCC testsuite have been fixed. This includes corrections for `FCADD` (complex multiplication), `UDOT` (dot product), and `USDOT` (integer dot product) instructions, ensuring these tests accurately reflect hardware capabilities and don't lead to unsupported features or false failures.
