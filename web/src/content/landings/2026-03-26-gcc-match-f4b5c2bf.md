---
project: gcc
subsystem: gcc/match
patch_id: null
tags:
- optimization
- pattern-matching
- min
- max
commit_hash: f4b5c2bf40d68e1666c83556a236a53cdddc34a2
source_type: github
author: Pengxuan Zheng
headline: 'Match: Add simplifications for min/max comparisons.'
tldr: The compiler can now simplify comparisons between min(a, b) and max(a, b) to
  true, false, a!=b, or a==b.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file uses the Pattern Description language to define
  tree transformations. This commit adds patterns that fire during the tree-ssa phase
  to simplify relational comparisons of MIN_EXPR and MAX_EXPR.  The simplification
  patterns are architecture-independent.
primer_general: The compiler uses pattern matching to recognize opportunities for
  optimization.  The `match.pd` file contains a list of code patterns and their corresponding
  replacements. This commit adds several new patterns that allow the compiler to simplify
  code that compares the minimum and maximum of two values, potentially leading to
  more efficient code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f4b5c2bf40d68e1666c83556a236a53cdddc34a2
date: '2026-03-26'
---

New patterns were added to simplify comparisons between the results of min(a, b) and max(a, b).  Specifically, expressions like `min(a,b) <= max(a,b)` will now reduce to `true`, `min(a,b) > max(a,b)` to `false`, `min(a,b) < max(a,b)` to `a!=b`, and `min(a,b) >= max(a,b)` to `a==b`. This can help later optimization passes by removing complexity early.
