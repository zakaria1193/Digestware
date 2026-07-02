---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- bugfix
- optimization
- middle-end
commit_hash: 7ec15f8a0b357e33a9c93ad25e4401dd75b7d466
source_type: github
author: Andrew Pinski
headline: Disabling a match pattern for non-GIMPLE avoids infinite loops.
tldr: GCC now disables a specific optimization pattern for non-GIMPLE code, preventing
  a stack overflow crash.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'GCC''s `match.pd` defines patterns for recognizing and transforming
  code. This commit disables a specific pattern, `if (cond) (A | CST1) : (A & ~CST1)`,
  for non-GIMPLE code. The issue arose because the `fold` pass, particularly `fold_binary_op_with_conditional_arg`,
  could reintroduce the original form after the pattern''s transformation into `(A
  & ~CST1) | (cond * CST1)`. This retransformation created an infinite loop within
  the compiler''s optimization passes, leading to a stack overflow. Restricting the
  pattern to GIMPLE ensures it''s only applied at a stage where the `fold` pass is
  less likely…'
primer_general: Compilers transform your code through several stages to make it efficient.
  One stage involves recognizing common code structures and optimizing them. This
  commit fixes a bug in GCC where a specific code transformation, designed to make
  conditional expressions more efficient, could cause the compiler to get stuck in
  an endless loop if applied at the wrong time. This happened because another part
  of the compiler would then undo the transformation, and the first part would re-apply
  it, causing a cycle. The fix ensures this particular optimization is only applied
  at a stage where it won't be immediately undone, preventing the compiler from crashing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7ec15f8a0b357e33a9c93ad25e4401dd75b7d466
date: '2026-06-04'
is_stub: false
---

This GCC commit disables a specialized pattern, `if (cond) (A | CST1) : (A & ~CST1)`, when processing non-GIMPLE intermediate representation. Previously, this pattern could interact negatively with the `fold` optimization pass, creating an infinite loop and leading to a stack overflow. Restricting the pattern to GIMPLE code prevents these crashes, improving compiler stability.
