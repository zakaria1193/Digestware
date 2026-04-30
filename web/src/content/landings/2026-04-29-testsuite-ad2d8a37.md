---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
- AVX-512
commit_hash: ad2d8a375404628de396380bb36e6f81c054c4e1
source_type: github
author: Andrew Pinski
headline: 'Testsuite: Fix and enhance cond-add-vec tests.'
tldr: Adjustments to conditional add vector tests ensure that the correct transformations
  are applied, especially when using AVX-512.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: These C++ test cases exercise vectorization of conditional expressions
  using `VEC_COND_EXPR`.  The issue is that, with certain architecture flags, the
  compiler transforms `VEC_COND_EXPR` into `COND_ADD`. The fix modifies the tests
  to account for this transformation, ensuring the tests remain valid.
primer_general: This commit modifies compiler test cases that check the behavior of
  vector conditional expressions, which are used to perform operations on multiple
  data elements simultaneously. The changes account for specific instruction set extensions
  (like AVX-512 on Intel CPUs) that can alter how these expressions are compiled,
  ensuring the tests remain accurate and reliable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ad2d8a375404628de396380bb36e6f81c054c4e1
date: '2026-04-29'
---

The vector conditional add tests `cond-add-vec-1.C` and `cond-add-vec-2.C` were updated to correctly handle cases where `VEC_COND_EXPR` is transformed into a `COND_ADD` instruction, which occurs with `-march=cascadelake` or `-mavx512f`. The tests now check for both `VEC_COND_EXPR` and `COND_ADD` to ensure the expected behavior.
