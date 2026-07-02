---
project: gcc
subsystem: gcc/aarch64
patch_id: null
tags:
- aarch64
- sve
- sme
- intrinsics
commit_hash: f1fb9dec32d5194b54ac05f7a5423213deabee81
source_type: github
author: Artemiy Volkov
headline: 'AArch64: Add zeroing forms for predicated SVE FP-to-integer conversions'
tldr: The compiler now supports zeroing predication for SVE FP-to-integer conversion
  instructions under SVE2.2 or SME2.2.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: SVE2.2 and SME2.2 add zeroing predication to FP-to-integer conversion
  instructions FCVTZU and FCVTZS. This commit modifies RTL patterns using the SVE_COND_FCVTI
  iterator to include a new alternative for zeroing predication, enabled when ``sve2p2_or_sme2p2``
  is true.
primer_general: The Scalable Vector Extension (SVE) is an Arm architecture extension
  that allows vector instructions to operate on vectors of varying lengths. Predication
  is a feature that allows vector instructions to be conditionally executed based
  on a predicate vector. Zeroing predication is a form of predication where inactive
  lanes in the destination vector are set to zero. This commit adds support for zeroing
  predication to SVE FP-to-integer conversion instructions, enabled under SVE2.2 or
  SME2.2.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f1fb9dec32d5194b54ac05f7a5423213deabee81
date: '2026-01-14'
is_stub: false
---

The compiler now supports zeroing predication for SVE FP-to-integer conversion instructions under SVE2.2 or SME2.2. A new alternative is added to patterns involving the SVE_COND_FCVTI iterator and accepting an independent value as the merge operand. The new alternative has the new zeroing-predication forms as the output string and is only enabled when sve2p2_or_sme2p2 is true in the target architecture.
