---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- bugfix
commit_hash: b20d26da1d10536fd3e5448f6b467f62ecdb4e73
source_type: github
author: Jakub Jelinek
headline: expmed avoids undefined behavior with bit-field operations.
tldr: Compiler avoids undefined behavior when calculating bit-field masks for large
  sizes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `store_split_bit_field` function in `expmed.cc` previously used
  `HOST_WIDE_INT_1` for bit shifts and subtractions when computing masks for bit fields.
  For `thissize` values of 63, this could lead to invoking undefined behavior due
  to overflow on subtraction after a left shift of 63 bits on a `long` type. By changing
  to `HOST_WIDE_INT_1U`, the operations are performed on unsigned integers, which
  have well-defined behavior for these bitwise operations, thus removing the UB.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b20d26da1d10536fd3e5448f6b467f62ecdb4e73
date: '2026-11-28'
is_stub: false
stub_reason: ''
---

This change in the expmed component fixes undefined behavior that occurred when calculating bit-field masks for sizes up to 63 bits. Specifically, using left shifts and subtractions with 64-bit integers could invoke undefined behavior. The fix replaces the problematic integer types with unsigned equivalents, ensuring correct mask generation and removing the UB.
