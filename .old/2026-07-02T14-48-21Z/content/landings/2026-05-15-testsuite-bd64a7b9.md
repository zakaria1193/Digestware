---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- aarch64
- sve
- vectorization
- slp
commit_hash: bd64a7b9437c39ef0fe9bea25a0d81eaff25b3a5
source_type: github
author: Lili Cui
headline: 'Testsuite: Add AArch64 SVE support to slp-reduc-15.c'
tldr: The slp-reduc-15.c test now supports AArch64 SVE and uses -mavx2 for x86 to
  cover all x86 modes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit extends the `slp-reduc-15.c` test case to include AArch64
  SVE support using `-march=armv8.2-a+sve`.  It also updates the x86 target to use
  `-mavx2` instead of `-march=x86-64-v3` to cover all x86 modes.  This change ensures
  that SLP vectorization is thoroughly tested on both AArch64 and x86 architectures,
  providing better coverage for the SLP vectorizer.
primer_general: The compiler uses Single Loop Vectorization (SLP) to combine similar
  independent calculations into vector operations, speeding up code execution.  This
  commit updates a test case to ensure that SLP vectorization works correctly on AArch64
  architecture with Scalable Vector Extension (SVE) and on all x86 modes.  The test
  case verifies that the compiler can effectively vectorize code using SLP on these
  platforms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bd64a7b9437c39ef0fe9bea25a0d81eaff25b3a5
date: '2026-05-15'
is_stub: false
---

The test case `gcc.dg/vect/slp-reduc-15.c` now includes AArch64 SVE support and uses `-mavx2` for x86 to support all x86 modes. This enhancement ensures comprehensive testing of SLP vectorization across different architectures.  The changes involve adding an `aarch64-*-*` target using `-march=armv8.2-a+sve` and separating `-fgimple` from architecture-specific options.
