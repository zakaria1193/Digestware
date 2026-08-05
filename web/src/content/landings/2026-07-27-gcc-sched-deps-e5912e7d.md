---
project: gcc
subsystem: gcc/sched-deps
patch_id: null
tags:
- optimization
- scheduler
- compile-time
- gcc
commit_hash: e5912e7dc1e3edb72f43624355a7e363cd76f0b3
source_type: github
author: Kyrylo Tkachov
headline: Improves scheduler performance by recording barriers once.
tldr: Reduces scheduler analysis time by avoiding redundant barrier recording.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Before register reload, `sched_analyze_insn` recorded instruction barriers
  (dependencies that block scheduling) redundantly in every `reg_last` entry. This
  could lead to a quadratic-time dependency analysis in large functions, especially
  without the dependency cache. This commit introduces a `pending_barriers` list to
  `deps_desc`. Barriers are now recorded once into this list and materialized only
  when a register is first touched. This lazy approach, used before reload outside
  selective scheduling, drastically reduces the analysis overhead. The eager form
  is retained after reload and for sele…
primer_glossary:
- term: scheduler
  definition: A component of the compiler backend responsible for reordering instructions
    to improve performance, often by minimizing pipeline stalls and maximizing resource
    utilization.
- term: sched-deps
  definition: The subsystem within GCC responsible for analyzing and managing instruction
    dependencies for scheduling.
- term: register reload
  definition: A phase in the compiler backend where virtual registers are mapped to
    physical machine registers.
- term: instruction barriers
  definition: Dependencies between instructions that prevent certain reordering, often
    due to data hazards or other constraints.
- term: reg_last
  definition: A data structure used by the scheduler to track the last instruction
    that defined or used a particular register.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e5912e7dc1e3edb72f43624355a7e363cd76f0b3
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

The GCC scheduler's dependency analysis, specifically how it records instruction barriers before register reload, has been optimized. Previously, barriers were recorded for every register entry, leading to potentially quadratic time complexity in large functions. This change modifies the analysis to record barriers only once into a pending list. These pending barriers are then materialized when a register is first used, significantly speeding up the analysis phase. This is a compile-time optimization with no impact on generated code.
