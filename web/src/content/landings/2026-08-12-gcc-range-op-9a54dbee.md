---
project: gcc
subsystem: gcc/range-op
patch_id: null
tags:
- optimization
- range analysis
- bitwise operations
commit_hash: 9a54dbee11c890546b0bad8e3022296f02449181
source_type: github
author: Daniel Barboza
headline: Infer non-zero result for bitwise OR when operands are known to be different.
tldr: Compiler now deduces `A | B` is non-zero if `A` is not equal to `B`.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Adds a `VREL_NE` relation effect to `operator_bitwise_or::op1_op2_relation_effect`
  in `range-op.cc`. When `op1 != op2` is established, the analysis now infers that
  `op1 | op2` is non-zero. This affects range-based analysis, potentially enabling
  further optimizations like constant propagation or simplification of conditional
  branches that depend on the result of a bitwise OR.
primer_glossary:
- term: Range analysis
  definition: A compiler optimization technique that determines the possible range
    of values a variable can hold during program execution. This information is used
    to prove properties about the code and enable further optimizations.
- term: Relation effect
  definition: In range analysis, this describes how an operation affects the relationship
    between its operands and their possible values, providing constraints for the
    analysis.
- term: VREL_NE
  definition: A relation indicating that two values are not equal.
- term: bit_ior
  definition: The GCC internal representation for the bitwise OR operation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9a54dbee11c890546b0bad8e3022296f02449181
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This commit enhances the range analysis optimization pass by introducing a new relation effect for the bitwise OR operation (`bit_ior`). When the compiler can determine that the two operands of a bitwise OR are not equal (`A != B`), it can now infer that the result of `A | B` will always be non-zero. This allows for more aggressive optimizations in subsequent passes by providing tighter range information.
