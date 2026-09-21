---
project: gcc
subsystem: expand_mult
patch_id: null
tags:
- gcc
- optimization
- vectorization
commit_hash: 5dc4ab23e0d01a1fd20c1365bdb2de039d831ff9
source_type: github
author: Stefan Schulze Frielinghaus
headline: 'expand_mult: Look through vector mode for constant multipliers'
tldr: GCC's `expand_mult` now correctly determines shift amounts for vector constants
  by examining the scalar operand's mode.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `expmed.cc`, the `expand_mult` function, when processing a constant
  vector multiplier with a `CONST_WIDE_INT` scalar operand, now correctly inspects
  the scalar operand's mode to determine the shift amount. Previously, it would use
  the vector mode, which is incorrect for scalar calculations within the vector context.
  This change ensures that the shift amount is correctly derived from the scalar's
  actual mode, not the vector's, before passing to `expand_shift` which requires the
  vector mode. This addresses PR middle-end/127474.
primer_glossary:
- term: expand_mult
  definition: A GCC compiler function responsible for expanding multiplication operations
    into lower-level intermediate representation (IR) instructions, particularly handling
    complex cases like constant multipliers and vector types.
- term: vector mode
  definition: In GCC's intermediate representation, this refers to the data type information
    associated with vector operations, indicating that multiple elements are being
    processed in parallel.
- term: CONST_WIDE_INT
  definition: An intermediate representation constant in GCC that represents an integer
    value of arbitrary precision, which might exceed the native machine word size.
- term: shift amount
  definition: The number of positions by which the bits of a number are shifted left
    or right in a bitwise shift operation.
- term: scalar mode
  definition: The data type information for a single, non-vectorized value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5dc4ab23e0d01a1fd20c1365bdb2de039d831ff9
date: '2026-09-20'
is_stub: false
stub_reason: ''
---

GCC's `expand_mult` function has been improved to correctly handle constant vector multipliers. When the scalar operand is a `CONST_WIDE_INT`, the function now looks through the vector mode to determine the scalar mode for calculating the shift amount. This ensures accurate code generation for vector operations, as highlighted by a new test case for a bug that previously miscalculated shift amounts.
