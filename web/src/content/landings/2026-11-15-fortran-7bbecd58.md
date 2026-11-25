---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler error
- bugfix
commit_hash: 7bbecd581aa6f87c68d9d1088ee97b1d7f96005a
source_type: github
author: Jerry DeLisle
headline: Fortran ICE for labeled END statement after CONTAINS.
tldr: Fixes an internal compiler error in Fortran related to labeled END statements
  after CONTAINS blocks.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc/fortran/parse.cc` function `accept_statement` has been updated
  to correctly handle labeled `END`, `END MODULE`, and `END SUBMODULE` statements
  following a `CONTAINS` section. Previously, the label associated with such an `END`
  statement could be lost or mishandled, especially in main programs where the host
  symbol is null. This led to an ICE due to a null pointer dereference or incorrect
  label handling, particularly when the fix for PR126909 was applied. The change ensures
  the label is defined in the host namespace with its correct source location using
  `gfc_define_st_label`, and als…
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A fatal error encountered by the compiler during
    its execution, typically indicating a bug in the compiler itself.
- term: CONTAINS
  definition: A Fortran keyword used to introduce a section of internal procedures
    (subroutines or functions) within a main program, module, or external procedure.
- term: label
  definition: In Fortran, a numeric identifier that can be used to branch to a specific
    statement using a `GOTO` statement or to reference a statement, such as an `END`
    statement.
- term: namespace
  definition: A declarative region that provides a scope to the identifiers (names
    of types, functions, variables, etc.) inside it. In this context, it refers to
    the symbol table management within the Fortran parser.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7bbecd581aa6f87c68d9d1088ee97b1d7f96005a
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

An internal compiler error (ICE) occurred in GCC's Fortran front-end when a labeled `END` statement appeared after a `CONTAINS` section. This issue arose because a previous fix for another bug moved labels to the host scope without proper source location information. For main programs without an explicit name, this caused an ICE when attempting to branch to such a label. The fix ensures labels are correctly defined in the parent scope with source locations, also diagnosing duplicate labels.
