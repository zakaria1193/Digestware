---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- interoperability
- fortran2023
commit_hash: a6b2fe7f54bffc4006bee4b20dd788c0a81a9e2e
source_type: github
author: Sandra Loosemore
headline: 'Fortran Gains New Intrinsic: c_f_strpointer for String Pointers'
tldr: Adds the `c_f_strpointer` intrinsic to Fortran, enabling interoperability with
  C string pointers as part of Fortran 2023 support.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces `c_f_strpointer` to the Fortran front end, specifically
  in `check.cc`, `intrinsic.cc`, and `trans-intrinsic.cc`.  It involves adding a new
  `gfc_check_c_f_strpointer` function for semantic analysis, a new `GFC_ISYM_C_F_STRPOINTER`
  symbol, and a `conv_isocbinding_subroutine_strpointer` function for code generation.
  The changes also include modifications to `iso-c-binding.def` and updates to the
  documentation in `intrinsic.texi`.
primer_general: This commit introduces a new feature to Fortran that improves its
  ability to work with C code.  Modern Fortran has an "ISO C Binding" feature that
  allows Fortran code to directly call functions written in C, and vice versa. The
  new `c_f_strpointer` intrinsic makes it easier for Fortran programs to manipulate
  character strings that are managed by C code, which is important when interfacing
  with external C libraries. This brings Fortran closer to full compliance with the
  Fortran 2023 standard.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a6b2fe7f54bffc4006bee4b20dd788c0a81a9e2e
date: '2026-05-28'
is_stub: false
---

The `c_f_strpointer` intrinsic has been added to Fortran, implementing a missing feature from the Fortran 2023 standard. This intrinsic allows Fortran programs to interoperate with C code that uses string pointers, by providing a way to associate a Fortran character variable with the target of a C string pointer. This enhancement expands Fortran's ability to work with C libraries.
