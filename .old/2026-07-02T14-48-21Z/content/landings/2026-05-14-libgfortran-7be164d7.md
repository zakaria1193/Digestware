---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- typo
- cleanup
commit_hash: 7be164d7fc738d51b3ea83f6926d7305c3225e1f
source_type: github
author: Dhruv Chawla
headline: 'Libgfortran: Correct typos in source files.'
tldr: This commit fixes typos across multiple libgfortran source files.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses typos in various libgfortran files, including
  CAF (`caf/`), intrinsics (`intrinsics/`), I/O (`io/`), and runtime (`runtime/`)
  components.  These fixes improve code clarity across the Fortran runtime library.
primer_general: This commit cleans up typos in libgfortran, the Fortran runtime library
  used by GCC. This library provides essential functions for Fortran programs, covering
  areas like parallel processing with coarrays, intrinsic functions, input/output
  operations, and general runtime support. Typos in the code, while not functional
  bugs, can make the code harder to read and maintain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7be164d7fc738d51b3ea83f6926d7305c3225e1f
date: '2026-05-14'
is_stub: true
stub_reason: low-score
---

This commit resolves typos in various files within the libgfortran directory, including files related to coarray Fortran (CAF), intrinsics, I/O, and runtime support. These changes improve code readability and maintainability.
