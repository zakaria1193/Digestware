---
project: gcc
subsystem: tree-optimization/ifcvt
patch_id: null
tags:
- optimization
- SSA
commit_hash: c7a7934c60c7e0112352c20efe4677a34a5b0cb6
source_type: github
author: Tamar Christina
headline: Fix single use checks in factor_out_operators
tldr: Corrects SSA analysis in ifcvt to properly handle single-use PHI nodes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ifcvt` optimization pass, specifically in `tree-if-conv.cc`, relies
  on accurate Static Single Assignment (SSA) form. This patch corrects how `factor_out_operators`
  checks for single-use PHI arguments, reverting a workaround that masked an SSA issue.
  The fix ensures that only genuinely single-use PHI nodes are considered, aligning
  the pass's behavior with its original intent.
primer_glossary:
- term: ifcvt
  definition: If conversion is a compiler optimization pass that transforms conditional
    code into equivalent code without explicit branches, often by using conditional
    moves or predicated operations. It aims to improve performance by reducing control
    flow overhead.
- term: SSA
  definition: Static Single Assignment (SSA) is an intermediate representation property
    where every variable is assigned a value exactly once. This simplifies many compiler
    analyses and optimizations by making data flow explicit. SSA form is typically
    constructed and maintained by the compiler's front-end and middle-end passes.
- term: PHI node
  definition: In SSA form, a PHI node (or Phi function) is used to merge values from
    different control flow paths. It takes multiple arguments, each corresponding
    to a predecessor block in the control flow graph, and selects the appropriate
    value based on which predecessor was executed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c7a7934c60c7e0112352c20efe4677a34a5b0cb6
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in the `factor_out_operators` function within the ifcvt (if conversion) optimization pass. The issue involved incorrect handling of single-use PHI nodes due to a temporary hack addressing broken SSA. By removing this hack and ensuring correct SSA checks, the optimization now functions as intended, resolving a test case failure.
