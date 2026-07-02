---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: b052d6bbbeea2b04c8a4f765e89b0b3f19f81764
source_type: github
author: Richard Biener
headline: Iterate PRE clean for cyclic value graphs
tldr: Fix PRE pass to handle cyclic value graphs by iterating.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-pre.cc` pass's `clean` function previously assumed acyclic
  value graphs. This commit introduces iteration to handle cases where ANTIC_IN values
  form a cycle, ensuring all invalid expressions are pruned. This is necessary for
  correctness when the SSA value graph contains cycles.
primer_glossary:
- term: PRE
  definition: Partial Redundancy Elimination is a compiler optimization pass that
    eliminates redundant computations by identifying identical expressions whose values
    are computed multiple times.
- term: SSA
  definition: Static Single Assignment is an intermediate representation form used
    in compilers where every variable is assigned exactly once. This simplifies many
    dataflow analyses and optimizations.
- term: ANTIC_IN
  definition: In the context of SSA and PRE, this likely refers to a data structure
    or analysis that tracks incoming values to an 'anticipatable' expression, crucial
    for detecting redundancy.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b052d6bbbeea2b04c8a4f765e89b0b3f19f81764
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

The PRE (Partial Redundancy Elimination) optimization pass now iterates to correctly prune invalid expressions when encountering cyclic value graphs. This change addresses a specific test case exhibiting this cycle, ensuring more robust optimization.
