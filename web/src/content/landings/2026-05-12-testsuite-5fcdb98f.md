---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- C
- C++
commit_hash: 5fcdb98f7ca658f053a2157731080af56550ca2b
source_type: github
author: Alexandre Oliva
headline: 'Testsuite: Include stddef.h for size_t in pr94994'
tldr: Fixes a testcase that used size_t without including stddef.h.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit fixes a testcase that uses size_t without including stddef.h.
  This is a straightforward fix to ensure the testcase compiles correctly.
primer_general: In C and C++, size_t is a type commonly used to represent the size
  of objects. It's defined in the stddef.h header file.  For code to use size_t, it
  needs to include this header file so that the compiler knows what size_t refers
  to.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5fcdb98f7ca658f053a2157731080af56550ca2b
date: '2026-05-12'
is_stub: false
---

The testcase in gcc.dg/vect/pr94994.c refers to size_t without including stddef.h. This commit adds the necessary include to fix the testcase.
