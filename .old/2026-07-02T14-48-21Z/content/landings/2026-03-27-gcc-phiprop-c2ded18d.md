---
project: gcc
subsystem: gcc/phiprop
patch_id: null
tags:
- optimization
- compiler pass
- SSA
commit_hash: c2ded18d4fcc5d7d951a6bbc455dadbf5a837939
source_type: github
author: Andrew Pinski
headline: 'Phirop: Move the VUSE check before dominator tests.'
tldr: The VUSE check now happens before the dominator tests in the phiprop pass, which
  should result in a small optimization.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The commit reorders checks within ``propagate_with_phi`` in ``tree-ssa-phiprop.cc``.
  Moving the VUSE check before dominator tests avoids unnecessary computation when
  the VUSE check fails. The dominator tests do not determine if a propagation will
  occur, so checks that prevent propagation are performed first.
primer_general: The phiprop pass in GCC optimizes code by propagating values through
  phi nodes (used to merge values from different control flow paths). This commit
  reorders the checks performed during this propagation process. Specifically, a check
  related to 'VUSE' (likely a check related to variable usage) is now performed before
  'dominator tests' (which determine if one block of code always executes before another).
  This optimization avoids unnecessary work when the VUSE check would have failed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c2ded18d4fcc5d7d951a6bbc455dadbf5a837939
date: '2026-03-27'
---

The phiprop pass now performs the VUSE check before the dominator tests.  This reordering avoids unnecessary dominator tests when the VUSE check would have failed, resulting in a small optimization.  The dominator tests no longer indicate if a propagation can occur, so checks that prevent propagation should be performed first.
