---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- pta
- compile-time
- performance
commit_hash: d56633c724c52910db102ecd314069af4243fa4d
source_type: github
author: Richard Biener
headline: Prevent PTA quadratic compile-time with artificial variables
tldr: Fixes quadratic compile-time in PTA by preventing artificial variables from
  merging.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/127758 by modifying `pta-andersen.cc`.
  The `unite` function is updated to refuse merging an artificial variable into another.
  This prevents a quadratic compile-time blowup that occurred when `ESCAPED` variables
  (which are artificial) were merged with regular variables. Such merges incorrectly
  dropped `is_artificial_var` checks, leading to `ESCAPED` information being propagated
  widely and causing excessive constraint generation and unification.
primer_glossary:
- term: PTA
  definition: Points-To Analysis. A static analysis technique used to determine, for
    each pointer in a program, the set of memory locations that the pointer might
    possibly refer to. This helps in understanding aliasing and enabling optimizations.
- term: artificial variable
  definition: In the context of PTA, an artificial variable is a placeholder used
    to represent a set of points-to information, often for intermediate or complex
    analysis results that don't directly map to a program variable.
- term: ESCAPED
  definition: In PTA, a variable is considered 'escaped' if its address is taken and
    potentially used outside its current scope, implying it might be accessed indirectly
    or via pointers.
- term: quadratic compile-time
  definition: A situation where the time taken by the compiler to compile a program
    grows proportionally to the square of the program's size or complexity. This can
    lead to very long compilation times for large projects.
- term: unify
  definition: In the context of constraint-based analysis like PTA, 'unify' refers
    to merging or equating two sets of points-to information, indicating that they
    must refer to the same set of locations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d56633c724c52910db102ecd314069af4243fa4d
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

A performance issue causing quadratic compile-time in Points-To Analysis (PTA) has been resolved by preventing the merging of artificial variables. Previously, when constraints were ordered such that an `ESCAPED` variable was unified with a regular variable, it could lead to `is_artificial_var` handling being dropped and `ESCAPED` results bleeding into unrelated analyses, causing excessive computation. Refusing to merge artificial variables into others resolves this quadratic behavior.
