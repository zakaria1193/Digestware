---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
- optimization
- ieee754
commit_hash: ad45faeb14a4acb551ecbb61bc1b0e1f6ce500b0
source_type: github
author: Icenowy Zheng
headline: 'RISC-V: Use NaN for fmin/fmax autovec reduce initial value'
tldr: RISC-V autovectorization of fmin/fmax now uses NaN as initial reduction value
  to correctly handle all-NaN inputs.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The RISC-V autovectorization pass for `fmin`/`fmax` reductions was
  using infinity as the initial accumulator value. This commit replaces it with a
  quiet NaN. This is because operations like `fmin` and `fmax` follow IEEE754 `minimumNumber`/`maximumNumber`,
  where NaN propagates. Using NaN as the initial value ensures that if the input vector
  contains only NaNs, the result is NaN, and if it contains any non-NaN values, those
  will correctly overwrite the initial NaN.
primer_general: Compilers can often optimize code by performing operations on multiple
  data items simultaneously, a process called vectorization. When calculating the
  minimum or maximum value in a set of numbers using techniques like fmin/fmax, the
  process might involve an accumulator. This change in GCC for RISC-V processors corrects
  how this accumulator is initialized for vectorized fmin/fmax operations. Previously,
  it used infinity, which led to incorrect results if the input data contained only
  Not-a-Number (NaN) values. The fix changes the initial value to NaN, ensuring that
  the operation behaves correctly according to the IEEE754 standard, even with unusual
  inputs like all NaNs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ad45faeb14a4acb551ecbb61bc1b0e1f6ce500b0
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

Vectorized fmin/fmax reductions on RISC-V previously used infinity as the initial value. This caused incorrect NaN results when processing arrays containing only NaNs. The change updates the initial value to NaN, aligning with IEEE754 semantics and ensuring correct behavior for all-NaN or mixed-NaN/non-NaN inputs.
