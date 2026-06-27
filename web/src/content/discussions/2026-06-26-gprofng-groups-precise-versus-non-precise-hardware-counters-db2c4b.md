---
project: binutils
subsystem: gprofng
patch_id: null
tags:
- gprofng
- profiling
- hardware counters
- usability
- binutils
discussion_id: 20260626113840.44715-2-claziss@gmail.com
source_type: public_inbox
title: '[PATCH 1/4] gprofng: group precise vs. non-precise HW counters'
headline: Gprofng groups precise versus non-precise hardware counters.
tldr: This patch reorders hardware counter listings in gprofng to differentiate precise
  from non-precise events, improving clarity for users analyzing source-view re…
proposer: Claudiu Zissulescu <claziss@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improved user clarity versus increased complexity in `hwctable.c` output formatting.
exchanges:
- author: Claudiu Zissulescu <claziss@gmail.com>
  role: proposer
  position: Proposes to reorganize hardware counter listings in gprofng to group precise
    and non-precise events for better clarity in source-view reports.
  quote: To make this clearer, split the "std-ctrs" and "raw-ctrs" listings into two
    sub-sections each ("Precise events" and "Standard events"), and append "(precise)"
    to the type label for ABST_EXACT / ABST_EXACT_PEBS_PLUS1 counters.
primer_expert: The gprofng profiling tool relies on hardware performance counters
  to gather execution data. Specifically, it uses `hwctable.c` to manage and display
  information about these counters. This patch modifies `hwc_memop_string` and `hwc_usage_internal`
  to enhance the user interface of this component, distinguishing between precise
  and non-precise event types, which directly impacts the accuracy of program counter
  attribution in profiling reports.
primer_general: Profiling tools like `gprofng` help developers understand where their
  programs spend time. They do this by sampling hardware events, such as CPU cycles
  or cache misses. Some of these hardware events can be precisely attributed to a
  specific line of code, while others might be slightly 'late,' leading to confusion
  in performance reports. This patch aims to clarify the distinction between these
  'precise' and 'non-precise' hardware counters in `gprofng` to make the profiling
  reports easier to understand for developers, ensuring they correctly interpret where
  performance bottlenecks might lie in their code.
series_id: 'binutils:gprofng: group precise vs. non-precise hw counters'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260626113840.44715-2-claziss@gmail.com
bugzilla_url: null
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

This patch rearranges the hardware counter listings presented by `gprofng` to clearly separate precise and non-precise events. This aims to reduce user confusion when interpreting performance data, as current listings do not distinguish between sample attribution methods. The change involves modifying `hwctable.c` to tag specific event types as precise and to emit the listings in two distinct passes.
