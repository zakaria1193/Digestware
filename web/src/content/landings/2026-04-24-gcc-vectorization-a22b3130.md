---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- gcc
- vectorization
- x86
- optimization
commit_hash: a22b31304e0a1ad21751f882c02c32c167c78793
source_type: github
author: Richard Biener
headline: Enable compare costs by default for x86 vectorization.
tldr: GCC now enables vector cost comparison by default for x86, improving vectorization
  decisions.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This flips the default for `--param ix86-vect-compare-costs`, which
  impacts `ix86_vector_costs` and its interactions with the vectorizer's cost model.  The
  change influences decisions within the vectorization epilogue selection process.
  Test adjustments required consideration of in-order reduction costs, and the addition
  of `-fno-vect-cost-model` indicates a dependency on more advanced cost modeling
  features. See also PR120398, PR123603.
primer_general: Vectorization is a compiler optimization that replaces scalar operations
  with vector operations, processing multiple data elements simultaneously.  The decision
  to vectorize and the choice of vectorization strategy involves cost modeling. GCC's
  cost model estimates the performance impact of different vectorization options.
  This commit changes the default behavior of a parameter that enables a comparison
  of these costs for x86 architectures, potentially leading to better code generation.
  The vectorizer lives between the high-level tree-SSA IR and the instruction selector.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a22b31304e0a1ad21751f882c02c32c167c78793
date: '2026-04-24'
---

The default behavior of the `ix86-vect-compare-costs` parameter has been flipped, enabling vector cost comparison by default for x86. This change, driven by discussions during stage3/4, aims to improve vectorization decisions by comparing the costs of different vectorization strategies. Several test cases were updated and adjusted to reflect the new default, ensuring that existing functionality remains intact while leveraging the benefits of cost comparison.
