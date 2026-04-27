---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- optimization
- rtl
- vectorization
- code generation
commit_hash: 0b12c7345a94f11bdacf360d45b847307f9be9cf
source_type: github
author: Roger Sayle
headline: 'rtl-optimization: Simplify vec_select of a vec_select.'
tldr: GCC now simplifies consecutive vector permutations, reducing redundant instructions
  and improving code generation for vector operations.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch adds an RTL optimization to `simplify-rtx.cc` to simplify
  a `vec_select` of a `vec_select`.  The transformation combines two consecutive vector
  permutations into a single permutation, effectively canonicalizing the expression.  The
  code leverages existing functionality in `simplify_rtx` that already detects identity
  permutations and extends it to handle more general permutation compositions.  This
  change directly impacts the RTL representation of vector operations and interacts
  with the combine pass.
primer_general: Modern processors use vector instructions to perform the same operation
  on multiple data elements simultaneously. `vec_select` is an instruction that rearranges
  elements within a vector.  This commit optimizes cases where the compiler generates
  two `vec_select` instructions in a row.  Since a permutation followed by another
  permutation is still a permutation, the two operations can be combined into one.  This
  optimization reduces the number of instructions needed, which can improve performance,
  especially in code that uses vector operations extensively, such as image processing
  or scientific simulations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0b12c7345a94f11bdacf360d45b847307f9be9cf
date: '2026-04-26'
---

GCC's RTL optimizer now simplifies vec_select operations applied consecutively. When the output of one `vec_select` instruction feeds directly into another, the compiler combines them into a single `vec_select` with an equivalent permutation.  This removes redundant shuffle instructions, leading to more compact and efficient code, particularly for vector-heavy operations.  This optimisation avoids a sequence of permutes by collapsing them into a single permute.
