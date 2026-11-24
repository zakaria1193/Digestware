---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- cost-model
commit_hash: 2f817b3ea9e9ed00c7f158bb43e6c234e5962bbd
source_type: github
author: Richard Biener
headline: Vectorizer costs PAREN_EXPR as NOP to improve accuracy.
tldr: The vectorizer now correctly costs PAREN_EXPR as a NOP, preventing inaccurate
  cost modeling.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-vect-stmts.cc`, the vectorizer uses a cost model to decide
  whether to vectorize loops. `PAREN_EXPR` nodes, which represent grouping of expressions,
  were previously costed as `vector_stmt`. This commit corrects `vect_nop_conversion_p`
  to identify `PAREN_EXPR` as a NOP, ensuring it doesn't artificially inflate the
  cost of vectorized code and allows more accurate decisions. This is relevant for
  optimizing code involving parenthesized expressions.
primer_glossary:
- term: Vectorizer
  definition: A compiler component that attempts to transform scalar code into vector
    code, using SIMD (Single Instruction, Multiple Data) instructions to process multiple
    data elements in parallel.
- term: PAREN_EXPR
  definition: A GCC Tree IR node representing an expression enclosed in parentheses.
    It typically does not alter the computation itself but affects grouping and precedence.
- term: NOP
  definition: No Operation. An instruction or operation that has no effect on the
    program state. In cost modeling, it usually has a cost of zero.
- term: Cost Model
  definition: A component of the compiler's optimization passes that estimates the
    execution cost (e.g., instruction count, latency, throughput) of different code
    sequences to guide optimization decisions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2f817b3ea9e9ed00c7f158bb43e6c234e5962bbd
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

The GCC vectorizer previously mis-costed PAREN_EXPR nodes, treating them as scalar or vector statements which unfairly benefited the vectorizer's decision-making. This commit corrects the costing to treat PAREN_EXPR as a NOP (no operation), leading to more accurate cost modeling for vectorization. A new test case verifies this change.
