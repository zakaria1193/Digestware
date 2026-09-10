---
project: gcc
subsystem: backthreader
patch_id: null
tags:
- performance
- analysis
commit_hash: 7f7bf82265941bce90c63a77aa5ab447fc4f1f90
source_type: github
author: Aldy Hernandez
headline: 'backthreader: use a BB flag for the visited-block set'
tldr: Replaces hash set with a basic block flag for tracking visited blocks, improving
  performance.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `back_threader`'s `find_paths_to_names` function previously used
  `m_visited_bbs` (a `hash_set<basic_block>`) to track visited blocks during path
  traversal. This commit replaces it with `m_visited_flag` (a `bb_auto_flag`). Since
  the flag is only used to check membership within the current function's CFG and
  is reset appropriately by `find_paths_to_names` (making the per-block reset in `maybe_thread_block`
  redundant), the flag offers better performance with no loss of correctness. It avoids
  heap allocation and hash lookups.
primer_glossary:
- term: backthreader
  definition: A GCC pass that performs backward analysis, starting from a destination
    and working backward through the control flow graph.
- term: basic block
  definition: A sequence of instructions in a program with a single entry point and
    a single exit point. Control flow graphs are composed of basic blocks.
- term: CFG
  definition: Control Flow Graph, a directed graph representing all execution paths
    within a program or function. Nodes are basic blocks, and edges represent jumps
    or transfers of control.
- term: hash set
  definition: A data structure that stores unique elements and provides fast average-time
    complexity for insertion, deletion, and lookup operations using a hash function.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f7bf82265941bce90c63a77aa5ab447fc4f1f90
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

The backwards threader pass in GCC previously used a `hash_set<basic_block>` to track visited blocks during path exploration. This incurred a hash lookup cost on entry and exit of each basic block. This commit replaces the hash set with a simple flag on the basic block itself, as the set's usage is confined to the current function and the control flow graph doesn't change. This change reduces overhead and simplifies the implementation.
