---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- templates
- bugfix
commit_hash: f78cb5ae260a88d9499d1496f3ba6fd54dd04bac
source_type: github
author: Marek Polacek
headline: Fix reflection on dependent class templates.
tldr: Fixes a bogus error when reflecting on dependent class templates in C++.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The issue occurred in `tsubst_qualified_id` within `pt.cc`. The code
  previously checked `!name_lookup_p` and gave an "instantiation yields a type" error.  The
  fix renames `name_lookup_p` to `reflecting_p`, checks `!reflecting_p` instead, and
  suppresses the error when `reflecting_p` is true.  The call to `tsubst_qualified_id`
  is also adjusted in `tsubst_expr` for the `REFLECT_EXPR` case.
primer_general: Templates in C++ allow writing code that can work with different data
  types without having to be rewritten for each type. Reflection allows programs to
  inspect and manipulate their own structure at compile time.  Dependent types are
  types that depend on template parameters. This commit fixes a bug in the C++ reflection
  implementation that prevented reflection on dependent class templates, enabling
  more advanced metaprogramming scenarios.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f78cb5ae260a88d9499d1496f3ba6fd54dd04bac
date: '2026-04-22'
---

The compiler was incorrectly issuing an error when reflecting on dependent class templates like `^^Cls<T>::template Inner` because it couldn't determine in advance what it would substitute into. This commit relaxes the error check when taking a reflection, allowing reflection of the `TEMPLATE_DECL` and resolving the issue. This affects code using C++ reflection with dependent class templates.
