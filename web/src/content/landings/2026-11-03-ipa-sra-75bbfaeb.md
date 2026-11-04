---
project: gcc
subsystem: ipa-sra
patch_id: null
tags:
- optimization
- IPA
- analysis
commit_hash: 75bbfaeb8ba0ad95e7c0fb306790ca71dbb55bbd
source_type: github
author: Martin Jambor
headline: Formal parameter index check added to IPA-SRA
tldr: IPA-SRA pass now correctly checks if formal parameter indices fit in an unsigned
  char.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ipa-sra.cc` file implements the IPA-SRA optimization pass. This
  pass involves analyzing function calls and their arguments. For efficiency, the
  indices of formal parameters passed as arguments are stored in an `unsigned char`
  array, limiting each index to 255. The `scan_expr_access` function, which processes
  accesses to parameters, previously lacked a check to ensure the parameter index
  fits within `unsigned char`. This commit adds the missing check, resolving PR ipa/128106.
primer_glossary:
- term: IPA-SRA
  definition: Interprocedural Analysis - Scalar Replacement of Aggregates. A GCC optimization
    pass that analyzes function calls to replace aggregate memory accesses with scalar
    variables where possible.
- term: formal parameter
  definition: A variable declared in a function definition that accepts a value when
    the function is called.
- term: unsigned char
  definition: An integer data type that can hold values from 0 to 255. It is often
    used for space efficiency when storing small integers.
- term: call argument
  definition: A value passed from a calling function to a called function.
discussion_id_link: github:gcc-mirror/gcc#128106
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/75bbfaeb8ba0ad95e7c0fb306790ca71dbb55bbd
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

The Interprocedural Analysis Scalar Replacement of Aggregates (IPA-SRA) pass has been updated to include a missing check for formal parameter indices. These indices are stored as `unsigned char` to save space, as they are packed into an array of up to seven per call argument. The `scan_expr_access` function now verifies that the index fits within an `unsigned char`, fixing a bug identified in PR 128106 and ensuring correct handling of function arguments during analysis.
