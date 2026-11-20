---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- alias analysis
- tbaa
- gcc
commit_hash: ae937b5ba700b3d9883505d73c59983863696d3c
source_type: github
author: Kyrylo Tkachov
headline: Predcom chains ensure TBAA-equivalence for type conversions
tldr: A fix ensures that predcom chains correctly handle type conversions, preventing
  incorrect alias analysis and data races in optimized code.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `pcom_worker::determine_offset` function in `tree-predcom.cc` previously
  created alias chains based solely on a type conversion check (`useless_type_conversion_p`).
  This commit adds a check for `refs_same_for_tbaa_p` in both directions. This ensures
  that references within the same chain also exhibit equivalent TBAA behavior, preventing
  issues like those in PR128324 where a `long` store and a `long long` load formed
  a chain, causing a preheader load of the `long long` location to be incorrectly
  treated as a `long` access due to shared chain root alias information.
primer_glossary:
- term: TBAA
  definition: Tree Alias Analysis. A technique used by GCC to determine memory aliasing,
    i.e., whether different memory accesses might refer to the same location. It's
    crucial for optimizing memory operations.
- term: predcom
  definition: Abbreviation for 'pre-computation' or 'predicate-based commoning', a
    GCC optimization pass that identifies and factors out common computations, often
    involving loop-invariant code.
- term: alias sets
  definition: In alias analysis, a classification of memory locations that distinguishes
    between accesses that are guaranteed not to alias and those that might alias.
    Different data types or memory regions can belong to different alias sets.
- term: LP64
  definition: A data model where `long` and pointers are 64 bits wide, while `int`
    is 32 bits. Common on 64-bit Unix-like systems.
- term: IPA
  definition: Interprocedural Analysis. Analysis that considers information from multiple
    functions or the entire program, rather than just a single function.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ae937b5ba700b3d9883505d73c59983863696d3c
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in GCC's `predcom` optimization pass where references with types that pass `useless_type_conversion_p` were incorrectly placed in the same alias analysis chain. This occurred even if the types had different alias sets (e.g., `long` and `long long` on LP64 systems). The fix enforces that references within a chain must also be equivalent according to TBAA (Tree Alias Analysis), preventing scenarios where loads of one type might alias with stores of another, leading to incorrect values being read before calls.
