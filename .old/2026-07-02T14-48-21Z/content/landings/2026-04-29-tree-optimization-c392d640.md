---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- slp
commit_hash: c392d64098cc675c804ff4f516548d023a4fe29a
source_type: github
author: Richard Biener
headline: 'SLP: Keep scalar statements for instance roots in externs'
tldr: Fixes SLP vectorization to prevent errors when instance roots are mentioned
  in externs of other instances.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's SLP vectorizer (in ``tree-vect-slp.cc``) hoists scalar operations
  into vector ones based on data dependencies and memory aliasing. The transformation
  has to respect external references, and this patch keeps scalar stmts for instance
  roots mentioned in externs of other instances.
primer_general: Superword Level Parallelism (SLP) is a compiler optimization that
  transforms scalar operations into vector operations to improve performance. This
  optimization identifies sequences of independent scalar operations that can be performed
  in parallel using vector instructions. The compiler needs to be careful when dealing
  with external references to variables to make sure the transformation is correct.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c392d64098cc675c804ff4f516548d023a4fe29a
date: '2026-04-29'
---

This commit fixes a bug in the SLP (superword level parallelism) vectorization pass that caused incorrect code generation when instance roots were referenced in externs of other instances. The fix ensures that instance root statements are kept scalar if they appear in externs, preventing the vectorization that would lead to errors. A new test case is added to verify the fix.
