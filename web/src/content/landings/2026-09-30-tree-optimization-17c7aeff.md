---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: 17c7aeffec9e1f7576957fdcb21e380d4e209c6f
source_type: github
author: Dominic P
headline: 'forwprop: Reset MOD result range when X is negative'
tldr: Fixes incorrect constant folding of the MOD operator when the dividend can be
  negative.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Value Range Propagation (VRP) pass relies on flow-sensitive information
  to determine the possible range of values for variables. In forwprop.cc, the `simplify_phi_result_movdiv`
  function sometimes rewrites `M = X % PHI` into `M = X & PHI`. If X can be negative,
  this rewrite preserves the zero-ness of M but not its precise value range. This
  commit corrects VRP by resetting the flow-sensitive info of M when such a rewrite
  occurs, preventing incorrect folds of M to 0.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/17c7aeffec9e1f7576957fdcb21e380d4e209c6f
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

The forward propagation pass in GCC incorrectly preserved the range of a MOD result even when the dividend was negative. This led to incorrect folding of the result to zero in specific cases. This change resets the flow-sensitive information of the MOD result when its value is rewritten under these conditions, ensuring accurate constant propagation.
