---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- hppa
- hpux
- xfail
commit_hash: e741ce45698e48d376fa50e474935adaa55efaf8
source_type: github
author: John David Anglin
headline: Xfail pr125734.c on hppa*-*-hpux*
tldr: Marks a test case as expected to fail on HP-UX PA-RISC due to missing CLZ instruction
  support.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC test case `gcc.dg/tree-ssa/pr125734.c` is now xfailed on the
  `hppa*-*-hpux*` target. This target architecture does not have a hardware instruction
  equivalent to CLZ (count leading zeros), which the test appears to exercise, thus
  making the test's expected outcome unattainable on this platform.
primer_glossary:
- term: CLZ
  definition: Count Leading Zeros. An instruction that counts the number of zero bits
    preceding the most significant one bit in a binary representation.
- term: xfail
  definition: Expectedly fail. A test suite marker indicating that a test is known
    to fail on a particular configuration and should not cause a build failure.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e741ce45698e48d376fa50e474935adaa55efaf8
date: '2026-09-19'
is_stub: true
stub_reason: low_score
---

The test case `pr125734.c` is marked as expected to fail on `hppa*-*-hpux*` systems. This is because these systems do not utilize the CLZ (count leading zeros) instruction, which the test likely relies on.
