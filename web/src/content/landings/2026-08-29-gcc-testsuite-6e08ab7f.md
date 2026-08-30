---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- integer size
commit_hash: 6e08ab7fbbcc776ca326c10578d931761c765e02
source_type: github
author: Georg-Johann Lay
headline: Skip tree-ssa test assuming 32-bit integers on smaller architectures
tldr: A tree-ssa test case failing due to int32plus assumptions is now skipped on
  relevant architectures.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR 112104 by skipping a tree-ssa test case that
  fails due to implicit int32plus assumptions. The test triggered an overflow warning
  and a failure on platforms where 'int' is smaller than 32 bits. The fix adds a requirement
  for int32plus, making the test conditional and preventing regressions on non-32-bit
  int platforms.
primer_glossary:
- term: tree-ssa
  definition: A GCC optimization pass that transforms the compiler's intermediate
    representation into a Static Single Assignment (SSA) form, facilitating various
    optimizations.
- term: int32plus
  definition: A compiler capability indicating that the 'int' type is at least 32
    bits wide.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6e08ab7fbbcc776ca326c10578d931761c765e02
date: '2026-08-29'
is_stub: true
stub_reason: low_score
---

This commit skips the gcc.dg/tree-ssa/pr112104-2.c test case, which failed due to an implied assumption of int32plus. The test produced an overflow warning when unsigned long was converted to unsigned int. By requiring the int32plus capability, the test is now skipped on architectures where int is smaller than 32 bits, resolving spurious failures.
