---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- rtl
- loongarch
- bugfix
commit_hash: ac3b21e53c4b392e8a72b30f1c81f2339a8d6b21
source_type: github
author: Igor Shevlyakov
headline: Fix vector comparison mode in simplify-rtx for LoongArch
tldr: Corrects how vector comparisons are handled in simplify-rtx, fixing incorrect
  folding of floating-point comparisons on LoongArch.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_context::simplify_subreg` function in `simplify-rtx.cc`
  incorrectly passed `INNERMODE` (the mode of the comparison result, e.g., `V4SI`)
  as the comparison mode argument to `simplify_gen_relational`. This argument should
  be the mode of the operands (e.g., `V4SF`). For floating-point comparisons with
  integer masks, this caused `simplify_const_relational_operation` to incorrectly
  honor NaNs based on `V4SI` instead of `V4SF`. On LoongArch, this led to incorrect
  folding and subsequent issues with fwprop and bit-casts. The fix passes `VOIDmode`
  instead, allowing the mode to be derived…
primer_glossary:
- term: simplify-rtx
  definition: A GCC optimization pass that simplifies RTL (Register Transfer Language)
    expressions.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used internally
    by GCC.
- term: subreg
  definition: A subregister, which is a part of a larger register. In GCC, it's represented
    by the `subreg` construct in RTL.
- term: vector comparison
  definition: A comparison operation performed on multiple elements of a vector simultaneously.
- term: MODE
  definition: Refers to the data type or format of a value in GCC's RTL, e.g., SF
    (single-precision float), DI (double integer).
- term: LoongArch
  definition: A CPU architecture developed in China.
- term: fwprop
  definition: Forward propagation, an optimization technique where values are propagated
    through the code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ac3b21e53c4b392e8a72b30f1c81f2339a8d6b21
date: '2026-10-17'
is_stub: false
stub_reason: ''
---

An issue in GCC's `simplify-rtx` pass caused incorrect handling of subreg'd vector comparisons involving floating-point operands and integer masks. The `simplify_subreg` function incorrectly passed the mode of the comparison result instead of the mode of the operands to `simplify_gen_relational`. This led to incorrect folding of NaN behavior in operations like `unordered`, which was then propagated via fwprop and a bit-cast on LoongArch, resulting in incorrect code. The fix ensures the correct operand mode is used for the comparison.
