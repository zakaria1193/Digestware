---
project: gcc
subsystem: lim/cselim
patch_id: null
tags:
- optimization
- compiler internals
commit_hash: e4d36a3fc154fe500bdfd7835ec9fe4d5e41fb42
source_type: github
author: Andrea Pinski
headline: 'lim/cselim: Use lhs_could_trap_p directly'
tldr: Simplifies code in the loop and conditional select elimination passes by directly
  using the specialized trapping check.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `lim/cselim` passes (Loop Invariant Motion and Conditional Select
  Elimination) perform optimizations within the GCC compiler. They previously called
  a general `tree_could_trap_p` and then manually checked if the expression was a
  `decl` or `string` to approximate LHS trapping behavior. This commit replaces those
  checks with direct calls to `lhs_could_trap_p`, which now correctly handles LHS
  trapping analysis as improved by a prior patch.
primer_glossary:
- term: lim/cselim
  definition: GCC compiler passes for Loop Invariant Motion and Conditional Select
    Elimination, which optimize loops and conditional assignments, respectively.
- term: lhs_could_trap_p
  definition: A function within GCC's tree-eh pass that checks if an expression on
    the left-hand side (LHS) of an assignment could cause a runtime trap or exception.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e4d36a3fc154fe500bdfd7835ec9fe4d5e41fb42
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

The loop and conditional select elimination passes in GCC now directly use `lhs_could_trap_p` instead of a more general trapping check followed by additional tests. This simplifies the code and ensures consistent handling of potentially trapping left-hand side expressions, improving maintainability and correctness.
