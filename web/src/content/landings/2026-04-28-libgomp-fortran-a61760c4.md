---
project: gcc
subsystem: libgomp.fortran
patch_id: null
tags:
- libgomp
- fortran
- openmp
- testing
- parallel programming
commit_hash: a61760c4e555f9f5af2ea1ca3aa7abc2e578eed1
source_type: github
author: Tobias Burnus
headline: 'libgomp.fortran/map-subarray-6.f90: Fix and robustify'
tldr: Fixed and improved the `map-subarray-6.f90` test in libgomp.fortran, addressing
  initialization issues and adding more checks for pointer handling.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch modifies the `map-subarray-6.f90` test in `libgomp.fortran`
  to address initialization issues and improve robustness. The changes involve correctly
  initializing variables and adding explicit handling for self-mapping/host fallback
  scenarios, as well as checks for pointer attaching using values outside the mapped
  range. The patch also handles cases where 'tgt' is removed during gimplification.
primer_general: Libgomp is GCC's implementation of the OpenMP API, which provides
  a standardized way to write parallel programs. This commit focuses on improving
  a specific test case for Fortran code that utilizes OpenMP's data mapping features,
  which control how data is shared between the main program and parallel regions.
  The changes ensure the test case is more reliable and handles different scenarios
  correctly, contributing to the overall stability of the OpenMP implementation in
  GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a61760c4e555f9f5af2ea1ca3aa7abc2e578eed1
date: '2026-04-28'
---

This commit addresses issues within the `map-subarray-6.f90` test in libgomp.fortran. The changes include correctly initializing variables, explicitly handling different mapping scenarios (self-mapping, host accessibility), and adding checks to prevent pointer attaching using values outside the mapped range. These fixes and enhancements improve the robustness and reliability of the test, ensuring proper behavior in various scenarios.
