---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- SSA
- PHI nodes
- vectorization
discussion_id: 1106967D-67C5-44CE-8924-03159CA31F1C@hygon.cn
source_type: public_inbox
title: '[RFC] Factoring common pure operations across PHIs / branches to reduce duplicated
  sqrt calls'
headline: Proposes factoring common pure operations across PHIs
tldr: Guoce Feng proposes an optimization to factor out common pure operations like
  `sqrt` across PHIs and branches to reduce redundant calls, especially in vectoriz…
proposer: Guoce Feng <fengguoce@hygon.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Factoring out operations may introduce additional overhead if the merged expression
  is more complex.
- The transformation needs to ensure the operation is truly side-effect-free and safe
  to move.
- Profitability analysis is required to determine whether the transformation results
  in a net performance gain.
exchanges:
- author: Guoce Feng <fengguoce@hygon.cn>
  role: proposer
  position: Proposes factoring common pure operations out of control-flow joins to
    reduce duplicated calls, using `sqrt` as an example.
  quote: 'That is, transform a conceptual pattern like


    phi(sqrt(a), sqrt(b), sqrt(c))


    into


    sqrt(phi(a, b, c))


    when the operation is safe to factor out and doing so is profitable.'
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Suggests looking at PR123113, which relaxes restrictions in phiopt/cselim,
    and at the cselib pass, which may already perform this optimization.
  quote: null
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Clarifies that PR123113 is about merge blocks with more than two predecessors
    and suggests the cselib pass might handle the requested optimization.
  quote: null
primer_expert: This RFC proposes an optimization to sink pure operations out of PHI
  nodes in GCC's SSA representation.  The goal is to transform `phi(op(a), op(b),
  op(c))` into `op(phi(a, b, c))` to avoid redundant computation, especially in vectorized
  code.  This touches on the SSA form, PHI nodes, and optimization passes like `phiopt`,
  `cselim`, and `cselib`.
primer_general: In compiler optimization, a PHI node merges values from different
  control flow paths. This proposal aims to reduce redundant calculations by moving
  common, side-effect-free operations (like square root) out of these merge points.
  By performing the operation once on a merged value, instead of multiple times on
  individual values, the code can become more efficient, particularly when dealing
  with vector operations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/1106967D-67C5-44CE-8924-03159CA31F1C@hygon.cn
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

Guoce Feng proposes an optimization to factor out common pure operations, such as `sqrt`, from control-flow joins in GCC. This aims to transform patterns like `phi(sqrt(a), sqrt(b), sqrt(c))` into `sqrt(phi(a, b, c))` when safe and profitable, potentially reducing redundant calculations in vectorized code. The author seeks guidance on the best implementation approach, considering extending the existing PHI factoring logic or adding a more general common instruction sinking transformation.
