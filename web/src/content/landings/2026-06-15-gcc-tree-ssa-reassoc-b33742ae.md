---
project: gcc
subsystem: gcc/tree-ssa-reassoc
patch_id: null
tags:
- optimization
- bugfix
commit_hash: b33742aed1176e4701a1daff6c34ff2ca9991be7
source_type: github
author: Richard Biener
headline: Fixes VEC_COND_EXPR matching with inverted compare.
tldr: GCC now correctly identifies `VEC_COND_EXPR` patterns, even when a comparison
  is inverted, preventing misidentification of operand values.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ovce_extract_ops` function in `tree-ssa-reassoc.cc` performs various
  transformations, including recognizing `VEC_COND_EXPR` patterns. This commit addresses
  a bug where the logic for inverting a comparison (`cmp`) and then validating the
  false-value operand (which should correspond to {-1,...}) would subsequently attempt
  to validate it as {0,...}. This was an incorrect assumption, and the fix ensures
  the true-value operand is checked in this specific inverted comparison scenario.
  This improves the reliability of certain vector conditional optimizations.
primer_general: Compilers like GCC convert your human-readable code into an intermediate
  representation (IR) before generating machine code. One optimization pass, called
  reassociation, rearranges mathematical and logical operations in this IR to make
  them more efficient. Imagine an expression like `A + B + C`; reassociation might
  change it to `(A + C) + B` if that avoids some redundant calculation. This commit
  fixes a specific issue in how GCC recognizes and optimizes 'vector conditional expressions'
  (`VEC_COND_EXPR`). These are like `if-else` statements but apply to multiple data
  elements at once, often used in performance-critical code. The bug caused the compiler
  to misinterpret parts of these expressions when a comparison was flipped, potentially
  missing optimization opportunities or even generating slightly less efficient code.
  The fix ensures the compiler correctly understands these expressions, leading to
  better optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b33742aed1176e4701a1daff6c34ff2ca9991be7
date: '2026-06-15'
is_stub: false
---

GCC's `tree-ssa-reassoc` pass, responsible for reassociating operations, previously mishandled `VEC_COND_EXPR` (vector conditional expression) matching when the comparison was inverted. Specifically, it incorrectly checked the false-value operand for a condition that should have been applied to the true-value operand. This fix corrects the logic, ensuring that the appropriate operand is checked, thus improving the accuracy of vector conditional expression optimizations.
