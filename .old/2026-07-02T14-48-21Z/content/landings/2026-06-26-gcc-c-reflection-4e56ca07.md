---
project: gcc
subsystem: gcc/c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
- consteval
commit_hash: 4e56ca07b9eeb9dd765893b34c147ca398a57f71
source_type: github
author: Marek Polacek
headline: GCC fixes consteval-only type errors in C++ reflection splice-specs
tldr: GCC now correctly handles `consteval`-only types within C++ reflection `splice-specifier`s,
  preventing bogus errors.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `check_out_of_consteval_use_r` function, located in `reflect.cc`,
  is responsible for ensuring that `consteval` expressions are used only in constant-evaluated
  contexts. This fix addresses a false positive where `SPLICE_EXPR` nodes, which represent
  `splice-specifiers` in C++ reflection (e.g., `[:constant-expression:]`), were incorrectly
  walked by this checker. Since `splice-specifiers` are defined as `constant-expression`s
  by [expr.const.defns], their content is inherently constant-evaluated, and thus
  the check is redundant and erroneous for these nodes.
primer_general: C++ compilers ensure that certain kinds of special constant computations,
  called `consteval` functions, only happen at compile time. C++ also has a new feature
  called reflection, which allows programs to examine and manipulate their own structure
  at compile time. A `splice-specifier` is a part of reflection that lets you insert
  constant expressions into metaprograms. This commit fixes a bug where the GCC compiler
  would incorrectly report an error when `consteval`-only types were used inside these
  `splice-specifier`s. The compiler mistakenly thought these were not in a constant
  context, even though `splice-specifiers` are always meant to be constant-evaluated.
  This correction makes C++ reflection work as intended, allowing developers to use
  `consteval` types within `splice-specifier`s without getting false errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4e56ca07b9eeb9dd765893b34c147ca398a57f71
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in GCC's C++ reflection implementation where `consteval`-only types within a `splice-specifier` would incorrectly trigger a "consteval-only expressions are only allowed in a constant-evaluated context" error. The fix involves preventing the `check_out_of_consteval_use_r` function from traversing `SPLICE_EXPR` nodes, as `splice-specifiers` are inherently constant-evaluated. This prevents false positive diagnostics and improves the usability of C++ reflection features.
