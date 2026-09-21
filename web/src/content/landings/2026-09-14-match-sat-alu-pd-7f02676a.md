---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
commit_hash: 7f02676a414e4a96c498c0b3e58487aca3c45185
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize signed constant-clamp truncation'
tldr: GCC can now optimize signed saturating truncation that results from clamping
  a value to the bounds of a narrower signed type.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` pattern matcher has been enhanced to recognize
  a specific form of signed saturating truncation. This form arises when a value is
  effectively clamped to the minimum and maximum representable values of a narrower
  signed type. The new patterns cover both `MIN(MAX(X, T_MIN), T_MAX)` and `MAX(MIN(X,
  T_MAX), T_MIN)` structures, targeting cases where the inner and outer clamp operations
  result in saturation to the target type's bounds. This allows for direct mapping
  to specialized instructions like `SQXTN` on architectures like AArch64, reducing
  instruction counts.
primer_glossary:
- term: signed saturating truncation
  definition: A conversion to a narrower signed integer type where the result is clamped
    to the minimum or maximum representable value of the target type if the original
    value falls outside that range. This prevents overflow by capping the result.
- term: clamping
  definition: The process of restricting a value to a specified range. In this context,
    it means ensuring a value does not exceed the minimum or maximum representable
    values for a given data type.
- term: MIN/MAX operations
  definition: Functions that return the smaller (MIN) or larger (MAX) of two input
    values. They are often used in sequence to implement clamping.
- term: pattern matcher
  definition: A component within a compiler that identifies specific sequences of
    intermediate representation (IR) operations that can be replaced by more efficient
    instructions or simpler IR forms. This is crucial for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f02676a414e4a96c498c0b3e58487aca3c45185
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

GCC's `match-sat-alu.pd` pattern matcher now recognizes signed saturating truncation that occurs when a value is clamped to the bounds of a narrower signed integer type. This optimization handles both orders of MIN and MAX operations used for clamping, enabling more efficient code generation. An AArch64 example shows a significant reduction from multiple instructions to a single `sqxtn` instruction.
