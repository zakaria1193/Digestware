---
project: gcc
subsystem: gcc/cfghooks
patch_id: null
tags:
- cfg
- cleanup
- dead code
commit_hash: bed1a621d670706a1811d8d85528ed048dd57234
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Remove new_bb_cbk callback from make_forwarder_block'
tldr: Removes an unused callback function from `make_forwarder_block`, simplifying
  the code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `new_bb_cbk` argument from `make_forwarder_block`
  in `cfghooks.cc` and `cfghooks.h`, along with corresponding updates in `cfgloop.cc`,
  `cfgloopmanip.cc`, `tree-cfgcleanup.cc`, and `tree-ssa-threadupdate.cc`. This callback
  has been unused since r0-78960-g89f8f30f356532.
primer_general: This commit cleans up the control flow graph (CFG) manipulation code
  in GCC by removing an unused callback function.  A callback function is a function
  passed as an argument to another function, allowing the latter to call it at a specific
  time.  In this case, the `new_bb_cbk` callback in `make_forwarder_block` was never
  actually used, so removing it simplifies the code and reduces potential for errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bed1a621d670706a1811d8d85528ed048dd57234
date: '2026-04-15'
---

This commit removes the `new_bb_cbk` callback from the `make_forwarder_block` function, as it has been unused for 19 years. Removing dead code simplifies the codebase.
