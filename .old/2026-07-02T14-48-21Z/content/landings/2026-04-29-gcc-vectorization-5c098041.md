---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- gcc
- vectorization
- x86
- testing
commit_hash: 5c09804150b2da7c18751905e7f1a23b7357bc06
source_type: github
author: Richard Biener
headline: Adjust x86 vectorization tests for cost comparison.
tldr: GCC test suite updates include duplicating vectorization tests with explicit
  cost comparison flags to ensure accurate behavior.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `gcc.target/i386/vect-epilogues-2.c` and `gcc.target/i386/vect-pr113078.c`
  by duplicating them into `-2b.c` and `-pr113078b.c` variants.  The original versions
  are configured with `--param ix86-vect-compare-costs=0`, while the new variants
  use `--param ix86-vect-compare-costs=1`.  This isolates the impact of the cost comparison
  model on the selection of SSE vector sizes in vector epilogues, specifically when
  generic tuning is enabled.  The change highlights the sensitivity of the vectorizer
  to cost modeling and target-specific tuning parameters.
primer_general: Vectorization in compilers transforms scalar operations into vector
  operations for performance. Vector epilogues handle remaining elements in a loop
  when the iteration count isn't a multiple of the vector length.  GCC uses a cost
  model to estimate the performance of different vectorization strategies. This commit
  adjusts tests to explicitly enable or disable the cost comparison, ensuring the
  vectorizer behaves as expected with and without this feature enabled.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5c09804150b2da7c18751905e7f1a23b7357bc06
date: '2026-04-29'
---

Several x86 vectorization tests have been adjusted to account for the enabled vector cost comparison feature. The changes involve duplicating test cases, with one version explicitly disabling cost comparison (`--param ix86-vect-compare-costs=0`) and the other enabling it (`--param ix86-vect-compare-costs=1`). This allows verifying the behavior of the vectorizer under both configurations, particularly for epilogue selection.
