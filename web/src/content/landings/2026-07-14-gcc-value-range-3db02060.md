---
project: gcc
subsystem: gcc/value-range
patch_id: null
tags:
- optimization
- floating-point
- compiler internals
commit_hash: 3db020600d47180dc097f405d1dd7cfcafe24d43
source_type: github
author: Aldy Hernandez
headline: New frange::set_nonzero and nonzero_p methods simplify floating-point range
  analysis.
tldr: Floating-point range analysis gains methods to represent and check for non-zero
  values, improving accuracy.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `value-range.cc` (frange) implementation now includes `set_nonzero`
  and `nonzero_p`. These complement the existing `irange` and `prange` predicates.
  The historical quirk of `nonzero_p` returning true only for `~[0,0]` is maintained,
  but `frange`'s `nonzero_p` now correctly ignores NaN bits when dealing with the
  `~[-0.0, +0.0] +-NAN` case, ensuring broader correctness for floating-point ranges.
primer_glossary:
- term: frange
  definition: Represents a range of floating-point values within GCC's value-range
    propagation (VRP) analysis. It's part of the compiler's effort to understand and
    optimize numerical computations.
- term: nonzero_p
  definition: A predicate function that returns true if a given range is known not
    to contain zero. Its specific implementation and behavior can vary slightly between
    integer and floating-point range representations.
- term: VR_ANTI_RANGE
  definition: A flag used in GCC's value-range analysis to signify the inverse of
    a normal range, often used to represent exclusion of specific values or sets of
    values.
- term: NAN
  definition: Not a Number. An IEEE 754 floating-point value representing an undefined
    or unrepresentable result, such as from an invalid operation like dividing zero
    by zero.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3db020600d47180dc097f405d1dd7cfcafe24d43
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

This commit introduces `frange::set_nonzero` and `frange::nonzero_p` to the GCC value-range analysis. These methods allow the compiler to more accurately represent and detect ranges that exclude zero, which is crucial for optimizing floating-point computations. The changes were tested on ppc64le Linux and did not alter generated output for tested Fortran files, indicating effective internal handling.
