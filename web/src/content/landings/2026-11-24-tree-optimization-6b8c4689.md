---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- SCEV
- overflow
- undefined behavior
commit_hash: 6b8c4689d99d36dc4e849a97bcf14b200d5d47cb
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fixes undefined behavior in SCEV overflow cases'
tldr: Addresses multiple PRs by improving Signed-Exponent-Logarithmic (SCEV) handling
  of overflow in character recurrence relations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change consolidates and generalizes fixes for undefined behavior
  arising from `CHREC_RIGHT` overflow within the scalar evolution (SCEV) analysis.
  Previously, specific constant-minus-character recurrence (`CST - CHREC`) overflow
  handling was spread across multiple files. These fixes are now centralized in `chrec_fold_plus_poly_poly`
  and `scev_dfs::add_to_evolution_1`, ensuring that `build_polynomial_chrec` correctly
  returns `chrec_dont_know` when `CHREC_RIGHT` overflows, rather than producing incorrect
  evolution information.
primer_glossary:
- term: SCEV
  definition: Scalar Evolution analysis, a GCC pass that determines properties of
    loop-invariant values, such as arithmetic progressions (character recurrences).
- term: CHREC
  definition: Character Recurrence, a type of arithmetic progression analyzed by SCEV,
    typically involving a starting value, a step, and a count.
- term: CHREC_RIGHT
  definition: Represents the right-hand side of a character recurrence, often related
    to the step value or an overflowed term.
- term: undefined behavior (UB)
  definition: Program behavior that results from an implementation-defined or unspecified
    condition, or a violation of an instruction, in which case the C and C++ standards
    impose no requirements on the behavior.
- term: chrec_dont_know
  definition: A return value from SCEV functions indicating that the evolution of
    a value cannot be determined, often due to complexity or overflow.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6b8c4689d99d36dc4e849a97bcf14b200d5d47cb
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This commit refactors the handling of Signed-Exponent-Logarithmic (SCEV) overflow cases related to character recurrence relations, addressing issues reported in PRs 128482, 125652, and 121370. It moves fixes for constant-minus-character recurrence handling into a more generic location, `chrec_fold_plus_1`, ensuring that overflow conditions are now correctly caught and lead to `chrec_dont_know` when `CHREC_RIGHT` overflows, thus preventing undefined behavior.
