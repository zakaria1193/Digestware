---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- refactor
- readability
- simplification
commit_hash: e76eb03d7722828ebb1a8c5d2f237eb5a9f87631
source_type: github
author: Igor Shevlyakov
headline: Name comparison mask bits for clarity
tldr: Improves readability of comparison mask logic in simplify-rtx.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `simplify-rtx.cc`, the `simplify_logical_relational_operation` function
  uses bitmasks to represent the possible outcomes of combining two comparison predicates.
  This commit replaces the use of raw integer bit values with a new `enum comparison_mask`
  for better readability and maintainability. Functions like `unsigned_comparison_to_mask`,
  `mask_to_comparison`, and `simplify_context::simplify_logical_relational_operation`
  now use these named enumerators.
primer_glossary:
- term: RTX
  definition: Representation of intermediate language in GCC. RTX is a Lisp-like language
    used to represent the program's structure and operations internally within the
    compiler.
- term: Comparison Predicate
  definition: A condition that evaluates to true or false. In this context, it refers
    to the result of a floating-point comparison operation (e.g., less than, equal
    to).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e76eb03d7722828ebb1a8c5d2f237eb5a9f87631
date: '2026-10-18'
is_stub: true
stub_reason: low_score
---

This change introduces an enum `comparison_mask` to assign names to the bits used within the comparison masks in `simplify-rtx.cc`. This improves code clarity and maintainability by replacing magic numbers with descriptive names for different comparison outcomes. No functional changes are introduced.
