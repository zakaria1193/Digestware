---
project: gcc
subsystem: gfortran.dg/coarray
patch_id: null
tags:
- fortran
- coarray
- testing
- parallel programming
commit_hash: 66b306adb2d8749dd70efa8fedb0e50e0fffb00d
source_type: github
author: Hans-Peter Nilsson
headline: Fortran coarray tests now require target sleep due to recent changes.
tldr: Fixes test failures for Fortran coarrays by requiring target sleep where calls
  were recently added.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The coarray feature in Fortran allows for parallel programming.  This
  change modifies the testsuite (specifically, files in gfortran.dg/coarray/) to account
  for timing-related issues that arise in parallel execution environments.  The 'target
  sleep' requirement likely relates to ensuring proper synchronization or ordering
  of operations in the tests.
primer_general: Fortran coarrays enable parallel programming within Fortran code.
  This commit adjusts the testing infrastructure for coarrays to handle timing issues.
  Due to the distributed nature of parallel programs, tests need to account for the
  time it takes for different parts of the program to communicate and synchronize.  The
  changes ensure more reliable and accurate testing of coarray functionality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/66b306adb2d8749dd70efa8fedb0e50e0fffb00d
date: '2026-04-23'
is_stub: false
---

Some Fortran coarray tests were failing due to recent additions of calls. This commit addresses the issue by adding a requirement for target sleep to these tests. This ensures that the tests pass consistently.
