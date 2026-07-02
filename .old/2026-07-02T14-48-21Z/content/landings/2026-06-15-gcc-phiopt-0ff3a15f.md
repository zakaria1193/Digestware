---
project: gcc
subsystem: gcc/phiopt
patch_id: null
tags:
- optimization
- phi-optimization
- performance
commit_hash: 0ff3a15fcac06cdf3b94f00c28867b3252b62544
source_type: github
author: Andrew Pinski
headline: Phiopt allows factoring out loads even when stores are present
tldr: GCC's phi-optimization pass can now factor out loads even if stores or calls
  precede them, improving store elimination and overall optimization.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change in `tree-ssa-phiopt.cc` specifically targets `is_factor_profitable`
  and `factor_out_conditional_load`. The core idea is to relax the conditions for
  factoring out loads across basic blocks, particularly in the presence of memory
  writes (stores or calls). Previously, such operations would inhibit load factoring,
  even if the memory accessed by the load was distinct from what the store/call was
  modifying. By allowing factoring in these scenarios, it opens up opportunities for
  subsequent store elimination passes to be more effective, addressing cases where
  a load's value could be known…
primer_general: Compilers like GCC optimize your code to make it run faster. One such
  optimization is called "phi-optimization," which operates during the Static Single
  Assignment (SSA) form of your code. SSA is a representation where every variable
  is assigned a value only once, making data flow analysis easier. Phi-optimization
  focuses on consolidating redundant computations, especially loads from memory. This
  update improves the compiler's ability to move memory loads to earlier points in
  the program, even if there are other memory writes (stores) or function calls in
  between. The compiler is smart enough to determine if the load and store operations
  access different memory locations, or if the function calls don't affect the loaded
  value. By moving these loads, dependent computations can also be moved and potentially
  eliminated, leading to faster execution. The compiler now also uses a "cost model"
  to decide if moving a load is actually beneficial for performance, preventing optimizations
  that mi…
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ff3a15fcac06cdf3b94f00c28867b3252b62544
date: '2026-06-15'
is_stub: false
---

The phi-optimization pass in GCC has been enhanced to permit factoring out loads even when stores or calls exist earlier in the code. This improvement enables more aggressive store elimination and factoring, leading to better optimization. A cost model has also been added to guide this load factoring process.
