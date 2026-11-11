---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- memory leak
- bugfix
commit_hash: 78148ac7f7e6bc7a7e82e0b761b48168c81c1988
source_type: github
author: Sendao Yan
headline: Fix memory leak in predicate simplification
tldr: Resolves a memory leak in `predicate::simplify_2` by ensuring heap-allocated
  storage is released.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-predicate-analysis.cc` file contains logic for simplifying
  predicates, which are used to represent conditions in GIMPLE. The `predicate::simplify_2`
  function was found to leak memory associated with `b_chain`. The fix involves ensuring
  that the `ordered_remove` operation on `m_preds` is preceded by a call to release
  the `b_chain`'s storage, likely via `delete` or a similar mechanism, before it's
  de-referenced or removed.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation. It's a low-level
    representation used for optimization passes before generating machine code.
- term: predicate
  definition: In this context, a predicate likely represents a condition or a set
    of conditions used in program analysis, potentially for optimization or verification
    purposes within the compiler's tree-SSA (Static Single Assignment) form.
- term: memory leak
  definition: A situation where a program allocates memory but fails to release it
    when it's no longer needed, leading to a gradual consumption of available memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/78148ac7f7e6bc7a7e82e0b761b48168c81c1988
date: '2026-11-02'
is_stub: true
stub_reason: low_score
---

A memory leak was identified in `predicate::simplify_2` where heap-allocated storage for `b_chain` was not released before being removed from `m_preds`. This commit corrects the issue by ensuring that the storage is properly released, preventing memory from being leaked on each successful simplification.
