---
project: gcc
subsystem: gcc/value-range
patch_id: null
tags:
- optimization
- floating-point
- compiler internals
- range analysis
commit_hash: a430011e1c2b75ff7a2cd82b118c69ffc168127a
source_type: github
author: Aldy Hernandez
headline: Floating-point range analysis now represents and handles inverse constant
  ranges.
tldr: GCC's floating-point range analysis can now represent intervals that exclude
  specific values, improving precision.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `frange` class in `value-range.cc` now supports `set_excluding`,
  enabling the representation of intervals that exclude specific points. This is achieved
  by transforming an exclusion request (e.g., `set(type, C, C, VR_ANTI_RANGE)`) into
  two explicit sub-ranges: `[-INF, prev(C)]` and `[next(C), +INF]`. This capability
  is crucial for precisely handling inequalities like `x != C` and brings the floating-point
  value-range propagation (VRP) analysis in line with integer VRP and DOM analysis,
  particularly benefiting floating-point intensive code like LAPACK.'
primer_glossary:
- term: frange
  definition: Represents a range of floating-point values within GCC's value-range
    propagation (VRP) analysis. It's part of the compiler's effort to understand and
    optimize numerical computations.
- term: value-range propagation (VRP)
  definition: A compiler optimization technique that tracks the possible range of
    values a variable can hold throughout the program to enable more aggressive optimizations.
- term: inverse range
  definition: A mathematical representation of all values *not* within a specified
    range. For example, the inverse of the range [2, 5] would be (-infinity, 2) U
    (5, +infinity).
- term: VR_ANTI_RANGE
  definition: A flag used in GCC's value-range analysis to signify the inverse of
    a normal range, often used to represent exclusion of specific values or sets of
    values.
- term: VR_VARYING
  definition: A state in GCC's value-range analysis indicating that the range of possible
    values for a variable is too complex or unpredictable to determine precisely.
- term: prev() and next()
  definition: Functions that return the representable floating-point number immediately
    preceding or succeeding a given value, respectively. Crucial for defining bounds
    of excluded intervals.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a430011e1c2b75ff7a2cd82b118c69ffc168127a
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's floating-point range analysis (`frange`) to correctly represent the inverse of a constant range. Previously, attempts to exclude a value were lost, turning into a generic 'varying' range. The update allows `frange` to store intervals like `x != C` by representing them as two sub-ranges, bringing it to parity with other analysis methods and improving the compiler's ability to optimize code involving inequalities.
