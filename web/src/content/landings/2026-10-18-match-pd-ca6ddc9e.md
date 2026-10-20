---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- vectorization
- correctness
- pattern-matching
commit_hash: ca6ddc9ecd74b89284ecede2ed90f768f70d88a5
source_type: github
author: Igor Shevlyakov
headline: 'match.pd: Index BIT_FIELD_REF of VEC_PERM_EXPR inputs by their length'
tldr: Fix vector permute and bitfield reference folding to use correct input element
  counts.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The pattern matching for `BIT_FIELD_REF` applied to `VEC_PERM_EXPR`
  in `match.pd` previously determined the element count from the `sel` operand of
  the `VEC_PERM_EXPR`. This was incorrect when the input vectors (`a`, `b`) had a
  different element width than the result specified by `sel`. The fix corrects this
  by using the element count of the input vectors, resolving issues where out-of-bounds
  indices led to silent incorrect code or GIMPLE verification failures, particularly
  after vector lowering and forward propagation.
primer_glossary:
- term: BIT_FIELD_REF
  definition: A GCC Intermediate Representation (IR) node that accesses a bitfield
    within a larger value. It specifies an offset and a length for the bitfield.
- term: VEC_PERM_EXPR
  definition: A GCC Intermediate Representation (IR) node representing a vector permute
    operation, which rearranges elements within or between vectors based on a selector.
- term: GIMPLE
  definition: GCC's internal three-address code representation. It's a simpler, more
    structured form of the compiler's Abstract Syntax Tree (AST), used for many optimization
    passes.
- term: vector lowering
  definition: The process of converting high-level vector operations into a sequence
    of more primitive vector instructions supported by the target architecture. This
    can sometimes introduce intermediate forms that require careful handling.
- term: forward propagation
  definition: An optimization technique where a value computed at one point is propagated
    forward to subsequent uses, potentially allowing for further optimizations or
    elimination of redundant computations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ca6ddc9ecd74b89284ecede2ed90f768f70d88a5
date: '2026-10-18'
is_stub: false
stub_reason: ''
---

A pattern in match.pd for folding BIT_FIELD_REF applied to VEC_PERM_EXPR was incorrectly using the element count of the VEC_PERM_EXPR's selector. This led to incorrect code generation when input vectors were wider or narrower than the result. The fix ensures the element count is derived from the actual inputs, preventing silent errors and GIMPLE verification failures. New test cases are added to verify the fix.
