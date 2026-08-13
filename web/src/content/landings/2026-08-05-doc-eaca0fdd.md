---
project: gcc
subsystem: doc
patch_id: null
tags:
- documentation
- vectorization
commit_hash: eaca0fdd031bbed1d2ff7dd86c3adfecef1c51cc
source_type: github
author: Kyrylo Tkachov
headline: Documentation clarifies lane freedom for widen sum reductions
tldr: Documentation now accurately describes the lane freedom in widening sum reduction
  patterns, ensuring correct implementation by ports.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `reduc_widen_ssum`/`usum` patterns and `WIDEN_SUM_EXPR` are used
  by the vectorizer for reassociable reductions. Previously, documentation implied
  strict element-wise accumulation, but these patterns allow for regrouping of input
  elements before accumulation, as long as intermediate sums do not overflow. This
  change clarifies that `widen_[us]sum` names are distinct and reserved for lane-preserving
  operations, ensuring correct interpretation by port maintainers.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eaca0fdd031bbed1d2ff7dd86c3adfecef1c51cc
date: '2026-08-05'
is_stub: true
stub_reason: low_score
---

The documentation for `reduc_widen_ssum` and `reduc_widen_usum` patterns has been updated to clarify that the assignment of input elements to accumulator elements is unconstrained. This change ensures that ports understand they can regroup input elements, for example, using pairwise widening adds. It also emphasizes that intermediate sums must not overflow and reserves `widen_[us]sum` names for lane-preserving patterns. The `WIDEN_SUM_EXPR` in `tree.def` now also reflects this documentation.
