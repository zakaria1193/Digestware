---
project: gcc
subsystem: tree-ssa-threadbackward
patch_id: null
tags:
- debugging
- refactor
- backthreader
commit_hash: a19952e8fc0c372097d11017c79a02519c220f7f
source_type: github
author: Aldy Hernandez
headline: 'backthreader: dump the profitability path in one place'
tldr: Backthreader's profitability path dumping is consolidated for easier code modification.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-threadbackward.cc`, the `back_threader_profitability::possibly_profitable_path_p`
  function previously interleaved debugging dumps of the profitability path with the
  loop that counted the path's instructions. This commit separates these concerns
  by moving the path dumping logic to execute solely after the counting loop completes.
  This makes it easier to refactor the counting loop without simultaneously impacting
  the dump output, and is a preparatory step for reintroducing per-block statistics
  to the profitability calculation.
primer_glossary:
- term: backthreader
  definition: A GCC optimization pass that reorders instructions to improve parallelism.
    It analyzes execution paths to determine the most profitable reordering strategies.
- term: profitability path
  definition: A sequence of basic blocks within a control flow graph that the backthreader
    pass analyzes to determine if instruction reordering would be beneficial.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a19952e8fc0c372097d11017c79a02519c220f7f
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

The logic for dumping the profitability path in the backthreader pass has been moved to occur after the instruction counting loop, rather than interleaving with it. This reorganization simplifies modifications to the counting loop and prepares for the return of per-block statistics.
