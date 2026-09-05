---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- bugfix
commit_hash: 31b8c15fd7608fe5bad8b105e9b5112ed18166dd
source_type: github
author: Andrew MacLeod
headline: Path ranger in tree-optimization disallowed from current_range_query.
tldr: Path ranger in GCC's tree-optimization is prevented from using current_range_query
  to avoid incorrect range calculations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `path_ranger` pass, used in GIMPLE optimization, can now provide
  incorrect range information if it relies on `current_range_query` established by
  other passes. This commit introduces `set_range_query` as the canonical way to manage
  the active `range_query` and modifies `path_ranger` to not use it, ensuring its
  analyses are self-contained and correct, especially in the context of Value Range
  Propagation (VRP).
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation (IR) used for optimization passes. It's
    a three-address code-like form.
- term: path ranger
  definition: A component within GCC's tree-optimization framework that analyzes ranges
    along execution paths.
- term: current_range_query
  definition: A mechanism within GCC's value analysis framework that provides the
    current range information for a variable.
- term: Value Range Propagation (VRP)
  definition: An optimization pass in GCC that determines the possible range of values
    for variables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/31b8c15fd7608fe5bad8b105e9b5112ed18166dd
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

A generic mechanism to set the current range query has been introduced, and the path ranger is now disallowed from using it. This prevents the path ranger from providing incorrect ranges for requests not dominated by the path it is analyzing, fixing a bug in range analysis.
