---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- pointer_analysis
- c++
- gcc
commit_hash: 080af1a675d94dc25d248b2638e82c03e1476c01
source_type: github
author: Richard Biener
headline: Fixes bogus Pointer Analysis with C++ delete calls
tldr: Correctly handles C++ delete expressions in Pointer Analysis (PTA) to avoid
  incorrect aliasing information.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This patch corrects an overzealous change in gimple-ssa-pta-constraints.cc''s
  `find_func_aliases_for_call`. Previously, all delete calls were being ignored for
  PTA constraints, based on r11-3612-g4f4ced28826ece which aimed to simplify new/delete
  elision. The fix reinstates the original restriction: only ignore calls to the standard
  library''s `operator delete` when `DECL_IS_REPLACEABLE_OPERATOR` is true. This reverts
  a bug introduced by a too-broad interpretation of the new/delete elision improvements,
  ensuring PTA constraints are correctly generated for user-defined delete operators.'
primer_glossary:
- term: Pointer Analysis (PTA)
  definition: A compiler technique that determines which memory locations a pointer
    might refer to. Accurate PTA is crucial for many optimizations, including alias
    analysis, dead code elimination, and memory safety checks.
- term: C++ delete expression
  definition: In C++, a statement that deallocates memory previously allocated with
    `new`. This can involve calling a destructors followed by deallocating the memory
    itself, potentially involving custom `operator delete` functions.
- term: aliasing
  definition: In programming, aliasing occurs when two or more different names (e.g.,
    pointers or variables) refer to the same memory location. Compiler optimizations
    often depend on knowing whether different memory accesses might alias.
- term: g++
  definition: The GNU C++ compiler, part of the GNU Compiler Collection (GCC).
- term: operator delete
  definition: A C++ special function that deallocates memory, typically called after
    a `new` expression to free the allocated memory. It can be overloaded by users.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/080af1a675d94dc25d248b2638e82c03e1476c01
date: '2026-07-13'
is_stub: false
stub_reason: ''
---

This commit corrects an error in GCC's Pointer Analysis (PTA) that incorrectly ignored delete calls originating from C++ delete expressions. A previous change intended to simplify pointer analysis by eliding new/delete pairs globally was too broad. This fix restores the original behavior, only ignoring calls to the standard library's delete, and adds a check for the `-fassume-sane-operators-new-delete` flag. This ensures that PTA accurately reflects memory management, preventing potential bugs related to aliasing.
