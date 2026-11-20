---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- GCC
commit_hash: b14dc9ddea18a3d1fd7bd05bfaf8c572bf08f428
source_type: github
author: Richard Biener
headline: Vectorization precision logic corrected for non-truncatable operations.
tldr: GCC's vectorization pass now correctly handles precision for non-truncatable
  operations and shift amounts, preventing incorrect code generation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch refines `vect_determine_precisions_from_range` and `vect_determine_min_output_precision_1`
  within the GCC tree-vectorizer. In `vect_determine_precisions_from_range`, it adds
  a check for `vect_truncatable_operation_p` before calling `vect_set_min_input_precision`.
  This prevents erroneous precision propagation for non-truncatable operations (like
  division/remainder) that might remain scalar during SLP vectorization, avoiding
  potential code generation errors due to input narrowing. In `vect_determine_min_output_precision_1`,
  it now returns `false` if the use operand is the shift amoun…
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compilation process that manipulates the intermediate
    representation (GIMPLE 'tree') to improve code efficiency.
- term: vectorization
  definition: An optimization technique that allows the compiler to perform the same
    operation on multiple data elements simultaneously, typically using SIMD (Single
    Instruction, Multiple Data) instructions.
- term: SLP vectorization
  definition: Superword-Level Parallelism vectorization. A compiler optimization that
    identifies sequences of identical scalar operations that can be vectorized, even
    if they are not part of a loop.
- term: TRUNC_DIV_EXPR
  definition: A GCC internal representation for a division operation that truncates
    the result towards zero.
- term: precision
  definition: In the context of data types, the number of bits used to represent a
    value, which determines its range and accuracy.
- term: LSHIFT_EXPR / RSHIFT_EXPR
  definition: GCC internal representations for left and right shift operations, respectively.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b14dc9ddea18a3d1fd7bd05bfaf8c572bf08f428
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This commit corrects two issues in GCC's vectorization precision logic. First, for non-truncatable operations like `TRUNC_DIV_EXPR`, the minimum input precision is no longer propagated if the operation might remain scalar, thus avoiding incorrect narrowing of inputs. Second, for shift operations (`LSHIFT_EXPR`, `RSHIFT_EXPR`), the minimum input precision is not propagated to the shift amount itself, preventing the shift count from being incorrectly narrowed and leading to wrong shift results. New test cases verify these fixes for loop and basic block vectorization.
