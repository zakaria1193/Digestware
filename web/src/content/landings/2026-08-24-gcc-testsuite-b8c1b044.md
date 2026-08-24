---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- sse4.1
- avx
commit_hash: b8c1b044a4b2884577d3094513a25abcef1161ee
source_type: github
author: H.J. Lu
headline: Scan both movaps and vmovdqa in SSE4.1 STV tests
tldr: Test suite updated to scan both movaps and vmovdqa instructions to avoid failures
  with AVX enabled by default.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When AVX is enabled, the SSE4.1 instruction 'movaps' has a corresponding
  VEX-encoded version 'vmovdqa'. The testsuite's scan-assembler checks were rigid,
  expecting only 'movaps'. This change broadens the scan to include 'vmovdqa', accommodating
  the default AVX behavior and preventing test failures.
primer_glossary:
- term: movaps
  definition: An x86 instruction that moves aligned single-precision floating-point
    values. It is part of the SSE (Streaming SIMD Extensions) instruction set.
- term: vmovdqa
  definition: The VEX-encoded version of 'movdqa' (Move Aligned Double Quadword),
    which is used for AVX (Advanced Vector Extensions). It moves 128-bit aligned data.
- term: SSE4.1
  definition: A set of SSE instructions introduced with Intel Core 2 processors, offering
    enhancements for various operations, including SIMD data movement and processing.
- term: STV
  definition: Likely refers to 'Scalar/Temporary Vector' or a similar concept within
    the GCC testsuite, indicating tests focused on specific vector processing scenarios.
- term: AVX
  definition: Advanced Vector Extensions, an x86 instruction set extension that improves
    performance by enabling larger SIMD registers and new instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b8c1b044a4b2884577d3094513a25abcef1161ee
date: '2026-08-24'
is_stub: true
stub_reason: low_score
---

This commit updates three test cases in the SSE4.1 STV suite to scan for both 'movaps' and 'vmovdqa' instructions. This is necessary because when AVX is enabled by default, the compiler may generate 'vmovdqa' instead of the expected 'movaps', causing the tests to fail. Scanning both ensures the tests pass regardless of the AVX default setting.
