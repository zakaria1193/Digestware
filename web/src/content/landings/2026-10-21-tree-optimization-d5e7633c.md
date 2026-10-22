---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- unaligned access
commit_hash: d5e7633c5a4e91f2c51cc12ca4995e51179ab96e
source_type: github
author: Richard Biener
headline: tree-optimization/128052 - miscompilation of unaligned loads from covered
  stores
tldr: Fixes miscompilation of unaligned loads from constant stores by accurately calculating
  bit offsets.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SSA SCCVN (Value Numbering for Sparse Conditional Constant Propagation)
  pass, specifically within `vn_reference_lookup_3`, had a bug in handling loads that
  were fully covered by a single constant store. The calculation of the bit range
  for such loads did not properly account for the bit remainder `(offseti - offset2i)
  % BITS_PER_UNIT`. This led to incorrect checks on the encoded buffer size, potentially
  causing a miscompilation where unaligned loads (especially those involving large
  `_BitInt` types spanning across byte boundaries) would drop bits from the loaded
  value because the necessar…
primer_glossary:
- term: SCCVN (Sparse Conditional Value Numbering)
  definition: An optimization technique that uses value numbering to determine constant
    values and propagate them through the program, even in the presence of conditional
    branches.
- term: unaligned load
  definition: A memory read operation where the address of the data is not aligned
    to a natural boundary of the data type (e.g., reading a 4-byte integer at an address
    not divisible by 4).
- term: constant store
  definition: Storing a fixed, known value into memory during compilation or runtime.
- term: _BitInt
  definition: A GCC extension for arbitrary-precision integers, allowing users to
    specify integers of any bit width.
- term: bit remainder
  definition: The fractional part of a bit offset when measured in units of bytes.
    For example, an offset of 3 bits into a byte has a bit remainder of 3.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d5e7633c5a4e91f2c51cc12ca4995e51179ab96e
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This commit corrects a miscompilation issue related to unaligned loads from memory locations covered by a single constant store. The previous implementation in `vn_reference_lookup_3` incorrectly calculated the bit span for such loads, especially when they started at a non-byte-aligned offset. This could lead to bits being dropped from the loaded value if the required data extended beyond the encoded buffer. The fix adjusts the buffer size and accurately accounts for the bit remainder and total span, ensuring correct data retrieval and preventing bit truncation.
