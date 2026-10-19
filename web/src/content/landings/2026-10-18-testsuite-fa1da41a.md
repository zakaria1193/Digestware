---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- analyzer
- hppa
- OpenMP
commit_hash: fa1da41aff1774c7f98c1e3001c4c545153f1285
source_type: github
author: John David Anglin
headline: 'testsuite: Fix c-c++-common/analyzer/omp-parallel-for-1.c on hppa64-hp-hpux11.11'
tldr: Increase analyzer-max-svalue-depth for OpenMP test on HP-UX PA-RISC.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `c-c++-common/analyzer/omp-parallel-for-1.c` fails on `hppa64-hp-hpux11.11`.
  The failure is resolved by increasing the value of the `--param=analyzer-max-svalue-depth`
  option to 20. This parameter governs how deep the static analyzer, specifically
  within GCC's control flow graph (CFG) analysis, will trace symbolic value propagation.
  The increase is necessary to correctly analyze the control flow and values in the
  context of OpenMP parallel for loops on this particular architecture.
primer_glossary:
- term: analyzer-max-svalue-depth
  definition: A GCC internal parameter that limits the maximum depth of symbolic value
    analysis performed by the compiler's static analyzer. Increasing this value allows
    the analyzer to explore more complex paths in the code but can increase compilation
    time.
- term: static analyzer
  definition: A tool that analyzes source code to find potential bugs or vulnerabilities
    without actually executing the code. GCC has a built-in static analyzer that can
    detect issues like uninitialized variables or null pointer dereferences.
- term: OpenMP
  definition: An API for supporting shared-memory parallel programming in C, C++,
    and Fortran. It consists of a set of compiler directives, library routines, and
    environment variables.
- term: symbolic value analysis
  definition: A technique used by static analyzers where variables are tracked not
    by their concrete values, but by symbolic expressions representing their possible
    values or ranges.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fa1da41aff1774c7f98c1e3001c4c545153f1285
date: '2026-10-18'
is_stub: true
stub_reason: low_score
---

This commit addresses a test failure in `omp-parallel-for-1.c` on hppa64-hp-hpux11.11 by increasing the `analyzer-max-svalue-depth` option to 20. This option controls the maximum depth the static analyzer will explore for symbolic values, and a higher value is needed for this specific test case on the target platform to complete successfully.
