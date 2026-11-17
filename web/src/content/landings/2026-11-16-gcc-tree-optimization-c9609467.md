---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- performance
- passes
commit_hash: c9609467230d5d690be1bde0d00fa3b8e2652a3d
source_type: github
author: Sendao Yan
headline: Move switch lowering after jump threading to fix PR128102.
tldr: Moving the switch lowering pass after jump threading restores GCC 11 performance
  for PR128102 by ensuring the jump threader sees GIMPLE_SWITCH.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit reorders GCC's optimization passes, moving `pass_lower_switch`
  after `pass_thread_jumps_full` within `gcc/passes.def`. The `pass_thread_jumps_full`
  pass performs backward jump threading, which is sensitive to the presence of `GIMPLE_SWITCH`
  constructs. When `pass_lower_switch` executed earlier, it lowered switches into
  decision trees before jump threading could fully operate on them. This regression
  impacted the performance of state-machine code, specifically in PR128102, and is
  now fixed by ensuring the jump threader sees the switch form.
primer_glossary:
- term: GIMPLE
  definition: GNU Intermediate Representation Language. A low-level, three-address
    code representation used by GCC after initial parsing and before machine code
    generation.
- term: optimization passes
  definition: Sequences of transformations applied to the intermediate representation
    of code to improve its performance, size, or other metrics.
- term: jump threading
  definition: An optimization technique that identifies sequences of conditional branches
    and replaces them with direct branches to the ultimate target, simplifying control
    flow.
- term: backward jump threader
  definition: A specific type of jump threading pass that analyzes control flow from
    the end of basic blocks backwards to optimize loops and complex branching structures.
- term: PR128102
  definition: Problem Report 128102. A bug report filed against GCC, detailing a specific
    issue or regression.
discussion_id_link: null
bugzilla_pr: null
series_id: gcc:tree-optimization/128102 - lower switches after the late jump threading
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c9609467230d5d690be1bde0d00fa3b8e2652a3d
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

The `pass_lower_switch` has been moved to execute after `pass_thread_jumps_full` in the GCC pass pipeline. This change is necessary because the backward jump threader was failing to correctly optimize a state-machine loop in binascii_a2b_base64. When switch lowering occurred before jump threading, the threader missed the `GIMPLE_SWITCH` construct, leading to performance degradation and exposing issues like PR128102.
