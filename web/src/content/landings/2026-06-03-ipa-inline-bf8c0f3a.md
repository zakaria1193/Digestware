---
project: gcc
subsystem: ipa-inline
patch_id: null
tags:
- optimization
- inlining
- IPA
commit_hash: bf8c0f3aee9760190a435d1d0a16cb4bd8698b2a
source_type: github
author: Kyrylo Tkachov
headline: Credit aggregate copies into return slot as eliminated by inlining
tldr: Inliner now correctly accounts for aggregate copies to return values when source
  is a removable local variable.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ipa-fnsummary.cc` function `eliminated_by_inlining_prob` was enhanced
  to correctly assess the cost of aggregate return values. It now recognizes that
  aggregate copies from automatic local variables or parameters (whose addresses are
  not taken) to the return slot can be eliminated by inlining, similar to scalar values.
  This avoids overcharging the inlining cost for value-type wrappers and improves
  the effectiveness of early inlining, especially when combined with SRA.
primer_glossary:
- term: IPA
  definition: IPA stands for Interprocedural Analysis. It refers to compiler analyses
    and optimizations that consider information from multiple functions or across
    the entire program, rather than just a single function in isolation.
- term: inliner
  definition: An inliner is a compiler optimization pass that replaces calls to a
    function with the actual body of that function. This can reduce function call
    overhead and expose more opportunities for optimization.
- term: SRA
  definition: Scalar Replacement of Aggregates (SRA) is an optimization that replaces
    components of an aggregate data type (like a struct or array) with individual
    scalar variables. This can enable further optimizations on these components.
- term: return slot
  definition: The 'return slot' refers to the memory location or mechanism used by
    the compiler to pass a return value from a function back to its caller. For aggregate
    types, this often involves passing a pointer to a memory location where the caller
    expects the result.
- term: invisible-reference result
  definition: In some calling conventions, particularly for C++, aggregate return
    values are passed by invisible reference. This means the compiler implicitly allocates
    space for the return value in the caller's scope and passes a pointer to it to
    the function, which then 'returns' the value by writing to that location.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bf8c0f3aee9760190a435d1d0a16cb4bd8698b2a
date: '2026-06-03'
is_stub: false
stub_reason: ''
---

The early inliner in GCC previously charged an aggregate copy to the return value even if its source was a local variable that could be eliminated after inlining. This change credits such copies as eliminated, preventing unnecessary memory operations for value-type wrappers and improving inlining efficiency. It handles both explicit return value assignments and implicit invisible-reference returns, while still excluding volatile accesses and copies from global/static variables.
