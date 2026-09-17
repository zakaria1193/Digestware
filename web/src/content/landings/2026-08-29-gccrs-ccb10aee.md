---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- rust
- compiler
- bugfix
commit_hash: ccb10aee3377495616b04aa6b004291f05f2ddf2
source_type: github
author: Arthur Cohen
headline: Correct typo in FN_VARIADIC flag name within gccrs
tldr: gccrs fixes a typo in the FN_VARIADIC flag name, ensuring correct type checking
  for variadic functions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `FN_VARIADIC_FLAG` is a crucial bitmask used in gccrs' type system
  to denote whether a function is variadic. This commit corrects a spelling mistake
  in the flag's definition, resolving potential issues in type checking, particularly
  in `TypeCheckTopLevelExternItem::visit` where it's used to determine function characteristics.
primer_glossary:
- term: variadic function
  definition: A function that can accept a variable number of arguments. In C-like
    languages, these are often indicated by an ellipsis (...) in the function signature.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ccb10aee3377495616b04aa6b004291f05f2ddf2
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

A minor typo in the `FN_VARIADIC_FLAG` name within gccrs has been corrected. The flag, used for identifying variadic functions, was renamed from `FN_VARADIC_FLAG` to `FN_VARIADIC_FLAG` in `typecheck/rust-tyty.h` and updated in `typecheck/rust-hir-type-check-implitem.cc`. This ensures proper handling of function types.
