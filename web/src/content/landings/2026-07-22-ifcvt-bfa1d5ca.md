---
project: gcc
subsystem: ifcvt
patch_id: null
tags:
- refactor
- optimization
commit_hash: bfa1d5cae14f9ce8bf399e6a3751174417970869
source_type: github
author: Kyrylo Tkachov
headline: 'ifcvt: Consolidate cost estimation for noce original regions.'
tldr: Consolidates redundant cost estimation logic in the ifcvt pass for better code
  reuse.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `noce_process_if_block` function in the ifcvt pass computed the
  cost of a branch removal twice: once for the multiple-set candidate and once for
  the single-set path. Both computations involved a branch-probability-weighted average
  (for speed) or sum (for size) of the two arms. This commit extracts this common
  logic into a new function, `noce_original_region_cost`. It renames the `old_cost`
  variable to `base_cost` and computes the speed-related estimate only once, reducing
  redundancy.'
primer_glossary:
- term: ifcvt
  definition: The GCC optimization pass that converts conditional branches into conditional
    moves or other branchless constructs to improve performance.
- term: noce
  definition: Likely an abbreviation for 'No Conditional Execution' or a related concept
    within the ifcvt pass, focusing on branchless code generation.
- term: cost estimation
  definition: The process of evaluating the potential performance impact (e.g., execution
    time, instruction count) of a code transformation or optimization.
- term: branch probability
  definition: The likelihood that a conditional branch instruction will be taken,
    often predicted by the compiler based on profiling or heuristics.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfa1d5cae14f9ce8bf399e6a3751174417970869
date: '2026-07-22'
is_stub: true
stub_reason: low_score
---

This commit refactors the GCC ifcvt pass by consolidating redundant cost estimation logic in `noce_process_if_block`. Previously, the cost of a removed branch was estimated twice: once for multiple-set and once for single-set paths, using similar calculations. The new `noce_original_region_cost` function centralizes this calculation. The commit also renames `old_cost` to `base_cost` for clarity and hoists a common speed test, improving code maintainability without functional changes.
