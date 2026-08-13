---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- control-flow
- compiler-internals
commit_hash: 218575554420ded75052e56d5a89cd23522f20a7
source_type: github
author: Aldy Hernandez
headline: Thread backward paths ending in computed gotos.
tldr: Backward threader now supports computed gotos, improving optimization analysis.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `back_threader` in `tree-ssa-threadbackward.cc` determines reachability
  and control flow. It previously only handled `GIMPLE_COND` and `GIMPLE_SWITCH` on
  exit edges. This change adds support for `GIMPLE_GOTO` by leveraging recent `prange`
  (points-to analysis) improvements, enabling it to correctly thread paths that end
  in computed jumps. Handling of abnormal PHI nodes remains a follow-up task.
primer_glossary:
- term: Backward threader
  definition: A compiler analysis pass that traces control flow paths backward from
    a given point to determine reachability and identify code structures.
- term: Computed goto
  definition: A control flow construct where the target of a jump is determined at
    runtime by the value of an expression, typically a pointer to a label.
- term: GIMPLE
  definition: GCC's Internal Machine-independent Optimizer Representation, a three-address
    code form used for intermediate optimization passes.
- term: Points-to analysis
  definition: A static analysis technique that determines which memory locations a
    pointer variable might refer to during program execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/218575554420ded75052e56d5a89cd23522f20a7
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

The GCC backward threader can now analyze control flow paths that terminate in computed gotos. Previously, it only handled conditional or switch statements, but recent improvements in points-to information from the `prange` analysis make handling GIMPLE_GOTO straightforward. This enhances the accuracy of optimization passes that rely on control flow analysis.
