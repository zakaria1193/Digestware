---
project: gcc
subsystem: scheduler
patch_id: null
tags:
- scheduler
- AArch64
- overflow
- optimization
commit_hash: afa9dd3769077c50180865f53bf2ff8abb0a2f97
source_type: github
author: xiezhiheng
headline: 'sched: Cap max_lookahead_tries to prevent overflow'
tldr: Prevents scheduler overflow on modern cores by capping `max_lookahead_tries`.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The scheduler's `max_lookahead_tries` calculation in `haifa-sched.cc`
  is susceptible to overflow when the backend's `max_issue` value becomes excessively
  large. With modern cores reporting issue rates up to 10, the AArch64 backend's `max_issue`
  reached this value, causing `max_lookahead_tries` to overflow. This commit caps
  `max_lookahead_tries` to mitigate this issue, ensuring stability in the scheduler's
  lookahead mechanism.
primer_glossary:
- term: scheduler
  definition: A compiler component responsible for reordering instructions to improve
    performance, often by optimizing for pipeline utilization and minimizing stalls.
- term: issue rate
  definition: The number of instructions a processor can begin executing in a single
    clock cycle.
- term: max_lookahead_tries
  definition: A scheduler parameter that limits the number of attempts the scheduler
    makes to look ahead in the instruction stream for optimization opportunities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/afa9dd3769077c50180865f53bf2ff8abb0a2f97
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

The issue rate on modern CPU cores has been increasing, leading to a value of 10 in the AArch64 backend's `max_issue` calculation. This caused an integer overflow when calculating `max_lookahead_tries`. This commit caps `max_lookahead_tries` to prevent this overflow, ensuring the scheduler operates correctly. The change is a small but crucial fix for handling high issue rates on contemporary hardware.
