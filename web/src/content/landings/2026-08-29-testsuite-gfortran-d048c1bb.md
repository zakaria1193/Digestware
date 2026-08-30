---
project: gcc
subsystem: testsuite/gfortran
patch_id: null
tags:
- testsuite
- gfortran
- inlining
commit_hash: d048c1bb016c3c7b911086ce2ca90f3dc9b24947
source_type: github
author: Jakub Jelinek
headline: Improve guality/arg1.f90 testcase by adjusting breakpoint location
tldr: The gfortran guality/arg1.f90 test case is improved by fixing a breakpoint issue
  that caused spurious failures.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Addresses a regression in gfortran.dg/guality/arg1.f90 on s390x and
  aarch64, seen in GCC 16. The failure was caused by a change in inlining heuristics
  in `r16-372` which led to the sub-procedure being inlined into `MAIN__`. Consequently,
  the breakpoint on line 14 was incorrectly positioned after array stores. This commit
  adjusts the breakpoint's placement to align with the actual execution after these
  transformations, resolving the test failure.
primer_glossary:
- term: gfortran
  definition: The GNU Fortran compiler, part of the GCC suite.
- term: inlining heuristics
  definition: Rules and algorithms used by the compiler to decide whether to substitute
    the body of a function call directly at the call site, optimizing performance.
- term: breakpoint
  definition: A point in a program where execution is paused, typically used for debugging.
    In test cases, specific instruction sequences can be designated as breakpoints.
- term: DWARF
  definition: A debugging data format used by many Unix-like systems to support debuggers
    and other tools that need to understand the structure of compiled programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d048c1bb016c3c7b911086ce2ca90f3dc9b24947
date: '2026-08-29'
is_stub: true
stub_reason: low_score
---

This commit improves the gfortran.dg/guality/arg1.f90 test case, which was failing on s390x and aarch64 due to a regression in inlining heuristics introduced in GCC 16. The issue arose because the breakpoint was placed too early after code transformations, causing the test to fail even though the generated code was correct. The fix adjusts the breakpoint timing to accurately reflect the program's execution flow after inlining.
