---
project: gcc
subsystem: tree-ssa-threadbackward
patch_id: null
tags:
- debugging
- backthreader
commit_hash: 36aa66e23cda4ddd4650b64fae66bf1c77435a30
source_type: github
author: Aldy Hernandez
headline: 'backthreader: dump the per-block insn count again'
tldr: backthreader now dumps per-block instruction counts for debugging profitability
  analysis.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit reverts a change that removed per-block instruction counts
  from the `back_threader_profitability::possibly_profitable_path_p` function in `tree-ssa-threadbackward.cc`.
  The counts are now dumped again to aid in debugging the profitability heuristics
  of the backthreader pass. This debugging information is crucial for understanding
  why certain paths are considered profitable or not, especially after recent refactorings.
primer_glossary:
- term: backthreader
  definition: A GCC optimization pass that reorders instructions to improve parallelism.
    It analyzes execution paths to determine the most profitable reordering strategies.
- term: basic block
  definition: A contiguous sequence of zero or more three-address instructions in
    which control enters at the beginning and leaves at the end without halt or possibility
    of branching except at the end.
- term: instruction count
  definition: The number of machine instructions within a given code segment, such
    as a basic block or a function. This is a key metric for performance analysis
    and optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/36aa66e23cda4ddd4650b64fae66bf1c77435a30
date: '2026-09-09'
is_stub: true
stub_reason: low_score
---

This commit reintroduces the dumping of per-block instruction counts within the backthreader's profitability analysis. This change helps in debugging and understanding the profitability calculations by providing detailed information about instruction distribution across basic blocks.
