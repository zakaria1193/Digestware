---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- gcc
- refactor
- c++
commit_hash: 98a6b0be1dda04d3155723f596041a41fc18678b
source_type: github
author: Andrea Pinski
headline: 'forwprop: Wrap C++ enums/structs in anonymous namespace'
tldr: Prevents ODR violations by localizing C++ types in the forward propagation pass.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In C++, entities declared at namespace scope (including global scope)
  must have unique names across all translation units that use them if they are to
  be used in a way that might lead to linkage. This commit wraps `long_mul_kind`,
  `long_mul_extract`, and `long_mul_summand` in an anonymous namespace within `tree-ssa-forwprop.cc`.
  This makes them internal to that specific `.cc` file, preventing potential ODR violations
  if similar type names were used elsewhere in GCC, even if they represent different
  concepts.
primer_glossary:
- term: anonymous namespace
  definition: A C++ construct that allows declarations to have internal linkage, meaning
    they are only visible within the current translation unit (source file). This
    is an alternative to using `static` for internal linkage.
- term: ODR conflict
  definition: A violation of the One Definition Rule (ODR) in C++, which states that
    any non-inline function or variable must have exactly one definition in the program.
    Conflicts arise when a name is defined multiple times in a way that violates this
    rule, often due to linkage issues.
- term: translation unit
  definition: A source file after it has been processed by the C++ preprocessor. It's
    the unit that the compiler compiles.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/98a6b0be1dda04d3155723f596041a41fc18678b
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

This commit encapsulates the `long_mul_kind` enum, `long_mul_extract` enum, and `long_mul_summand` struct within an anonymous namespace in `tree-ssa-forwprop.cc`. This change prevents potential One Definition Rule (ODR) conflicts by ensuring these types are local to the translation unit, rather than polluting the global scope. This improves code modularity and avoids issues in larger projects where symbol name collisions could occur.
