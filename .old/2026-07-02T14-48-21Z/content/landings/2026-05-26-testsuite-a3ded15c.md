---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- deprecated
- warning
commit_hash: a3ded15ccfe436efbf60e9f35d02c6904f2417c3
source_type: github
author: Daniel Barboza
headline: 'Testsuite: Remove tests related to Wstrict-overflow.'
tldr: The testsuite no longer includes tests for the `-Wstrict-overflow` flag, which
  is now deprecated.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit removes several test files from the GCC testsuite, including
  `gcc.dg/pr36227.c`, `gcc.dg/pr48022-1.c`, `gcc.dg/pr48022-2.c`, `gcc.dg/pr49705.c`,
  and `gcc.dg/pr52904.c`. It also removes `-Wstrict-overflow` options from `gcc.dg/pr81592.c`
  and `gcc.dg/pragma-diag-3.c`. Search terms: GCC testsuite -Wstrict-overflow'
primer_general: A compiler testsuite ensures that the compiler behaves as expected
  by running a series of tests and verifying that the output matches the expected
  results. These tests cover various aspects of the language and compiler, including
  warning messages. As compiler features are deprecated or removed, the corresponding
  tests are also removed to keep the testsuite relevant and maintainable. This commit
  removes tests related to the deprecated `-Wstrict-overflow` flag.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a3ded15ccfe436efbf60e9f35d02c6904f2417c3
date: '2026-05-26'
is_stub: false
---

The testsuite has been cleaned up by removing tests related to the `-Wstrict-overflow` option, which is now obsolete. This includes removing tests for specific bug reports, such as PR36227, PR48022, PR49705, and PR52904, as well as removing `-Wstrict-overflow` checks from other tests.  These tests exercised code paths that no longer exist, so removing them simplifies the testsuite.
