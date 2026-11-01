---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- correctness
commit_hash: 09c66632baa6ebf1bf18abc1b99b8f78dce16256
source_type: github
author: Rohith Kapelli
headline: Stop miscompiling by releasing distance vectors for unrepresentable self-dependences
tldr: Fixes miscompilations caused by incorrect handling of complex loop self-dependences
  in the GCC optimizer.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-optimization` subsystem handles loop analysis and transformation.
  This commit addresses a correctness issue in `add_multivariate_self_dist` and `add_other_self_distances`
  within `tree-data-ref.cc`. When a self-dependence is detected but cannot be precisely
  characterized by distance vectors (e.g., due to non-constant loop bounds or multiple
  varying loop indices), the existing logic only cleared the `DDR_AFFINE_P` flag.
  This commit now sets `DDR_ARE_DEPENDENT` to `chrec_dont_know` and releases the distance
  vectors, preventing misinterpretation by subsequent passes that consume these v…
primer_glossary:
- term: distance vectors
  definition: In loop optimization, distance vectors describe the difference in loop
    iteration indices between two accesses to the same memory location in different
    iterations. They are crucial for determining data dependence and enabling transformations
    like loop unrolling and vectorization.
- term: self-dependence
  definition: A data dependence where an instruction depends on a previous instruction
    within the same loop, but in a different iteration. This is common in array processing.
- term: chrec_dont_know
  definition: A special value indicating that the precise nature of a dependence or
    relation is unknown or cannot be determined by the analysis. It serves as a conservative
    flag to prevent incorrect optimizations.
- term: unroll-and-jam
  definition: A loop transformation technique that combines loop unrolling with loop
    jamming. It replicates loop body iterations and then combines them to improve
    instruction-level parallelism and reduce loop overhead.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/09c66632baa6ebf1bf18abc1b99b8f78dce16256
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

GCC's loop optimizer can miscompile code when it encounters complex self-dependences that cannot be precisely described by distance vectors. This change updates the `tree-data-ref.cc` logic to explicitly mark such dependencies as unknown and release their associated distance vectors. This prevents downstream components, like the outer-loop vectorizer and unroll-and-jam passes, from misinterpreting these dependencies and causing incorrect code generation. A new test case verifies this fix.
