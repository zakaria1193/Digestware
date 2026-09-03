---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- testing
- tree-ssa
commit_hash: c25dbfc56075ffb8fbe8e1437e15266b9082bbd7
source_type: github
author: Aldy Hernandez
headline: Add testcase for backward threading from never-executed entry edges.
tldr: A new testcase verifies that the backward threader correctly rejects paths with
  never-executed entry edges.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A new testcase is added for `tree-ssa/pr105679.c` to validate the `backward
  threader`'s behavior. This pass rejects paths with entry edges deemed unlikely to
  be executed. The test ensures that this rejection logic, introduced in r13-1891-g49ba4fdeb648c1,
  works as intended and does not regress, particularly concerning PRs 105679 and 126906.
primer_glossary:
- term: backward threader
  definition: A component within the GCC optimization passes that analyzes control
    flow graphs and 'threads' execution paths backward. It can be used to identify
    and potentially optimize or remove code that is unreachable or unlikely to be
    executed.
- term: tree-ssa
  definition: GCC's internal representation that uses a Static Single Assignment (SSA)
    form. SSA simplifies many optimizations by ensuring each variable is assigned
    a value only once.
- term: entry edge
  definition: In a control flow graph, the edge that represents the first instruction
    or basic block executed in a function or a loop.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c25dbfc56075ffb8fbe8e1437e15266b9082bbd7
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

This commit adds a testcase to verify that the backward threader in the tree-ssa optimization pass correctly identifies and rejects paths whose entry edge is likely never executed. This behavior was introduced in a previous change (r13-1891-g49ba4fdeb648c1) but lacked a corresponding test, potentially leading to regressions. The new test ensures this optimization remains effective.
