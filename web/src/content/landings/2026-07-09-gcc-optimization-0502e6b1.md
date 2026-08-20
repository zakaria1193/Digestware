---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- forwprop
- long-multiply
- phi-node
commit_hash: 0502e6b1e7be3d3fe00727e2936d3c3a03537c4e
source_type: github
author: Konstantinos Eleftheriou
headline: 'match.pd, forwprop: Recognize long-multiply carries as 2-arg PHI'
tldr: Improves long-multiply optimization by recognizing carry propagation in PHI
  nodes with specific base+pow2 patterns.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` pass gains new recognizers in `match.pd` for `cond_carry_add`
  and `cond_carry_add_neg` patterns. These recognize PHI nodes of the form `PHI<base
  + pow2, base>` guarded by an unsigned comparison, which often represent carry propagation
  in handwritten long-multiply code. When matched, the compiler can fold these into
  a 2N-bit multiply, specifically handling the HIGH_PART of the result. This addresses
  PR tree-optimization/107090 by improving the recognition of a specific carry-handling
  idiom.
primer_glossary:
- term: forwprop
  definition: Forward propagation is an optimization pass in GCC that attempts to
    simplify expressions by replacing variables with their definitions as early as
    possible in the program flow. It's part of the SSA (Static Single Assignment)
    based optimization framework.
- term: match.pd
  definition: A file within GCC that contains pattern-matching definitions for various
    intermediate code constructs, used by optimization passes to identify and transform
    specific code sequences.
- term: PHI node
  definition: In Static Single Assignment (SSA) form, a PHI node is used at a join
    point of control flow to merge values from different predecessors. It indicates
    which version of a variable should be used based on the path taken through the
    control flow graph.
- term: long-multiply
  definition: A multiplication operation where the result's bit-width is twice that
    of the operands (e.g., multiplying two 64-bit integers to produce a 128-bit result).
    Optimizing these operations is crucial for performance on platforms that may not
    have native hardware support for such wide multiplications.
- term: GIMPLE
  definition: GCC's Internal Manipulation-code Generator and Evaluator. It is an intermediate
    representation (IR) used within GCC after the parsing and initial tree building,
    designed to be simpler and more amenable to optimization than the original AST.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0502e6b1e7be3d3fe00727e2936d3c3a03537c4e
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This commit enhances the `forwprop` (forward propagation) optimization pass to recognize and optimize long-multiply operations where the carry is expressed using a two-argument PHI node. This pattern, common in hand-written assembly, involves a PHI that conditionally adds a power of two. The pass now identifies these PHI structures and folds them into the long-multiply operation, improving the compiler's ability to optimize these cases, particularly for the high part of the multiplication.
