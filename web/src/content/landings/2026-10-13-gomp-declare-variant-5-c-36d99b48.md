---
project: gcc
subsystem: gomp/declare-variant-5.c
patch_id: null
tags:
- testsuite
- openmp
- simd
- c++
commit_hash: 36d99b4873e675a5f7d389f5b27239ecdcd6677c
source_type: github
author: Tobias Burnus
headline: 'gomp/declare-variant-5.c: Add xfail for C++'
tldr: 'gomp/declare-variant-5.c: Marks C++ test case as expected to fail due to SIMD
  trait issues.'
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds `dg-bogus` and `xfail` directives to the `c-c++-common/gomp/declare-variant-5.c`
  test case. This is a workaround for failures observed in C++ compilation stemming
  from recent improvements to the SIMD trait handling in the compiler's middle-end.
  The test is temporarily marked to avoid disrupting the test suite while a proper
  fix is developed.
primer_glossary:
- term: xfail
  definition: A directive in GCC's testsuite that marks a test case as 'expected to
    fail'. The test suite will continue running but will not report an xfail test
    as a failure.
- term: SIMD trait
  definition: Traits related to Single Instruction, Multiple Data (SIMD) operations,
    which allow a single instruction to operate on multiple data elements simultaneously
    for performance gains.
- term: dg-bogus
  definition: A GCC testsuite directive that indicates a test case has known issues
    or is intentionally problematic, often used in conjunction with xfail.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/36d99b4873e675a5f7d389f5b27239ecdcd6677c
date: '2026-10-13'
is_stub: true
stub_reason: low_score
---

This commit marks the `declare-variant-5.c` test case as expected to fail for C++ (`xfail`). A recent fix in the SIMD trait handling has caused this test to fail, and this change silences it with `dg-bogus` and `xfail` directives until the underlying issue can be properly addressed.
