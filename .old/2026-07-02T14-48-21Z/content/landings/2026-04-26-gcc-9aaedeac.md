---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c
- typeof
- bugfix
commit_hash: 9aaedeaced055efe5041004e0643f4f3127c6ce9
source_type: github
author: Martin Uecker
headline: 'C: Argument expressions may be evaluated too often by typeof.'
tldr: Fixes a bug where argument expressions within `typeof` were evaluated multiple
  times.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a bug in `c-decl.cc` related to the handling
  of `typeof` expressions. When multiple declarators are present in a declaration
  and `typeof` is used to specify the type, the argument expression within `typeof`
  could be redundantly evaluated. The fix employs `save_expr` to ensure single evaluation,
  preventing potential side effects.
primer_general: '`typeof` is a C language feature that allows you to determine the
  type of an expression at compile time. This commit fixes a bug where, if you used
  `typeof` in a complex declaration, the expression inside the `typeof` might be evaluated
  more than once. This could lead to unexpected behavior if the expression had side
  effects, such as modifying a variable. The fix ensures that the expression is evaluated
  only once, as intended.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9aaedeaced055efe5041004e0643f4f3127c6ce9
date: '2026-04-26'
---

When using `typeof` with multiple declarators in a declaration, argument expressions within `typeof` could be evaluated multiple times. This commit fixes the issue by adding a `save_expr`, which ensures that the expression is evaluated only once. This prevents unexpected side effects and ensures the program behaves as intended.
