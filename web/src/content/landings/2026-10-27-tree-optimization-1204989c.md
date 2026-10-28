---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- pta
commit_hash: 1204989c4ff5061576538a51df826c6c023f18cd
source_type: github
author: Richard Biener
headline: PTA solver issue with node merging corrected
tldr: Corrects an issue in the Point-to-Analysis solver where merging nodes failed
  to properly forward target node solutions to successors.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Andersen PTA solver in GCC, specifically in `pta-andersen.cc`,
  has a bug in `merge_graph_nodes`. When merging two nodes, if new successor edges
  are created, the solver must ensure that the analysis result (solution) for the
  target node is re-evaluated and propagated to these new successors. This commit
  corrects `unify_nodes` to mark the target node as changed if new successor edges
  are added, triggering a re-evaluation.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1204989c4ff5061576538a51df826c6c023f18cd
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

The Point-to-Analysis (PTA) solver in GCC has been fixed to correctly handle node merging. Previously, when two graph nodes were merged, the solver failed to ensure that the target node's solution was propagated to any new successors. This change modifies the `pta-andersen.cc` file to mark nodes as changed when new successor edges are introduced during a merge, ensuring accurate analysis. A new test case `pr128198.c` has been added.
