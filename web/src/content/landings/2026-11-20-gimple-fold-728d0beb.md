---
project: gcc
subsystem: gimple-fold
patch_id: null
tags:
- optimization
- bugfix
- c++
commit_hash: 728d0bebb85d72e59ee8836e82ee19fa0bef8b14
source_type: github
author: Jakub Jelinek
headline: Handle large _BitInt bit-fields in __builtin_clear_padding
tldr: GCC's `__builtin_clear_padding` now handles very large `_BitInt` bit-fields,
  fixing an assertion failure for huge types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `gimple-fold` pass''s implementation of `__builtin_clear_padding`
  encountered issues with large bit-fields (especially `_BitInt` types) exceeding
  the capacity of its internal working buffer. The original logic, relying on `clear_padding_add_padding`,
  would assert when the number of bytes to clear was too large. This patch refactors
  the handling for such extreme cases: it limits `clear_padding_add_padding` to a
  smaller initial region, then enters a loop to flush and clear larger contiguous
  blocks, and finally handles the remaining bits. This prevents the assertion and
  correctly processes ov…'
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-address code representation, used as an intermediate
    language between the front-end and back-end optimization passes.
- term: gimple-fold
  definition: A GCC optimization pass that performs constant folding and other algebraic
    simplifications on GIMPLE code.
- term: __builtin_clear_padding
  definition: A GCC built-in function (introduced in GCC 11) that clears padding bits
    within a data structure, setting them to zero. This can be useful for ensuring
    consistent memory layouts or preparing data for serialization.
- term: _BitInt
  definition: A C++23 feature that allows for integer types of arbitrary bit width,
    providing more flexibility than fixed-width types like `int` or `long long`.
- term: bit-field
  definition: A data member within a struct or union that is allowed to occupy only
    a specified number of bits, which may be less than the number of bits in its data
    type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/728d0bebb85d72e59ee8836e82ee19fa0bef8b14
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This commit addresses an assertion failure in GCC's `__builtin_clear_padding` when processing extremely large bit-fields, particularly those using the `_BitInt` type. The fix modifies the handling of large bit-fields to avoid overwhelming internal buffers, ensuring that such types can be processed correctly without crashing the compiler.
