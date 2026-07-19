---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
commit_hash: 3bf0224b877c2975e02330de88165a94c7ece16f
source_type: github
author: Andrew MacLeod
headline: Recompute relations during relation query walk.
tldr: Improved value-relation queries by recomputing relations during the DOM walk.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Inside GCC's value-relation analysis, the `dom_oracle` tracks relationships
  between values. This patch modifies `find_relation_dom` to call a new function,
  `recomputed_relation`. This function revisits dominator tree edges, re-evaluating
  the relationships on these edges if they appear promising. This is an optimization
  to refine relation discovery, particularly useful when previous relation computations
  might have been imprecise due to intermediate transformations or initial heuristic
  assumptions.
primer_glossary:
- term: DOM walk
  definition: A traversal of the Dominator Tree. In compiler theory, a dominator tree
    represents the control flow graph's dominance relationships, where a node dominates
    another if all paths from the entry to the second node must pass through the first.
- term: dom_oracle
  definition: A data structure or class in GCC used to query and maintain information
    about dominator relationships and value relations within a program.
- term: value-relation
  definition: In compiler optimization, a value-relation describes how the value of
    one variable or expression relates to another (e.g., equality, inequality, or
    a specific mathematical function).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3bf0224b877c2975e02330de88165a94c7ece16f
date: '2026-07-16'
is_stub: false
stub_reason: ''
---

This commit enhances the `dom_oracle` by introducing a mechanism to recompute potential relations during a DOM walk. When querying relationships between values, the system now re-evaluates promising edges, potentially discovering more accurate relationships. This change aims to improve the precision of value-relation analysis, addressing a bug where specific relations were not being correctly identified.
