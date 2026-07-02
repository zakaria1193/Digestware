---
project: gcc
subsystem: gcc/tree-optimization/vect
patch_id: null
tags:
- optimization
- vectorization
- slp
commit_hash: cc5179f3a36a087891beecd1b3cb23d172dc76c7
source_type: github
author: Lili Cui
headline: Allow Single-Lane SLP Fallback When Limit Is Exhausted
tldr: GCC now allows single-lane SLP vectorization to proceed even when the multi-lane
  SLP discovery limit is exhausted, fixing missed optimizations in loops with co…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Scalar replacement via SLP (straight-line-program) vectorization groups
  scalars into vectors. ``vect_analyze_slp_reduction`` previously bailed out early
  if the SLP discovery limit was exhausted, blocking single-lane SLP. The fix moves
  the limit check to only guard chain analysis, as single-lane trees don't cause exponential
  growth. The interaction with IPA is that missed SLP optimizations can prevent inlining,
  but a toolchain dev outside SLP might not know the nuance of the single-lane fallback
  path.
primer_general: SLP vectorization in GCC identifies opportunities to perform the same
  operation on multiple data elements simultaneously using SIMD instructions — e.g.
  replacing four `float` additions with a single vector addition. This commit fixes
  a limitation in the SLP vectorization process.  The vectorizer has a limit on how
  much it will search; after reaching this limit, it would fail to vectorize even
  when a simpler, single-lane vectorization was possible. This change allows single-lane
  vectorization to proceed even after the limit is reached, improving performance.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:tree-optimization/vect: allow single-lane slp fallback when limit
  is exhausted'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cc5179f3a36a087891beecd1b3cb23d172dc76c7
date: '2026-05-12'
is_stub: false
---

GCC's SLP vectorizer now attempts single-lane vectorization even after the multi-lane vectorization limit is reached. Previously, the limit check blocked all SLP discovery, including single-lane fallbacks, leading to missed optimizations in code with multiple independent conditional reductions. This change improves performance (3.8% on EMR, 1.4% on Znver5 for 731.astcenc_r with -Ofast).
