---
project: gcc
subsystem: wide-int
patch_id: null
tags:
- optimization
- wide-int
- C++
commit_hash: cee53ed42c753a0c936e005b7dd15f029ca34da7
source_type: github
author: Kael Andrew Alonzo Franco
headline: 'wide-int: Use return 1 instead of return len.'
tldr: Optimizes wide-integer canonization by returning a constant 1, potentially speeding
  up C++ optimizers.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In the `wide-int` library, the `canonize` function was observed to
  always have `len` equal to 1 in a specific code path. This commit replaces `return
  len;` with `return 1;` to eliminate a redundant variable read, offering a micro-optimization
  that may benefit C++ frontends that heavily utilize the `wide-int` library for arbitrary-precision
  arithmetic, particularly during optimization phases.
primer_glossary:
- term: wide-int
  definition: GCC's internal library for handling arbitrary-precision integers, used
    for representing values that exceed standard integer types during compilation.
- term: canonize
  definition: A function within the `wide-int` library that normalizes or simplifies
    an arbitrary-precision integer representation. In this context, it likely ensures
    a canonical form for integers of a specific size.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cee53ed42c753a0c936e005b7dd15f029ca34da7
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

This commit simplifies the `canonize` function in `wide-int.cc` by directly returning 1 instead of the variable `len`. Since `len` is known to be 1 in this context, this change is a minor optimization that can contribute to faster C++ compilation times by removing a redundant variable lookup.
