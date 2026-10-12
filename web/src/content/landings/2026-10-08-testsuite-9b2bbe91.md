---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- hppa
- hpux
- skip
commit_hash: 9b2bbe9104aef2e6bd9e8d7ace5fed3e2726f4d3
source_type: github
author: John David Anglin
headline: Skip failing tests on hppa*-*-hpux*
tldr: GCC skips several test cases on hppa*-*-hpux* due to math library limitations,
  ABI issues, and toolchain problems.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit marks testsuite failures on the `hppa*-*-hpux*` target
  as expected. The failures stem from target-specific limitations in math library
  support (C99/C11), ABI issues (libstdc++ constructor clones), numerical precision
  limitations (quad-precision folding), toolchain issues (`ar` deadlocks), and frontend
  robustness problems (syntax error recovery). Skipping these tests prevents spurious
  regressions on this platform.
primer_glossary:
- term: libm
  definition: The standard C math library.
- term: libstdc++
  definition: The C++ standard library implementation used by GCC.
- term: C4 unified constructor clones
  definition: A specific ABI feature for C++ constructors used in certain compiler
    versions or configurations.
- term: quad-precision folding
  definition: Optimization that performs arithmetic operations on 128-bit floating-point
    numbers directly in hardware.
- term: ar tool
  definition: The archive utility, used for creating static libraries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9b2bbe9104aef2e6bd9e8d7ace5fed3e2726f4d3
date: '2026-10-08'
is_stub: true
stub_reason: low_score
---

This commit skips multiple test cases on the `hppa*-*-hpux*` target. The failures are attributed to the target's limited C99/C11 math library support, missing C4 unified constructor clones in libstdc++, lack of hardware quad-precision folding, `ar` tool deadlocks, and issues with the frontend's syntax error recovery. Skipping these tests prevents spurious regressions on this platform.
