---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- floating-point
- bugfix
- ilp32
commit_hash: c5eff89d859f98bf9e896eff22a65d1bbf0c5104
source_type: github
author: Jerry DeLisle
headline: 'Fortran: Fix EX format kind=8 output on ILP32 targets'
tldr: The Fortran compiler now correctly outputs hexadecimal format for kind=8 real
  numbers on 32-bit systems, resolving a truncation issue.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR93727, concerning Fortran's `EX` format output
  within `libgfortran`. The issue stems from incorrect handling of `kind=8` real numbers
  (double precision) on ILP32 architectures. Specifically, `get_float_hex_string`
  used `unsigned long` (32-bit) for `frac_part`, leading to truncation. The fix replaces
  this with `GFC_UINTEGER_8` (64-bit), ensuring sufficient precision. Affected files
  include `libgfortran/io/write_float.def`.
primer_general: In Fortran, real numbers can have different precisions, specified
  by the `kind` parameter. The `EX` format is used to output a real number in hexadecimal
  format. This commit fixes a bug in the Fortran compiler that caused incorrect output
  when printing double-precision (`kind=8`) real numbers in hexadecimal format on
  32-bit systems. The issue was due to the internal representation of the number being
  truncated, leading to inaccurate output. The fix ensures that the full precision
  of the number is preserved when generating the hexadecimal representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c5eff89d859f98bf9e896eff22a65d1bbf0c5104
date: '2026-05-24'
is_stub: false
---

The Fortran compiler's `EX` format output for `kind=8` real numbers on 32-bit targets was truncating the mantissa due to the use of a 32-bit integer to store the 52-bit mantissa. This commit fixes this by using `GFC_UINTEGER_8`, a guaranteed 64-bit integer type, to store the mantissa. This ensures correct hexadecimal output and avoids raising `IEEE_INVALID_FLAG` on ARM hardware.
