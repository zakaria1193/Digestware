---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- optimization
- performance
- aarch64
commit_hash: 806feb8e017b243de37e4502a6fc01fb76dd1529
source_type: github
author: Konstantinos Eleftheriou
headline: 'forwprop: Match and fold the long-multiply carry form'
tldr: Recognizes and folds a specific pattern of long-multiply summation to improve
  performance.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The forward propagation pass (forwprop) now recognizes and optimizes
  the summation of partial products from a 2N-bit unsigned multiplication. It identifies
  the specific pattern involving four NxN partial products, a carry-sum, and an overflow-compare,
  then rewrites it using widening multiply and multiply expressions. This optimization
  targets cases where the target architecture supports 2N-bit multiplication, reducing
  instruction count by replacing a complex summation chain with specialized instructions.
primer_glossary:
- term: forwprop
  definition: Forward propagation is a compiler optimization pass that duplicates
    computations to avoid recomputing them later. It can simplify code and expose
    further optimization opportunities.
- term: MULT_EXPR
  definition: A GIMPLE (GCC's intermediate representation) expression representing
    a multiplication operation.
- term: widening multiply
  definition: A multiplication operation that produces a result wider than either
    operand, typically producing a 2N-bit result from two N-bit operands.
- term: SPEC2026
  definition: A suite of benchmarks used for computer performance evaluation. SPEC
    CPU benchmarks are widely used to compare performance across different systems
    and architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/806feb8e017b243de37e4502a6fc01fb76dd1529
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

The forwprop pass now recognizes a schoolbook expansion of a 2N-bit unsigned multiply. It folds this pattern into a widening multiply plus a right shift for the high part and a plain MULT_EXPR for the low part. This optimization significantly reduces the instruction count for operations like those in SPEC2026's 750.sealcrypto_r, transforming 16 instructions down to a few, improving performance.
