---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- testsuite
- portability
commit_hash: be2bf2db773c01516b71a388221d61443fa069ee
source_type: github
author: Jerry DeLisle
headline: 'fortran: Adjust test cases for span addressing'
tldr: 'fortran: Corrects test cases that incorrectly expected span addressing on certain
  platforms.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'PR fortran/126964: Adjusts test cases in `gfortran.dg/c_loc_test_22.f90`
  and `gfortran.dg/gomp/target-span-1.f90` to not expect span addressing when the
  spacing is not known to be folded, improving test case robustness.'
primer_glossary:
- term: span addressing
  definition: A feature related to memory addressing in Fortran, potentially allowing
    operations on contiguous blocks of memory.
- term: folded
  definition: In compiler optimization, refers to an expression or value that has
    been simplified or pre-calculated.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/be2bf2db773c01516b71a388221d61443fa069ee
date: '2026-09-08'
is_stub: true
stub_reason: low_score
---

This commit adjusts several Fortran test cases to prevent them from failing on platforms where span addressing behavior is not guaranteed or folded. By dropping the expectation of span addressing in these specific test files, the suite becomes more portable and robust across different environments.
