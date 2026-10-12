---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- SSA
- bugfix
commit_hash: 189b0202e2664ea06e17c5424d2d17151607ee2d
source_type: github
author: Andrew MacLeod
headline: Check free list before using a relation.
tldr: Fixes a bug where released SSA names could be incorrectly reused in value relations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `value-relation.cc`, `dom_oracle::nearest_relations` previously
  called `reset_range_Info` in `release_ssa_name_fn`. This could lead to returning
  a relation with a released SSA name. The change modifies `release_ssa_name_fn` to
  *not* call `reset_range_info`, and instead, `dom_oracle::nearest_relations` now
  lazily checks the free list before adding a name to the relation list. This ensures
  that SSA names are only added to relations if they are still valid and have not
  been released.
primer_glossary:
- term: SSA name
  definition: In Static Single Assignment (SSA) form, an SSA name represents a unique
    version of a variable after a specific assignment. Each SSA name corresponds to
    a single definition point.
- term: Value relation
  definition: A data structure or analysis that tracks how values of different variables
    or expressions relate to each other within the program. This can be used for optimizations
    like constant propagation or dead code elimination.
- term: Free list
  definition: A data structure used for memory management that keeps track of available
    (free) memory blocks or objects that can be reused. In this context, it likely
    manages reusable SSA name information.
- term: Lazy evaluation
  definition: A strategy where the evaluation of an expression is delayed until its
    value is actually needed. This contrasts with eager evaluation, where expressions
    are evaluated as soon as they are encountered.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/189b0202e2664ea06e17c5424d2d17151607ee2d
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This commit prevents a bug where a relation might incorrectly reuse an SSA name that has already been released. Instead of immediately releasing information about a relation, the compiler now lazily checks a free list when registering nearest relations. This ensures that only valid, unreleased SSA names are used, fixing a potential issue in value relation tracking.
