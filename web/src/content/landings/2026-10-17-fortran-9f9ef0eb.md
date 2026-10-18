---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- coarray
- bugfix
commit_hash: 9f9ef0ebf25764537f6f879fb48df82589829619
source_type: github
author: Jerry DeLisle
headline: Fortran collective subroutines pass ERRMSG= by reference
tldr: Fixes libgfortran to pass the ERRMSG variable by reference for coarray collective
  subroutines, preventing crashes.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `trans-intrinsic.cc` file's `conv_co_collective` function has been
  updated to pass the `errmsg` argument by reference using `gfc_conv_expr_reference`.
  Previously, it was passed by value. This change corrects how error messages are
  handled for libgfortran's coarray collective subroutines, ensuring the library receives
  a valid pointer to the error message buffer.
primer_glossary:
- term: coarray
  definition: A Fortran language feature that allows for parallel programming by providing
    a mechanism for images (concurrent processes) to directly access data on other
    images.
- term: ERRMSG=
  definition: A Fortran standard argument for certain intrinsic procedures, including
    coarray collectives, used to return error messages. It expects a character variable.
- term: by reference
  definition: Passing an argument to a function such that the function receives the
    memory address of the variable, allowing it to modify the original variable.
- term: by value
  definition: Passing an argument to a function such that the function receives a
    copy of the variable's value. Modifications within the function do not affect
    the original variable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9f9ef0ebf25764537f6f879fb48df82589829619
date: '2026-10-17'
is_stub: false
stub_reason: ''
---

Coarray collective subroutines in Fortran, such as CO_BROADCAST and CO_REDUCE, incorrectly passed the ERRMSG= variable by value. This led to the library receiving the string length instead of a pointer, causing crashes when the ERRMSG variable was set, for example, when an image in a team stopped. The fix ensures ERRMSG= is passed by reference, aligning with how image control statements handle such variables.
