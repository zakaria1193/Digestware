---
project: gcc
subsystem: internal-fn
patch_id: null
tags:
- optimization
- integer
- bugfix
commit_hash: e1167aef8d7477fe3aa152cdc61a62b92a1c4f3b
source_type: github
author: Kyrylo Tkachov
headline: Fix widening CLMUL for narrow _BitInt types
tldr: Corrected CLMUL widening logic for narrow _BitInt types to accurately compute
  the high half of the product.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `expand_CLMUL_WIDEN` intrinsic expansion was not correctly calculating
  the high half of a widening CLMUL operation when the result's precision exceeded
  the operand type's precision, specifically for narrow `_BitInt` types. The shortcut
  `if (mode_fits_bitwise_p(TARGET_MODE, CLMUL_RES_MODE))` was incorrectly applied,
  leading to `hi` being zeroed out. The fix correctly computes `hi` as `(product >>
  bits_precision)` when the product requires more bits than the operand type can hold,
  addressing PR128111.
primer_glossary:
- term: _BitInt
  definition: A C++23 feature allowing arbitrary-precision integers. `_BitInt(N)`
    defines an integer type with exactly N bits.
- term: CLMUL
  definition: Carry-Less Multiplication. A bitwise multiplication operation where
    carries are ignored. It's often used in cryptography and error correction codes.
- term: intrinsic
  definition: A function that is implemented directly by the compiler, often mapping
    to a specific machine instruction. Intrinsic functions provide low-level access
    to hardware capabilities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e1167aef8d7477fe3aa152cdc61a62b92a1c4f3b
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in the `expand_CLMUL_WIDEN` function where it incorrectly handled the high half of a widening carry-less multiplication (CLMUL) for narrow `_BitInt` types. Previously, it took a shortcut assuming the entire product fit within the operand's mode, resulting in zero for the high half when bits above the type's precision were involved. The fix ensures the high half is correctly computed by shifting the product right by the type's precision when necessary.
