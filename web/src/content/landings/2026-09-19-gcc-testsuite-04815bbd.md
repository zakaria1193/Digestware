---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- hppa
- hpux
- xfail
commit_hash: 04815bbd69f0527c8a04297229859398417712b5
source_type: github
author: John David Anglin
headline: Xfail cswtch-6.c and cswtch-7.c on hppa*-*-hpux*
tldr: Marks two test cases as expected to fail on HP-UX PA-RISC due to section naming
  differences.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC test cases `gcc.dg/tree-ssa/cswtch-6.c` and `cswtch-7.c` are
  now xfailed on the `hppa*-*-hpux*` target. This target platform does not utilize
  the `.rodata.cst16` section, which these tests likely depend on for placing constants,
  leading to test failures.
primer_glossary:
- term: xfail
  definition: Expectedly fail. A test suite marker indicating that a test is known
    to fail on a particular configuration and should not cause a build failure.
- term: .rodata.cst16
  definition: A specific section name in ELF object files used for read-only constants,
    often with alignment requirements (indicated by '16'). The exact section naming
    can vary between targets and linkers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/04815bbd69f0527c8a04297229859398417712b5
date: '2026-09-19'
is_stub: true
stub_reason: low_score
---

The test cases `cswtch-6.c` and `cswtch-7.c` are marked as expected to fail on `hppa*-*-hpux*` systems. This is because these systems do not use the `.rodata.cst16` section, which the tests appear to rely on for specific data placements.
