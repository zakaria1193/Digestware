---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler
- standard conformance
commit_hash: b6de3eb243c91b6503d95cc1942f55378ae6cbae
source_type: github
author: Jerry DeLisle
headline: 'Fortran: Fix character function invocation as stop code'
tldr: Fortran compiler now correctly handles character functions used as STOP codes,
  per F2008 standard.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Addresses PR fortran/126018 by modifying `gfc_match_stopcode` in `match.cc`
  and `gfc_resolve_code` in `resolve.cc`. The change relaxes the error check in `gfc_match_stopcode`
  to not error if the STOP code expression's type is unknown, deferring the check
  to `gfc_resolve_code`. The latter function is updated to add specific checks for
  `EXEC_STOP` and `EXEC_ERROR_STOP` associated with character expressions.
primer_glossary:
- term: STOP code
  definition: An optional integer or character expression used in a Fortran STOP statement
    to provide a message or status code when program execution terminates.
- term: Character function
  definition: In Fortran, a function that returns a character string value.
- term: gfortran
  definition: The GNU Fortran compiler, part of the GNU Compiler Collection (GCC).
- term: F2008
  definition: Fortran 2008, a revision of the Fortran programming language standard.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b6de3eb243c91b6503d95cc1942f55378ae6cbae
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

The Fortran compiler (gfortran) has been fixed to correctly handle character functions invoked as stop codes, aligning with the F2008 standard. Previously, the compiler would reject valid character function invocations, leading to incorrect error checking. This patch adjusts the matching and resolving logic to allow these constructs and checks them later in the resolution phase.
