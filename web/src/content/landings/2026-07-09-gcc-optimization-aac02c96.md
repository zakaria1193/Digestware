---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- widening_mul
- long-multiply
commit_hash: aac02c9666184d19334a0527ec444b5e55fbd113
source_type: github
author: Konstantinos Eleftheriou
headline: 'widening_mul: Lower long-multiply chains to inline longhand'
tldr: Improves long-multiply optimization by lowering wide intermediate products to
  N-bit operations when target support is lacking.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `widening_mul` pass now lowers canonicalized longhand multiply
  chains (recognizer's form) to N-bit operations when the target cannot expand the
  full 2N-bit intermediate product. This is achieved by emitting `MULT_EXPR`s at N-bit
  precision, with explicit casts to the outer type. This lowering strategy covers
  modes lacking direct 2N-bit expansion and handles operands wider than N bits by
  splitting them. It also refines the handling of PHI nodes, chained wide products,
  and values that provably fit within N bits, ensuring correct generation even when
  the target lacks direct support for wide s…
primer_glossary:
- term: widening_mul
  definition: A GCC optimization pass that recognizes and optimizes multiplication
    operations that produce a result wider than the operands, such as multiplying
    two 64-bit integers to produce a 128-bit result. It aims to generate efficient
    code for these operations on targets that may not have direct hardware support
    for wide multiplies.
- term: GIMPLE
  definition: GCC's Internal Manipulation-code Generator and Evaluator. It is an intermediate
    representation (IR) used within GCC after the parsing and initial tree building,
    designed to be simpler and more amenable to optimization than the original AST.
- term: N-bit
  definition: Refers to a data type or operation size that is N bits wide. For example,
    32-bit integers are N-bit where N=32.
- term: PHI node
  definition: In Static Single Assignment (SSA) form, a PHI node is used at a join
    point of control flow to merge values from different predecessors. It indicates
    which version of a variable should be used based on the path taken through the
    control flow graph.
- term: optab
  definition: A table within GCC that stores operations (ops) and their corresponding
    code patterns for different data types and target architectures. It's used for
    pattern matching and code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aac02c9666184d19334a0527ec444b5e55fbd113
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This commit enhances the `widening_mul` optimization pass by introducing a mechanism to lower intermediate wide multiply products back to N-bit operations. When the target architecture cannot efficiently handle the full 2N-bit result of a multiply, this pass now breaks down the calculation into smaller, N-bit partial products that can be handled, improving code generation for such cases. It also refines how operands wider than N bits are split and how results are materialized in GIMPLE.
