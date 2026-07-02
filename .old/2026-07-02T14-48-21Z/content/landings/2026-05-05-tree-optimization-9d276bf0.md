---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- slp
- ice
- bugfix
commit_hash: 9d276bf057459de93ba304cdf780dbff3882491e
source_type: github
author: Richard Biener
headline: Fix ICE when associating DOT_PROD_EXPR in SLP vectorization.
tldr: Prevents an internal compiler error (ICE) during SLP vectorization when handling
  DOT_PROD_EXPR by avoiding non-binary associatable statements.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: During SLP vectorization, the compiler attempts to identify reduction
  chains. This patch modifies `tree-vect-slp.cc` to prevent non-binary associatable
  statements from being passed to `vect_slp_linearize_chain` when handling `DOT_PROD_EXPR`
  nodes.  This avoids an ICE (internal compiler error) reported in PR tree-optimization/125185.
  A new test case, `pr125185.c`, is added to `gcc.dg/torture/`.
primer_general: Vectorization is a compiler optimization technique that allows the
  compiler to perform multiple operations simultaneously using vector instructions.  SLP
  (Superword Level Parallelism) vectorization is a specific type of vectorization
  that identifies sequences of independent operations that can be combined into a
  single vector operation.  This commit fixes a bug that could cause the compiler
  to crash during SLP vectorization when dealing with dot product expressions (calculating
  the sum of the products of corresponding elements of two vectors). The fix ensures
  that the compiler correctly handles these expressions during optimization, preventing
  unexpected errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9d276bf057459de93ba304cdf780dbff3882491e
date: '2026-05-05'
---

This commit fixes an internal compiler error (ICE) that could occur during SLP (Superword Level Parallelism) vectorization when dealing with `DOT_PROD_EXPR` nodes. The issue arose when non-binary associatable statements were incorrectly passed to `vect_slp_linearize_chain`. The fix adds a check to prevent this, thus avoiding the ICE. A new test case is added to verify the fix.
