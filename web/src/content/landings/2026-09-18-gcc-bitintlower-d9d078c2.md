---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- compiler bug
- bit-integer
- endianness
- powerpc
commit_hash: d9d078c216150bbe0397ded72f035c35b476e88e
source_type: github
author: Jakub Jelinek
headline: Fix big-endian separate_ext loop condition for bit integers
tldr: Corrects loop bounds for sign extension of bit integers on big-endian systems.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `separate_ext` lowerer for `_BitInt` types handles sign extension.
  On big-endian targets, the loop that copies the sign-extended bits to higher-order
  limbs had an incorrect condition. It used `_36 = _35 + 18446744073709551615` (effectively
  `_35 - 1`) and compared against 0, intending to iterate downwards from an initial
  limb index. However, the initial index and the decrement logic were mismatched,
  causing it to process incorrect limbs. This patch corrects the loop to iterate through
  the correct range of limbs, ensuring consistent behavior with little-endian targets.
primer_glossary:
- term: bit-integer lowering
  definition: The process of converting high-level arbitrary-width integer types (`_BitInt`)
    into sequences of machine-level operations or types.
- term: big-endian
  definition: A computer architecture where the most significant byte of a multi-byte
    word is stored at the lowest memory address.
- term: little-endian
  definition: A computer architecture where the least significant byte of a multi-byte
    word is stored at the lowest memory address.
- term: sign extension
  definition: The process of filling the most significant bits of a number with copies
    of the sign bit when converting it to a larger data type. This preserves the sign
    of the number.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d9d078c216150bbe0397ded72f035c35b476e88e
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in GCC's bit-integer lowering pass where the loop condition for sign extension on big-endian architectures was incorrect. The problem, observed on powerpc64-linux, caused the loop to iterate over the wrong set of limbs, leading to incorrect code generation. The fix adjusts the loop's starting point and increment logic to match the expected behavior for big-endian byte order.
