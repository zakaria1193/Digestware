---
project: gcc
subsystem: gcc/ivopts
patch_id: null
tags:
- optimization
- loop
- enum
- bitint
commit_hash: d6d21c3abd31b73146df15b626da544eb4a8509a
source_type: github
author: Andrew Pinski
headline: 'Ivopts: Improve doloop support for enum and bitint types'
tldr: Extends doloop recognition to enum and bitint types by converting them to a
  full mode integer type.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The ivopts pass optimizes loops by recognizing induction variables
  and transforming the loop into a doloop. This commit modifies `add_iv_candidate_for_doloop`
  to handle enum and bitint types, which are now returned by `ninter`. The code converts
  non-integer or non-full mode integer types to a full mode integer type. Search terms:
  GCC ivopts doloop induction variable.'
primer_general: 'Loop optimization is a crucial part of compiler optimization, where
  the compiler identifies patterns in loops to improve performance. One such pattern
  is the ''doloop'', which has a simple and predictable structure. Induction variable
  optimization identifies variables that increment or decrement in each loop iteration.
  This commit enhances the compiler''s ability to recognize doloops when the loop
  counter is an enum or bitint type, expanding the scope of this optimization. Search
  terms: GCC ivopts doloop induction variable.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d6d21c3abd31b73146df15b626da544eb4a8509a
date: '2026-04-27'
---

This commit extends the loop induction variable (iv) optimization to handle enum and bitint types. Previously, the `add_iv_candidate_for_doloop` function only supported integer types. This commit modifies the function to accept non-integer types, converting them to a full mode integer type before processing. This change enables doloop optimization for loops using enum and bitint types as induction variables.
