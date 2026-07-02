---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- rounding
- io
- formatting
commit_hash: aacccc01d2bb3dd76ee37281b9f2f04aa9c13f5c
source_type: github
author: Jerry DeLisle
headline: 'Fortran: Add EX Format Rounding for Truncated Hex Mantissa'
tldr: Implements proper rounding of the hex mantissa in Fortran's EX format, supporting
  all rounding modes and normalization.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR93727 by implementing proper rounding for truncated
  hex mantissas in Fortran's `write_ex` function. The changes involve modifying `io/write.c`
  to incorporate rounding-aware logic based on the `dtp round_status`. Carry propagation
  and integer-digit normalization are included. The commit introduces new tests `gfortran.dg/EXformat_3.F90`
  and `gfortran.dg/EXrounding.F90` to verify the functionality.
primer_general: When Fortran writes a floating-point number in hexadecimal (`EX`)
  format, it needs to handle cases where the user asks for fewer digits than the full
  precision of the number.  This commit ensures that the output is correctly rounded
  according to the specified rounding mode (e.g., rounding to the nearest even number).
  It also manages the complexities of carry propagation when rounding increases the
  value of the mantissa, potentially requiring normalization (adjusting the exponent).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aacccc01d2bb3dd76ee37281b9f2f04aa9c13f5c
date: '2026-05-24'
is_stub: false
---

This commit enhances Fortran's `EX` format to correctly round the hexadecimal mantissa when the user specifies a precision smaller than the full precision. It implements all Fortran rounding modes, including ties-to-even, ties away from zero, round up, round down, and round to zero.  The implementation also handles carry propagation and normalizes the output by adjusting the exponent when incrementing a mantissa causes it to overflow.
