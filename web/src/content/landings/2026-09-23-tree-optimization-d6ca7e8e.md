---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- UBSAN
commit_hash: d6ca7e8e1cf62734f0257cdc668da907cf3e0297
source_type: github
author: Richard Biener
headline: Fix offset computation association in VNVN
tldr: Corrects an offset computation in GCC's SCCVN pass to prevent potential overflows
  and UBSAN issues.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, the `vn_walk_cb_data::push_partial_def` function's
  offset calculation was re-associated to prevent potential integer overflows. This
  addresses a UBSAN-reported issue related to the order of operations within the Value
  Numbering (VN) framework, ensuring the invariant is maintained correctly before
  the partial definition is pushed.
primer_glossary:
- term: UBSAN
  definition: Undefined Behavior Sanitizer. A runtime instrumentation tool that detects
    undefined behavior in C/C++ code, such as integer overflow, which can lead to
    crashes or security vulnerabilities.
- term: Value Numbering (VN)
  definition: A compiler optimization technique used to identify and eliminate redundant
    computations by assigning unique numbers (values) to expressions. SCCVN (Sparse
    Conditional Value Numbering) is an advanced form that operates efficiently even
    on sparse data.
- term: SSA
  definition: Static Single Assignment. An intermediate representation form in compilers
    where every variable is assigned a value exactly once, simplifying many optimization
    analyses.
- term: tree-ssa-sccvn.cc
  definition: The source file in GCC containing the implementation of the Sparse Conditional
    Value Numbering (SCCVN) optimization pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d6ca7e8e1cf62734f0257cdc668da907cf3e0297
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

GCC's Sparse Conditional Constant Propagation (SCCVN) pass has been fixed to correctly associate offset computations. This change addresses a bug flagged by UBSAN, ensuring that the computation order prevents overflows and accurately reflects the intended logic, thereby improving the robustness of the optimization.
