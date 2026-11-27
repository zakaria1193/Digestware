---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- ssa
- value numbering
commit_hash: 9a872903b6f73840a5128790e9127e063173adb0
source_type: github
author: Richard Biener
headline: 'tree-optimization/129064: Fix PHI value handling in backedge checks'
tldr: Corrects how PHI values are handled during backedge checks to prevent incorrect
  VARYING states.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, the `do_rpo_vn` function iterates through blocks
  in RPO order. When checking for changes across a backedge to a destination block
  containing PHIs, it currently updates the PHIs. If a change is detected in a PHI,
  the function continues to the next iteration, re-visiting the destination block.
  However, at this point, PHIs before the changed one retain their old values, while
  the changed PHI has its new value. This inconsistency can lead to cycles being incorrectly
  marked as `VARYING` because not all PHIs in the destination block reflect the same
  iteration's changes. The…
primer_glossary:
- term: PHI node
  definition: A special instruction in SSA form that merges values from different
    control flow paths. It takes multiple arguments, each corresponding to a predecessor
    block, and outputs a single value representing the merged result.
- term: backedge
  definition: An edge in a control flow graph that jumps from a later block to an
    earlier block, typically representing a loop.
- term: SSA
  definition: Static Single Assignment form. A representation of code where every
    variable is assigned exactly once. PHI nodes are used to handle merging values
    at control flow join points.
- term: VARYING
  definition: A state in value numbering indicating that a value is not constant or
    has multiple possible values, often due to changes or uncertainty in the control
    flow.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9a872903b6f73840a5128790e9127e063173adb0
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

A bug in `do_rpo_vn` allowed PHI values to be updated prematurely when checking backedges. This led to inconsistent states across different PHIs within the same block, causing some to advance while others lagged. The lagging PHIs would then be marked as `VARYING`, preventing the detection of equivalent values. This patch restores PHI values after the check, ensuring consistent evaluation and accurate equivalence detection.
