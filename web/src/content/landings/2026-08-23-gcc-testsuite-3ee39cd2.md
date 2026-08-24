---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- avx
- avx512
commit_hash: 3ee39cd29ad31d0035e3b1cfb798c058156868cc
source_type: github
author: H.J. Lu
headline: Compile AVX loadu2/storeu2 tests with -mno-avx512f
tldr: Ensures AVX load/store tests don't fail when AVX512 is enabled by default.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The AVX loadu2/storeu2 tests are designed to verify specific AVX behavior.
  When AVX512F is enabled by default on a system, the compiler might generate AVX512
  instructions that are incompatible with the test's expectations, causing scan-assembler
  to fail. Adding -mno-avx512f ensures these AVX-specific tests run in an environment
  where only AVX features are considered.
primer_glossary:
- term: AVX
  definition: Advanced Vector Extensions, an x86 instruction set extension that improves
    performance by enabling larger SIMD registers and new instructions.
- term: AVX512F
  definition: The foundational instruction set of the AVX-512 family, introducing
    512-bit SIMD registers and new operations. It extends AVX capabilities significantly.
- term: -mno-avx512f
  definition: A GCC flag that explicitly disables the generation of AVX-512F instructions.
    This is used here to ensure that tests designed for AVX do not inadvertently use
    AVX-512 features.
- term: loadu2/storeu2
  definition: Likely refers to 'unaligned load/store' operations for 256-bit (AVX)
    vectors. These instructions allow loading or storing data from memory addresses
    that are not necessarily aligned to a 32-byte boundary.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3ee39cd29ad31d0035e3b1cfb798c058156868cc
date: '2026-08-23'
is_stub: true
stub_reason: low_score
---

This commit updates six test cases related to AVX loadu2/storeu2 instructions to be compiled with -mno-avx512f. This prevents failures that occur when AVX512 is enabled by default, as these tests specifically expect AVX instructions and might otherwise incorrectly match AVX512 variants, leading to test failures.
