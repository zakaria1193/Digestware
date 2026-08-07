---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- refactoring
- tree-optimization
commit_hash: 2ec8e0de71cf273abcefba70deb9210eb0239e48
source_type: github
author: Aldy Hernandez
headline: Remove redundant freestanding `contains_zero_p` function.
tldr: Cleans up range analysis code by removing a redundant function.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The standalone `irange` overload for `contains_zero_p` in `value-range.h`
  has been removed. All its former callers in `range-op.cc` and `range-op-float.cc`
  have been updated to use the equivalent `irange::contains_zero_p` method. This cleanup
  eliminates code duplication and streamlines the range analysis infrastructure.
primer_glossary:
- term: range analysis
  definition: A compiler optimization technique that determines the possible range
    of values a variable can hold during program execution.
- term: redundant
  definition: Unnecessary or superfluous; performing a function that is already accomplished
    by another part of the system.
- term: standalone
  definition: Existing or functioning independently, not part of a larger system or
    structure.
- term: method
  definition: A function associated with an object or class in object-oriented programming.
- term: vranges
  definition: An internal GCC data structure or set of structures used to represent
    value ranges during optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2ec8e0de71cf273abcefba70deb9210eb0239e48
date: '2026-08-06'
is_stub: true
stub_reason: low_score
---

This commit refactors the range analysis code by removing a standalone `contains_zero_p` function. Since the `vranges` representation now provides its own `contains_zero_p` method, the separate function had become redundant. The change updates callers to use the method instead and removes the old function, simplifying the codebase.
