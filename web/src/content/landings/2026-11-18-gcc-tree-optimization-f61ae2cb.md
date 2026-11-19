---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- undefined-behavior
- gcc
commit_hash: f61ae2cb8d38929cb3761631160fdfa58e59fdc4
source_type: github
author: Richard Biener
headline: Avoid undefined behavior in CSE of -x / y.
tldr: GCC now correctly handles CSE of negated division/multiplication operands to
  avoid UB.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, the `visit_nary_op` function performs common
  subexpression elimination. This patch modifies the handling of division and multiplication
  operations to correctly identify and match negated operands. It specifically checks
  if a negated operand is available before attempting to build or simplify it, especially
  when negation could lead to UB. This is crucial for correctly folding expressions
  involving negation and avoiding incorrect transformations when operands like `INT_MIN`
  are involved.
primer_glossary:
- term: CSE
  definition: Common Subexpression Elimination, an optimization technique that identifies
    and replaces identical expressions with a single temporary variable.
- term: undefined behavior (UB)
  definition: Behavior of a program that results from an operation or condition that
    violates a language or C standard, for which the standard imposes no requirements.
    Compilers assume UB does not happen, which can lead to unexpected optimizations.
- term: INT_MIN
  definition: The smallest representable value for a signed integer type.
- term: IL
  definition: Intermediate Language, a representation of a program between the source
    code and the machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f61ae2cb8d38929cb3761631160fdfa58e59fdc4
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

The common subexpression elimination (CSE) pass in GCC incorrectly handled cases like `-x / y` when trying to match it with `x / y`. This commit ensures that the pass checks for the literal availability of the negated operand and avoids issues with undefined behavior (UB) that can arise from negation, particularly with `INT_MIN`.
