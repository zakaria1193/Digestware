---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop unrolling
- bugfix
commit_hash: 74cd90132516624104d353e370e660c861a81958
source_type: github
author: Richard Biener
headline: Fix loop unrolling when latch execution count reaches maximum value
tldr: Corrects loop unrolling to prevent wrap-around issues with maximum latch execution
  counts.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The loop unrolling pass in GCC, specifically within `tree-ssa-loop-manip.cc`,
  calculates the number of times a loop header executes to determine the extent of
  unrolling. When the maximum value of the loop's iteration count type is reached,
  the calculation for header executions can wrap around to zero. This commit modifies
  the `determine_exit_conditions` function to prevent this wrap-around for constant
  iteration counts, thus avoiding a common cause of incorrect code generation when
  the loop is frequently executed.
primer_glossary:
- term: Loop unrolling
  definition: A loop transformation technique that reduces loop overhead by replicating
    the loop body multiple times and adjusting the loop control. This can improve
    performance by reducing branch costs and increasing instruction-level parallelism.
- term: Latch execution count
  definition: The number of times the loop's latch (the condition that determines
    if the loop continues) is executed. In unrolling, this is used to calculate how
    many times the loop header executes.
- term: predictive commoning
  definition: A compiler optimization that identifies and commonizes code patterns
    that are likely to occur together, potentially based on profiling data or predictive
    analysis.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/74cd90132516624104d353e370e660c861a81958
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

A bug in the generic loop unroller caused incorrect code generation when the loop's latch execution count reached its maximum representable value. This led to a wrap-around to zero, resulting in wrong code. The fix modifies `tree-ssa-loop-manip.cc` to avoid this wrapping for constant iteration counts, improving the reliability of loop unrolling.
