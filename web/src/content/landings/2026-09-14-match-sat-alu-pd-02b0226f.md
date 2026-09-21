---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- gcc
- aarch64
commit_hash: 02b0226f9f8ac1face83c096b6e783e5c8956f6a
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize unsigned constant-clamp truncation'
tldr: GCC can now optimize unsigned saturating truncation resulting from clamping
  a signed value to the bounds of a narrower unsigned type.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` pattern matcher now identifies unsigned saturating
  truncation that arises from clamping a signed value to the range of a narrower unsigned
  type. This new pattern, `integer_constant_clamp`, handles nested MIN and MAX operations
  irrespective of their order. It specifically targets cases where the clamping results
  in a value within the unsigned type's range, allowing replacement with efficient
  instructions like `UQXTN` on AArch64. The match requires an exact zero lower bound
  and the maximum upper bound for the unsigned type, with a single use of the outer
  clamp.
primer_glossary:
- term: unsigned saturating truncation
  definition: A conversion to a narrower unsigned integer type where the result is
    clamped to the maximum value of the target type if the original value exceeds
    it. This prevents overflow by capping the result at the highest representable
    value for the unsigned type.
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
url: https://github.com/gcc-mirror/gcc/commit/02b0226f9f8ac1face83c096b6e783e5c8956f6a
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

GCC's `match-sat-alu.pd` pattern matcher has been extended to recognize unsigned saturating truncation when a signed value is clamped to the range of a narrower unsigned type. This optimization handles nested MIN and MAX operations in either order and can replace complex sequences with a single `uqxtn` instruction on architectures like AArch64, as shown in an example.
