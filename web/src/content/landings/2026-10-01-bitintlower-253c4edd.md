---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- optimization
- compiler bug
commit_hash: 253c4edd1d5d20d562ca89329d9664812538f0a5
source_type: github
author: Jakub Jelinek
headline: Fix lowering of bswapg/bitreverseg for _BitInt types
tldr: GCC fixes miscompilation of _BitInt types in bswapg/bitreverseg operations by
  correcting how partial limbs are handled.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bitintlower` pass, specifically handling `bswapg` and `bitreverseg`
  operations on `_BitInt` types, had an issue with `handle_operand`. When `fold_const_call`
  did not optimize internal functions with propagated constants, the lowering produced
  a call to `.BITREVERSE(1)` with an unsigned `_BitInt(129)`. This led to incorrect
  handling of partial limbs, where optimizations assuming constant access to the partial
  limb in straight-line code were misapplied. The patch corrects the logic to ensure
  that partial limbs are properly accounted for, even in loops, by adjusting how the
  `m_var_msb` flag…
primer_glossary:
- term: _BitInt
  definition: A GCC extension for arbitrary-precision integer types, allowing developers
    to specify integers of any bit width.
- term: lowering
  definition: The process of transforming higher-level intermediate representations
    (IR) or operations into simpler ones, typically closer to machine instructions.
- term: partial limb
  definition: In arbitrary-precision arithmetic, a 'limb' is a machine word used to
    represent a larger number. A 'partial limb' refers to the most significant limb
    of such a number, which may not be fully utilized.
- term: fold_const_call
  definition: A GCC optimization function that attempts to evaluate calls to internal
    functions with constant arguments at compile time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/253c4edd1d5d20d562ca89329d9664812538f0a5
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

This commit addresses a miscompilation issue in GCC related to the lowering of `bswapg` and `bitreverseg` operations for `_BitInt` types. The problem stemmed from incorrect handling of partial limbs during the lowering process, where optimizations intended for constant indices failed to account for the full bit-reversal logic. The fix ensures that all necessary bits, including those in partial limbs, are correctly processed, preventing incorrect results.
