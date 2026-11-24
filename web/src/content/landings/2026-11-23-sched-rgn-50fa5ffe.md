---
project: gcc
subsystem: sched-rgn
patch_id: null
tags:
- optimization
- scheduler
- bugfix
commit_hash: 50fa5ffebbd6dc02dd045fff75923a5409d9f169
source_type: github
author: Yongqiang Tian
headline: 'sched-rgn: Correctly count non-debug instructions in region size estimates.'
tldr: Fixes region scheduling to accurately count non-debug instructions, resolving
  over-subtraction issues with notes and improving region size estimation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `rgn_estimate_number_of_insns` function in `sched-rgn` calculates
  the size of code regions for instruction scheduling. It previously used a Line Number
  Information (LUID) span and subtracted debug instructions. This method over-subtracted
  debug instructions when a note followed the last non-debug instruction in a block.
  The fix directly counts non-debug instructions, yielding a more accurate size estimate
  and resolving PR128860.
primer_glossary:
- term: sched-rgn
  definition: A GCC pass responsible for instruction scheduling within code regions,
    aiming to improve execution performance by reordering instructions.
- term: LUID
  definition: Likely refers to a Line Number Information (LNI) or similar mechanism
    that tracks instruction positions, possibly at a finer granularity than source
    lines.
- term: note
  definition: In the context of assembly or object files, a 'note' section or entry
    contains metadata or information not directly executable code, often used for
    debugging or linking.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/50fa5ffebbd6dc02dd045fff75923a5409d9f169
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

The `sched-rgn` pass incorrectly estimated the number of non-debug instructions in a code region, particularly when notes followed the last non-debug instruction. This commit modifies the estimation to directly count non-debug instructions, fixing an issue where debug instructions were subtracted too many times and improving accuracy for regions containing only debug code. This resolves PR128860.
