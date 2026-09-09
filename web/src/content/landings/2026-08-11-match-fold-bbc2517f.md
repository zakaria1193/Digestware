---
project: gcc
subsystem: match/fold
patch_id: null
tags:
- optimization
- pattern matching
- boolean logic
commit_hash: bbc2517fe41307a8ce21ca9b96d6660e1e842abf
source_type: github
author: Andrea Pinski
headline: 'match/fold: Add LT/GT/LE/GE to combine_comparisons'
tldr: The `combine_comparisons` function now supports less-than, greater-than, less-than-or-equal,
  and greater-than-or-equal operations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `combine_comparisons` function, used within `fold-const.cc` and
  `match.pd`, has been augmented to handle LT, GT, LE, and GE comparison codes. Previously,
  it primarily supported EQ and NE. This change improves the ability to simplify complex
  conditional expressions and boolean logic, such as representing `a > b` as `a &
  ~b`. The `match.pd` patterns have been updated to leverage this expanded functionality,
  which is anticipated to benefit `phiopt` and `ifcombine` optimizations.
primer_glossary:
- term: combine_comparisons
  definition: A GCC internal function that attempts to simplify or combine two comparison
    operations into a single, equivalent comparison or logical operation.
- term: match.pd
  definition: A file containing pattern matching rules used by GCC's tree-based optimizers
    to recognize and transform specific code structures (expressions and statements)
    into more efficient forms.
- term: phiopt
  definition: An optimization pass in GCC that deals with PHI nodes in SSA (Static
    Single Assignment) form, often related to loop-invariant code motion or other
    control-flow-based optimizations.
- term: ifcombine
  definition: An optimization pass in GCC that attempts to combine or simplify conditional
    statements (if-else structures) and boolean expressions.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned exactly once, simplifying many data-flow analyses and
    optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbc2517fe41307a8ce21ca9b96d6660e1e842abf
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

The `combine_comparisons` function in GCC's `fold-const.cc` has been extended to support the LT, GT, LE, and GE comparison operators. This enhancement, along with a corresponding update in `match.pd` to use these new capabilities, simplifies the generation of code involving boolean logic and comparisons. It is expected to facilitate better support for `phiopt` and `ifcombine` optimizations, particularly for expressions like `a > b` which can be represented as `a & !b`.
