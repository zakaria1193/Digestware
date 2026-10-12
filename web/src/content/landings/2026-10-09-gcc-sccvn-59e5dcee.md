---
project: gcc
subsystem: gcc/sccvn
patch_id: null
tags:
- optimization
- refactor
commit_hash: 59e5dcee5375614cf1cc58e97dcc04f63bc9b519
source_type: github
author: Aldy Hernandez
headline: 'sccvn: add a driver object for the value numbering walk [PR126904]'
tldr: Refactors SCC value numbering to use a driver object for future enhancements.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SCC value numbering infrastructure, previously spread across free
  functions like `do_rpo_vn_1`, `run_rpo_vn`, etc., is now consolidated under a `vn_driver`
  class. This abstraction is intended to facilitate future extensions, particularly
  for integrating jump threading directly within the FRE (Forward Replaceable Expression)
  pass. The `vn_driver` manages the state and traversal logic for value numbering,
  allowing for persistent VN data beyond a single walk.
primer_glossary:
- term: SCC
  definition: Strongly Connected Component. In compiler theory, a subgraph where every
    vertex is reachable from every other vertex. Used in value numbering to identify
    loops or regions with cyclic dependencies.
- term: Value Numbering (VN)
  definition: A compiler optimization technique that assigns a unique number (value
    number) to equivalent expressions. This allows the compiler to identify and eliminate
    redundant computations.
- term: FRE
  definition: Forward Replaceable Expression. A compiler optimization pass that identifies
    and replaces redundant expressions with previously computed values, often relying
    on value numbering.
- term: Jump Threading
  definition: An optimization that rearranges control flow by eliminating branches
    that always go to the same successor, making code faster by reducing branching
    overhead.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/59e5dcee5375614cf1cc58e97dcc04f63bc9b519
date: '2026-10-09'
is_stub: false
stub_reason: ''
---

The strongly connected components (SCC) value numbering (VN) pass has been refactored to encapsulate its driving functions within a new `vn_driver` class. This change, driven by PR126904, does not alter current functionality or output but prepares the groundwork for implementing jump threading within the FRE pass, where the lifetime of value numbers is critical.
