---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- compiler
commit_hash: a426e0a8c5ee9cdcf842ea44dc396069e890a4ca
source_type: github
author: Richard Biener
headline: Fix vector PAREN_EXPR code generation for assignments.
tldr: Correctly generates code for parenthesized expressions in vector assignments,
  fixing a bug in vectorization.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The vectorizer in GCC incorrectly ignored PAREN_EXPR nodes in vectorizable
  assignments. This commit modifies `vectorizable_assignment` in `tree-vect-stmts.cc`
  to properly generate code for these expressions, ensuring that parenthesized subexpressions
  are not lost during the vectorization pass.
primer_glossary:
- term: PAREN_EXPR
  definition: An intermediate representation (IR) node in GCC that represents a parenthesized
    expression in the source code. It signifies grouping but doesn't change the expression's
    evaluation order on its own.
- term: Vectorization
  definition: An optimization technique that transforms a scalar loop into a vector
    loop, performing the same operation on multiple data elements simultaneously using
    SIMD (Single Instruction, Multiple Data) instructions. This can significantly
    improve performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a426e0a8c5ee9cdcf842ea44dc396069e890a4ca
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit fixes a bug where parenthesized expressions (PAREN_EXPR) were incorrectly dropped during vector code generation. This led to bogus code when vectorizing assignments. The fix ensures that PAREN_EXPRs are properly handled, improving the accuracy of vectorization.
