---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- tree-optimization
- CLZ
- loop optimization
commit_hash: 52ceb1698c9f46be900fe3719c2967fe74bcd1f7
source_type: github
author: Shivam Gupta
headline: Handle undefined ranges in CLZ loop optimization.
tldr: Fixes loop optimization for CLZ by correctly handling undefined ranges.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-loop-niter.cc`, the `number_of_iterations_cltz` and `number_of_iterations_cltz_complement`
  functions optimize signed right-shift loops into CLZ operations. These functions
  use `Ranger` on the loop preheader to check for non-negativity. However, `range_on_edge`
  returning true only confirms Ranger support, not that the range is defined. This
  commit adds a check for `undefined_p()` before applying the non-negativity test,
  preventing misoptimizations when the range is not fully determined.
primer_glossary:
- term: CLZ
  definition: Count Leading Zeros, an instruction that counts the number of zero bits
    from the most significant bit to the first set bit.
- term: loop optimization
  definition: Compiler transformations applied to loops to improve their execution
    speed, such as reducing the number of iterations or simplifying loop-invariant
    computations.
- term: Ranger
  definition: A GCC analysis pass that determines the range of values a variable can
    take during program execution.
- term: loop preheader
  definition: A basic block that unconditionally jumps to the beginning of a loop,
    used to facilitate loop optimizations by providing a single entry point.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/52ceb1698c9f46be900fe3719c2967fe74bcd1f7
date: '2026-09-12'
is_stub: false
stub_reason: ''
---

The optimization that converts signed right-shift loops into Count Leading Zeros (CLZ) operations previously mishandled undefined ranges. When determining the number of loop iterations, the `Ranger` analysis could return an undefined range, which was then incorrectly treated as a valid non-negative range. This change adds explicit checks for undefined ranges, preventing incorrect optimization.
