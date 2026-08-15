---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- integer-types
- performance
commit_hash: 21c8ddd2cd2f3bf64225e4523e20e795083676fb
source_type: github
author: Andrew MacLeod
headline: Limit phi analyzer iterations for large bit-int types
tldr: Prevents excessive iterations in phi analysis for large integer types.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `phi_group::calculate_using_modifier` within `gimple-range-phi.cc`,
  the upper bound for loop iterations has been capped at `MAX_FIXED_MODE_SIZE`. This
  pass simulates the effect of modifiers on cyclic PHI nodes to establish initial
  values. For `_BitInt` types, which can have arbitrary precision, simulating up to
  the number of bits could lead to extremely long or infinite loops. Capping the iterations
  prevents this excessive computation, ensuring the analysis terminates in a reasonable
  time.
primer_glossary:
- term: phi analyzer
  definition: A component within the compiler's analysis framework that handles Phi
    (Φ) nodes. Phi nodes are used in SSA (Static Single Assignment) form to represent
    values that may come from different control flow paths.
- term: cyclic PHI
  definition: A Phi node where the value depends on itself, typically found in loops.
    Resolving the correct value often requires iterative computation.
- term: modifier
  definition: In this context, a transformation or operation applied to a value, often
    within a loop or cyclic dependency.
- term: _BitInt
  definition: A C++ type that supports arbitrary-precision integers, allowing users
    to specify integers of any bit width.
- term: MAX_FIXED_MODE_SIZE
  definition: A constant defining the maximum bit width for fixed-size machine modes
    that GCC typically handles efficiently. Beyond this size, operations might become
    significantly more complex or unsupported.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/21c8ddd2cd2f3bf64225e4523e20e795083676fb
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This commit limits the number of iterations performed by the phi analyzer when simulating cyclic PHIs, specifically for large `_BitInt` types. The analyzer previously attempted to simulate modifiers for a number of times equal to the bit precision, which is impractical for very large types. The iteration bound is now capped at `MAX_FIXED_MODE_SIZE`, improving performance and preventing potential hangs.
