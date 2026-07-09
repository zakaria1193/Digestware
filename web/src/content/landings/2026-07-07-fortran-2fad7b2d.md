---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler
- operator
- block construct
commit_hash: 2fad7b2d4d4ae51bb65a23d45e883e07beae624c
source_type: github
author: Harald Anlauf
headline: 'Fortran: Fix user-defined operator resolution in named BLOCKs (PR126127)'
tldr: Correctly resolves user-defined operators within named `BLOCK` constructs in
  Fortran.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/fortran/interface.cc`, the `find_symtree0` and `gfc_find_sym_in_symtree`
  functions have been updated to improve symbol resolution for user-defined operators
  within named `BLOCK` constructs. Specifically, `gfc_find_sym_in_symtree` now includes
  a check against the user-defined operator list when the symbol being looked up pertains
  to a function, ensuring these operators are correctly found when they are used within
  the scope of a named `BLOCK`.
primer_glossary:
- term: user-defined operators
  definition: In Fortran, procedures that can be invoked using operator syntax (e.g.,
    `a + b`, where `+` is defined by a procedure) rather than function call syntax.
- term: named BLOCK
  definition: A Fortran construct that allows a block of code to be named and scoped,
    similar to a subroutine or module procedure, providing a way to group statements
    and declare local variables.
- term: symbol resolution
  definition: The process by which a compiler determines the meaning and location
    of identifiers (symbols) used in the source code, such as variables, functions,
    and operators.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2fad7b2d4d4ae51bb65a23d45e883e07beae624c
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This commit resolves an issue where user-defined operators were not being correctly resolved within named `BLOCK` constructs in Fortran code. The fix in `interface.cc` ensures that the compiler correctly searches user-defined operator lists when a symbol refers to a function within these constructs. A new test case verifies the correction.
