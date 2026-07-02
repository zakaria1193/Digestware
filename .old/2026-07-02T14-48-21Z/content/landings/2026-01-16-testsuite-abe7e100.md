---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- deprecated
- warning
commit_hash: abe7e10012051344695760e89419c7df73cce856
source_type: github
author: Daniel Barboza
headline: 'Testsuite: Remove all Wstrict-overflow tests.'
tldr: All remaining tests specifically checking for `-Wstrict-overflow` behavior have
  been removed.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit removes a large number of test files from the GCC testsuite,
  all named `gcc.dg/Wstrict-overflow-*.c`. Search terms: GCC testsuite -Wstrict-overflow'
primer_general: A compiler testsuite ensures the compiler produces correct code and
  diagnostics.  As features are deprecated or removed from the compiler, corresponding
  tests are removed, which keeps the testsuite maintainable and focused on current
  functionality. This commit removes the tests for the deprecated `-Wstrict-overflow`
  flag.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/abe7e10012051344695760e89419c7df73cce856
date: '2026-01-16'
is_stub: false
---

The testsuite no longer contains any tests that explicitly check for `-Wstrict-overflow` warnings.  Since these warnings are no longer issued, the tests were either compile tests that were not expected to issue a warning, or XFAIL tests. Removing them simplifies the testsuite and avoids confusion.
