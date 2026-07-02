---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
commit_hash: 7b5a05667c8e40bec5e070b1638d3b3882f7c78e
source_type: github
author: Richard Biener
headline: Fix sorted_array_from_bitmap_set to compute value graph entries first
tldr: Improve topological sorting of expressions by ensuring value graph entries are
  computed before building the sorted set, reducing iteration.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `sorted_array_from_bitmap_set` function, used within `tree-ssa-pre.cc`,
  aims to provide a topological sort of expressions represented in a bitmap set. This
  commit addresses a flaw where the required knowledge of the value graph's entries
  was missing, leading to incomplete sorting. By pre-computing these entries, the
  pass can now correctly order expressions, potentially improving the efficiency of
  subsequent optimizations that rely on this ordering.
primer_glossary:
- term: topological sorting
  definition: An ordering of nodes in a directed acyclic graph such that for every
    directed edge from node A to node B, node A comes before node B in the ordering.
    In compilers, this is often used to order operations or expressions based on their
    dependencies.
- term: bitmap set
  definition: A data structure that represents a set of elements using a bit array.
    Each bit corresponds to a potential element, and its value (0 or 1) indicates
    whether the element is present in the set. This is memory-efficient for dense
    sets.
- term: value graph
  definition: A graph representation where nodes represent values or expressions,
    and edges represent relationships between them, such as data flow or dependencies.
    It's used in compiler optimizations to analyze and manipulate program values.
- term: tree-ssa-pre
  definition: A compiler pass within GCC that performs optimizations on the SSA (Static
    Single Assignment) form of the code. 'pre' likely refers to 'pre-pass' or 'preprocessing'
    within the SSA framework, focusing on initial transformations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7b5a05667c8e40bec5e070b1638d3b3882f7c78e
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

The `sorted_array_from_bitmap_set` function in `tree-ssa-pre.cc` has been modified to fix an issue where it failed to correctly topologically sort expressions. Previously, it lacked knowledge of the value graph's entries. The update ensures these entries are computed first, which should reduce the amount of iteration needed for sorting.
