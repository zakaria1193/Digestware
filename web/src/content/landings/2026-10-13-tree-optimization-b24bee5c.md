---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
commit_hash: b24bee5c07afb8c90c02597527871a44b00c4fd5
source_type: github
author: Richard Biener
headline: Fix wrong code with non-linear induction vectorization
tldr: Corrects vectorization of non-linear induction variables with shifts to avoid
  incorrect code generation.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_nonlinear_induction` function in `tree-vect-loop.cc`
  incorrectly validated shift amounts for non-linear induction variables. It only
  checked against `nunits` (number of loop units) rather than `VF` (vectorization
  factor). This commit fixes the check to use `VF` for shift amount validation, preventing
  incorrect code generation when vectorizing loops with non-linear induction variables
  and shifts.
primer_glossary:
- term: vectorization
  definition: An optimization technique where a single instruction operates on multiple
    data elements simultaneously. This is achieved by using special vector registers
    and instructions.
- term: induction variable
  definition: A variable in a loop whose value is updated by adding a constant or
    an expression involving loop-invariant variables in each iteration. It's commonly
    used for array indexing.
- term: non-linear induction variable
  definition: An induction variable whose update step is not a simple constant addition,
    but rather a more complex expression, such as a multiplication or a shift, that
    might depend on the loop iteration count in a non-additive way.
- term: VF
  definition: Vectorization Factor. The number of data elements that can be processed
    in parallel by a single vector instruction. It corresponds to the width of the
    vector registers and the chosen vectorization strategy.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b24bee5c07afb8c90c02597527871a44b00c4fd5
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

A bug in GCC's vectorization pass could generate incorrect code for non-linear induction variables involving shifts. The issue stemmed from an incomplete check of the shift amount, which only considered loop iteration counts (`nunits`) instead of vector factor counts (`VF`). This commit corrects the validation logic to properly account for the vector width, ensuring accurate code generation for these patterns.
