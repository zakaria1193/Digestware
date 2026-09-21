---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
commit_hash: 0c6332c9fff5a0cb3dcf541e2b0f9c82c61ea182
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize signed saturation clamps'
tldr: GCC now optimizes signed saturating additions and subtractions that involve
  clamping a wider intermediate result.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` pattern matcher now recognizes signed saturating
  addition (`.SAT_ADD`) and subtraction (`.SAT_SUB`) operations that use a wider intermediate
  type, which is then clamped to the result type's bounds. The patterns handle both
  `MIN`/`MAX` nesting orders, requiring the intermediate to be strictly wider than
  the result to ensure arithmetic precision before clamping. The outer clamp must
  have a single use to facilitate replacement. This optimization is demonstrated with
  an AArch64 example showing the reduction of a complex sequence involving `adds`,
  `cmp`, and `csel` to a sing…
primer_glossary:
- term: signed saturating addition
  definition: An addition operation where, if the sum exceeds the maximum or minimum
    representable value for the signed result type, the result is clamped to that
    maximum or minimum value. This prevents overflow by capping the result.
- term: signed saturating subtraction
  definition: A subtraction operation where, if the difference exceeds the maximum
    or minimum representable value for the signed result type, the result is clamped
    to that maximum or minimum value. This prevents overflow by capping the result.
- term: widened
  definition: An operation where the intermediate result is stored in a data type
    that has more bits (higher precision) than the final result type. This is often
    done to perform calculations without overflow before clamping or converting to
    the final narrower type.
- term: clamping
  definition: The process of restricting a value to a specified range. In this context,
    it means ensuring a value does not exceed the minimum or maximum representable
    values for a given data type.
- term: pattern matcher
  definition: A component within a compiler that identifies specific sequences of
    intermediate representation (IR) operations that can be replaced by more efficient
    instructions or simpler IR forms. This is crucial for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0c6332c9fff5a0cb3dcf541e2b0f9c82c61ea182
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

GCC's `match-sat-alu.pd` pattern matcher has been updated to recognize signed saturating addition and subtraction operations where a wider intermediate result is clamped to the bounds of the final result type. This optimization handles both orders of MIN and MAX operations and allows for direct replacement with instructions like `SQADD` on AArch64, significantly simplifying code generation.
