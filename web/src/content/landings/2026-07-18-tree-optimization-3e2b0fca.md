---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- arm
commit_hash: 3e2b0fcab75527bae01a0e22fe993addcf8475d9
source_type: github
author: Torbjörn SVENSSON
headline: Fold constant conditional selects for integral types.
tldr: 'Optimize conditional selects of the form (x == CST) ? x : CST to CST.'
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This commit enhances the tree-ssa-instr-reduce pass by introducing
  a new pattern in `match.pd` to fold conditional selects involving constants. It
  targets expressions like `(x == C) ? x : C` and `(x != C) ? C : x` for integral
  types. The folding transforms these into a constant `C`, recognizing that if `x`
  equals `C`, the result is `C`, and if `x` does not equal `C`, the other branch yields
  `C` anyway. This addresses specific ARM MVE predicate-to-vector mask conversions.'
primer_glossary:
- term: conditional select
  definition: An expression that chooses between two values based on a condition.
    In GCC's Gimple intermediate representation, this is often represented by `GIMPLE_COND_EXPR`
    or similar constructs.
- term: Integral types
  definition: Data types that represent whole numbers, such as integers (`int`, `long`)
    and their unsigned counterparts. This excludes floating-point types.
- term: ARM MVE
  definition: ARM's Mạnh Vector Extension, a SIMD (Single Instruction, Multiple Data)
    instruction set extension for Cortex-M processors designed for digital signal
    processing and general-purpose computing tasks.
- term: Predicate
  definition: In SIMD/vector processing, a mechanism often used to control which lanes
    of a vector operation are active. A predicate can be a bitmask or a set of boolean
    flags.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3e2b0fcab75527bae01a0e22fe993addcf8475d9
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

This change allows the compiler to fold conditional select expressions where the condition compares a variable against a constant. Specifically, it handles cases like `(x == CST) ? x : CST` and `(x != CST) ? CST : x`, simplifying them to `CST` for integral scalar and vector types. This optimization catches patterns previously converted from bitwise masks, including some ARM MVE specific forms, leading to more efficient code.
