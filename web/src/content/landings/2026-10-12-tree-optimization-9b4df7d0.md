---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- loop optimization
- undefined behavior
commit_hash: 9b4df7d052915431725e58156754dfb077b915c1
source_type: github
author: Richard Biener
headline: 'tree-optimization: Avoid UB and miscompiles in vectorized loops'
tldr: Fixes vectorization of loops with 'niter' assumptions and 'may_be_zero' conditions
  to prevent undefined behavior and miscompiles.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_loop_versioning` pass in `tree-vect-loop-manip.cc` previously
  had issues with loops containing `niter` assumptions and `may_be_zero` conditions,
  leading to UB and miscompiles. This commit modifies the pass to emit versioning
  for these conditions first, rewriting them to defined operations and placing them
  in a separate basic block. This strategy ensures that these conditions are evaluated
  predictably, preventing misoptimizations and adhering to defined behavior, particularly
  around short-circuiting logic.
primer_glossary:
- term: vectorization
  definition: An optimization technique where a single instruction operates on multiple
    data elements simultaneously, often leveraging SIMD (Single Instruction, Multiple
    Data) hardware.
- term: niter assumption
  definition: An assumption made by the compiler about the number of iterations a
    loop will execute, used to aid optimization.
- term: may_be_zero
  definition: A condition or flag indicating that a value or count might be zero,
    which can affect loop analysis and optimization.
- term: UB
  definition: Undefined Behavior. In C and C++, this refers to behaviors for which
    the C++ standard imposes no requirements, meaning the compiler can generate any
    code or no code, leading to unpredictable results.
- term: basic block (BB)
  definition: A contiguous sequence of code within a function in which control enters
    at the beginning and leaves at the end without the possibility of branching except
    at the end.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9b4df7d052915431725e58156754dfb077b915c1
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This change prevents undefined behavior and subsequent miscompiles when vectorizing loops that involve 'niter' assumptions or 'may_be_zero' conditions. By emitting versioning for these conditions first and rewriting them to defined operations in a separate basic block, the optimization pass now correctly handles these cases, particularly when short-circuiting is involved. This addresses a hole in previous mitigations for the 'may_be_zero' condition.
