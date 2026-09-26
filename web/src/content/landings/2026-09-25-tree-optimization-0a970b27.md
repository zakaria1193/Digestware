---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- loop analysis
- undefined behavior
commit_hash: 0a970b2702183d290df044858fd4df13ef698924
source_type: github
author: Richard Biener
headline: 'tree-optimization: Avoid overflow in vector loop epilog initialization'
tldr: Prevents undefined behavior from integer overflow when calculating vector loop
  epilog start values.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes PR tree-optimization/127588 by modifying `vect_update_ivs_after_vectorizer`
  in `tree-vect-loop-manip.cc`. The computation for the epilog IV start value, previously
  `init + step * vect-niters`, could overflow. By using an unsigned type for this
  calculation, the compiler now correctly handles potential overflows, avoiding undefined
  behavior and ensuring accurate loop invariant (IV) updates after vectorization.
primer_glossary:
- term: vectorizer
  definition: A compiler pass that transforms scalar code into vector code, using
    special CPU instructions to perform operations on multiple data elements simultaneously.
- term: loop epilog
  definition: The portion of a loop that executes after the main vectorized part,
    typically to handle any remaining iterations that did not fit into the vector
    width.
- term: invariant (IV)
  definition: Induction variable. A variable in a loop whose value changes predictably
    with each iteration, often used as a loop counter or for array indexing.
- term: undefined behavior (UB)
  definition: Behavior that results from an erroneous program construct or invalid
    input, for which the C++ standard imposes no requirements. Compilers may assume
    UB does not happen, leading to unexpected results.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0a970b2702183d290df044858fd4df13ef698924
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

This commit resolves an undefined behavior issue in the vectorizer by using an unsigned type to compute the start value of loop epilogs. This prevents potential overflow during the calculation of `init + step * vect-niters`, ensuring more reliable loop transformations.
