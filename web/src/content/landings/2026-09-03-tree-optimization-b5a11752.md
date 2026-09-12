---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- performance
- tree-optimization
- loop optimization
commit_hash: b5a11752dcb093fd0f9ce4c205a14acf9dbe702a
source_type: github
author: Kyrylo Tkachov
headline: Tree optimizer uses reference parameter bounds in trap analysis.
tldr: Tree optimizer now uses object bounds for reference parameters, improving loop
  invariant load motion and reducing cycles.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree_could_trap_p` analysis in `tree-eh.cc` has been enhanced
  to utilize object size information for `REFERENCE_TYPE` parameters, analogous to
  how it already handles the `this` parameter. A new function `whole_object_param_size`
  consolidates the logic for querying parameter object bounds. This change allows
  LIM to move loads that were previously held back by the inability to prove the size
  of referenced objects, enabling optimizations like moving loads to loop preheaders.
  The object bound is applied only to rvalues to avoid issues with potential `const_cast`
  scenarios.
primer_glossary:
- term: tree-optimization
  definition: An intermediate representation (IR) and optimization framework within
    GCC. It manipulates code in a tree-like structure to perform various optimizations
    before generating machine code.
- term: trap analysis
  definition: Analysis performed by the compiler to determine if a piece of code could
    potentially cause a runtime trap or exception, such as division by zero or accessing
    null pointers. This information is used for optimization.
- term: REFERENCE_TYPE
  definition: A GCC internal representation for a reference type, similar to C++ references
    or Rust references. It signifies a parameter that refers to an object.
- term: Load Invariant Motion (LIM)
  definition: A compiler optimization pass that moves loop-invariant loads (memory
    accesses whose values do not change within the loop) to the preheader of the loop
    to reduce redundant computations.
- term: rvalue
  definition: In C++, an rvalue represents a temporary value that can be assigned
    to a variable or used in an expression, but not typically modified directly. It's
    often the result of an expression or function call.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b5a11752dcb093fd0f9ce4c205a14acf9dbe702a
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

The tree optimizer's trap analysis now considers the size of objects referred to by `REFERENCE_TYPE` parameters, not just the `this` pointer. This allows the Load Invariant Motion (LIM) pass to move safe invariant loads across these parameters, enabling optimizations that were previously blocked. This change improves performance, with a reported 6.2% cycle reduction on a specific benchmark.
