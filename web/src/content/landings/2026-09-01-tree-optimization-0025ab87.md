---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- testing
- tree-ssa
commit_hash: 0025ab8747c66ce47dd6705460d5e1b0b5d37d39
source_type: github
author: Aldy Hernandez
headline: Add testcases for backward threading to never-executed edges.
tldr: Two new testcases ensure the backward threading optimization correctly avoids
  edges that are unlikely to be executed.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Two testcases, `pr106495-1.c` and `pr106495-2.c`, are added to `gcc.dg/tree-ssa/`
  to cover the `backward threading` to `never-executed edges` logic. These tests were
  generated retroactively to ensure that the optimization introduced in r13-1924-gb9da686470d1c2,
  which avoids threading to such edges, is correctly implemented and does not regress.
  They confirm that code that previously failed now passes with this change.
primer_glossary:
- term: backward threading
  definition: An optimization technique where the compiler analyzes control flow to
    identify and potentially remove or optimize code that is unlikely to be executed.
    It involves 'threading' execution paths backward from certain points.
- term: never-executed edges
  definition: In a control flow graph, edges that lead to code sections that the compiler
    determines are impossible or extremely unlikely to be reached during program execution.
- term: tree-ssa
  definition: GCC's internal representation that uses a Static Single Assignment (SSA)
    form. SSA simplifies many optimizations by ensuring each variable is assigned
    a value only once.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0025ab8747c66ce47dd6705460d5e1b0b5d37d39
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

This commit introduces two new testcases to validate the behavior of the backward threading optimization, which aims to avoid threading execution paths to edges that are probably never reached. These tests cover scenarios related to PRs 106495 and 126906. Both testcases pass with the recent optimization changes (r13-1924-gb9da686470d1c2) that implemented this edge-avoidance logic, confirming its correctness.
