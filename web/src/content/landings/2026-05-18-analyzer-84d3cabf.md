---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- refactor
- code cleanup
commit_hash: 84d3cabfdacb383fd18a6f5f37e04b2d1bf098e4
source_type: github
author: David Malcolm
headline: 'Analyzer: Remove unused field in exploded_node.'
tldr: The `exploded_node::m_num_processed_stmts` field in the GCC static analyzer
  is no longer used and has been removed.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC static analyzer represents the state of its exploration using
  an `exploded_graph`, composed of `exploded_node` instances. This commit removes
  the `m_num_processed_stmts` field from `exploded_node`, as it became redundant after
  refactoring in `r16-6063-g0b786d961d4426`. This simplifies the internal data structures
  of the analyzer.
primer_general: The GCC static analyzer explores possible execution paths in a program.  It
  uses a graph-like structure to represent the different states the program can be
  in. This commit removes an unused field from one of the data structures used to
  represent these states. Removing unused fields makes the code cleaner and potentially
  slightly reduces memory usage.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/84d3cabfdacb383fd18a6f5f37e04b2d1bf098e4
date: '2026-05-18'
is_stub: false
---

An unused field, `exploded_node::m_num_processed_stmts`, has been removed from the `exploded_node` class in the GCC static analyzer. This field, which tracked the number of statements processed, became redundant in a previous commit. Removing it simplifies the code and reduces memory usage.
