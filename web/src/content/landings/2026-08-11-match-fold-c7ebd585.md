---
project: gcc
subsystem: match/fold
patch_id: null
tags:
- optimization
- pattern matching
- floating point
commit_hash: c7ebd58535ad63351123e2aa98b92b1eec3c8ca9
source_type: github
author: Andrea Pinski
headline: 'match/fold: Add NE, XOR, and EQ to combine_comparisons'
tldr: The `combine_comparisons` function now supports NE, XOR, and EQ, simplifying
  floating-point comparisons and code structure.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit enhances `combine_comparisons` in `fold-const.cc` to handle
  NE, XOR, and EQ, previously limited primarily to other operators. It also introduces
  overloaded bitwise operators (`~`, `|`, `&`, `^`) for `comparison_code` within an
  anonymous namespace for cleaner expression. The `match.pd` patterns that use `combine_comparisons`
  for these operators are now placed before other combines to ensure they are matched
  first. This simplifies floating-point comparison handling and reduces the complexity
  of the pattern matching code.
primer_glossary:
- term: combine_comparisons
  definition: A GCC internal function that attempts to simplify or combine two comparison
    operations into a single, equivalent comparison or logical operation.
- term: match.pd
  definition: A file containing pattern matching rules used by GCC's tree-based optimizers
    to recognize and transform specific code structures (expressions and statements)
    into more efficient forms.
- term: floating point
  definition: A method of approximating real numbers using a fixed number of digits,
    commonly used in computers for scientific and engineering calculations. Floating-point
    arithmetic can introduce small precision errors.
- term: GIMPLE
  definition: GCC's three-address intermediate representation. It simplifies control
    flow and data flow analysis, serving as a common ground for various optimization
    passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c7ebd58535ad63351123e2aa98b92b1eec3c8ca9
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

GCC's `combine_comparisons` function has been updated to include support for the NE (not equal), XOR, and EQ (equal) operators. This change simplifies the internal `match.pd` patterns by allowing them to utilize this function for these comparison types, leading to cleaner code and enabling more opportunities for merging floating-point comparisons. The relevant patterns in `match.pd` have been reordered to ensure these new combinations are prioritized.
