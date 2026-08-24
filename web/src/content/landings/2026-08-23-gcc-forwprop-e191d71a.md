---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- gcc
- documentation
- refactor
commit_hash: e191d71a0627e0ba87c4b002a5fb826f181602ef
source_type: github
author: Andrea Pinski
headline: 'forwprop: Clarify comment on tree_to_uhwi safety'
tldr: Updates a comment to accurately reflect why tree_to_uhwi is safe.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `long_mul_set_summand` function in `tree-ssa-forwprop.cc` uses
  `tree_to_uhwi` to convert a tree operand to an unsigned `hwint` type. The safety
  of this conversion, particularly concerning potential shifts, is dependent on the
  operand's value relative to the target type's precision. This change revises the
  accompanying comment to explicitly state that the conversion is safe because the
  operand's value is guaranteed to be less than `TYPE_PRECISION`, thus avoiding overflow
  or unexpected behavior.
primer_glossary:
- term: tree_to_uhwi
  definition: A GCC internal function that converts a value from the compiler's intermediate
    representation (tree) to an unsigned hardware integer type.
- term: TYPE_PRECISION
  definition: A macro or constant in GCC that represents the number of bits in the
    precision of a given data type.
- term: unsigned hwint
  definition: An unsigned integer type that directly maps to a hardware-supported
    integer size, often used internally by the compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e191d71a0627e0ba87c4b002a5fb826f181602ef
date: '2026-08-23'
is_stub: true
stub_reason: low_score
---

This commit updates a comment in `tree-ssa-forwprop.cc` to provide a clearer explanation of why the `tree_to_uhwi` function is considered safe. The comment now emphasizes that the operation is safe because the result is always less than `TYPE_PRECISION`, providing better context for developers reading the code.
