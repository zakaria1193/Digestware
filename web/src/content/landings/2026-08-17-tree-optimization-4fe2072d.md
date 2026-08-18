---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: 4fe2072d5d16ce26112d8035e627d47809aaa6c2
source_type: github
author: Richard Biener
headline: Allow backward threading to loop exit
tldr: Loop optimization can now thread backward through loop headers to exit, enabling
  better peeling of non-iterating loops.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The back_threader pass in GCC's SSA optimization infrastructure now
  allows searching past loop headers when a backward thread path targets a loop exit.
  This special case handles situations where a loop is being peeled, but the threader
  itself cannot copy loops. The patch ensures this is safe by not allowing arbitrary
  loop peeling and correctly dissolves entered subloops without creating new entries
  into the original loop.
primer_glossary:
- term: tree-ssa
  definition: Tree Single Static Assignment form. An intermediate representation in
    GCC used for optimizations, where each variable is assigned a value only once.
- term: loop peeling
  definition: An optimization technique where the first iteration of a loop is extracted
    and executed separately, potentially simplifying the remaining loop body or enabling
    other optimizations.
- term: backward threader
  definition: An optimization component that identifies paths of execution that can
    be duplicated and threaded backward, often to eliminate branches or redundant
    computations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4fe2072d5d16ce26112d8035e627d47809aaa6c2
date: '2026-08-17'
is_stub: false
stub_reason: ''
---

This change enhances the backward threader in GCC's tree-ssa optimization passes. It allows threading to pass through loop headers when exiting a loop, which helps in fully peeling loops that do not iterate. Care has been taken to prevent random loop peeling, with specific measures and new test cases added to ensure correctness.
