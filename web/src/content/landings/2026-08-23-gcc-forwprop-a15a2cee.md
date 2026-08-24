---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- optimization
- bugfix
commit_hash: a15a2cee730ccdd5894ca6ece783f6fe27cb3e20
source_type: github
author: Andrea Pinski
headline: 'forwprop: Add LMK_INVALID and associated checks'
tldr: Improves robustness of the forward propagation pass by adding checks for invalid
  states.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The forwprop pass in GCC uses `long_mul_summand` to represent terms
  in a scalar multiplication. This commit introduces `LMK_INVALID` to signify an uninitialized
  state, preventing incorrect processing of partially formed summands. Checks are
  added to several functions within `tree-ssa-forwprop.cc` to validate the state of
  `long_mul_summand` before use, particularly when classifying chains or finding summands.
  This aims to catch potential errors early in the optimization pipeline.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a15a2cee730ccdd5894ca6ece783f6fe27cb3e20
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

This change introduces an LMK_INVALID enum value to represent an uninitialized state within the `long_mul_summand` structure. Checks are added in `long_mul_set_summand`, `long_mul_summand_compare`, `long_mul_find_summand`, and `long_mul_classify_chain` to ensure that only fully initialized `long_mul_summand` values are processed. These checks are primarily for non-release builds, enhancing debugging and stability.
