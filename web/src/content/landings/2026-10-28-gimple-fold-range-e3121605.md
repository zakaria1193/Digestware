---
project: gcc
subsystem: gimple-fold-range
patch_id: null
tags:
- optimization
- constants
- gimple
commit_hash: e3121605d2a5507b4ec456ad28f133c4f11f67b6
source_type: github
author: Jakub Jelinek
headline: Handle STRING_CSTs and RAW_DATA_CSTs in range_from_readonly_var
tldr: Improves range folding to correctly handle string and raw data constants.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `gimple-range-fold.cc`, specifically within `ctor_ref_range::accumulate_range`
  and `ctor_ref_range::accumulate_range_from_component_ref`, to support `STRING_CST`
  and `RAW_DATA_CST` in addition to `CONSTRUCTOR`. This is relevant for folding constant
  array initializers into single constants. For these types, the index range is checked
  against the byte representation, and if a match occurs, a `wide_int` is created
  via union, avoiding intermediate `build_int_cst` calls. The code now handles potential
  sign or zero extension for `CHAR_BIT` precision integral types derived from…
primer_glossary:
- term: gimple-fold-range
  definition: A GCC optimization pass that folds constant values within a specified
    range, often applied to array initializers or string literals.
- term: STRING_CST
  definition: An internal GCC representation for a string constant.
- term: RAW_DATA_CST
  definition: An internal GCC representation for a constant block of raw data, often
    used for embedded data or large initializers.
- term: wide_int
  definition: An arbitrary-precision integer type used within GCC for representing
    integer constants that may exceed the native machine word size.
- term: CHAR_BIT
  definition: A C preprocessor macro defining the number of bits in a byte.
- term: CPP_EMBED
  definition: A C++ preprocessor directive that allows embedding raw binary data into
    a program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e3121605d2a5507b4ec456ad28f133c4f11f67b6
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit enhances the `range_from_readonly_var` function in `gimple-fold-range` to properly handle `STRING_CST` and `RAW_DATA_CST` operands. Previously, these types were not fully supported, potentially leading to incorrect folding of constants that represent string literals or embedded raw data. The changes allow the compiler to accurately interpret and fold these constant types, improving optimization opportunities for string initializers and embedded data.
