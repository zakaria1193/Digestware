---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler
commit_hash: 055a2eca6fe2efed84b7287536cd144f789de66b
source_type: github
author: Marek Polacek
headline: 'c++/reflection: Tweak reflection_function_template_p'
tldr: Improves C++ reflection by using a narrower type check for function templates.
why_it_matters: Refines the C++ reflection mechanism, potentially leading to more
  accurate and efficient reflection capabilities.
impact_score: 5
impact_rationale: Refactoring of internal reflection mechanisms.  Likely a bugfix
  of some sort, but probably narrow impact.
performance_win: false
breaking_change: false
outcome: committed
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/055a2eca6fe2efed84b7287536cd144f789de66b
date: '2026-04-16'
---

This commit modifies the `reflection_function_template_p` function to use `DECL_FUNCTION_TEMPLATE_P` instead of `really_overloaded_fn` for a more precise check. It also adjusts the parameter type to `const_tree` and unwraps BASELINKs and OVERLOADs.
