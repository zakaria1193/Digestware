---
project: gcc
subsystem: tree-cfgcleanup
patch_id: null
tags:
- tree-cfgcleanup
- optimization
- bugfix
- phi
- ssa
commit_hash: ec79b0779b6eeb9ef3b8a45f46a596cbb75a7844
source_type: github
author: Andrew Pinski
headline: Tree-CFGCleanup Retains Forwarder Blocks with PHIs and Abnormal Uses
tldr: The compiler now avoids incorrectly removing forwarder blocks that contain PHI
  nodes with abnormal uses, preventing potential code generation issues.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/125396 by preventing `maybe_remove_forwarder_block`
  from removing blocks where `bb_phis_references_abnormal_uses` returns true. This
  ensures that forwarder blocks with PHIs that have arguments with abnormal uses are
  not incorrectly removed, which could lead to overlapping live ranges.
primer_general: GCC's compiler performs several optimization passes to improve the
  generated code. One of these passes, tree-cfgcleanup, simplifies the control flow
  graph of the program. This commit fixes a bug in this pass that could cause the
  compiler to incorrectly remove certain blocks of code (forwarder blocks) if they
  contained special instructions (PHI nodes) and had unusual control flow patterns
  (abnormal uses). This fix prevents potential errors and ensures that the compiler
  generates correct code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ec79b0779b6eeb9ef3b8a45f46a596cbb75a7844
date: '2026-05-20'
is_stub: false
---

The tree-cfgcleanup pass in GCC could incorrectly remove forwarder blocks containing PHI nodes if the PHI arguments had abnormal uses. This commit fixes this issue by adding a check to ensure that forwarder blocks with PHIs referencing SSA names with abnormal uses are not removed. This prevents potential issues with live range overlap and incorrect code generation during optimization.
