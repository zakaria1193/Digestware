---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- sve
- middle-end
- aarch64
commit_hash: 1dd02e1deffddc3b6c17b26d78569d93d8a0dac0
source_type: github
author: Tamar Christina
headline: 'middle-end: Teach ranger about POLY_INT_CST ranges for VRP'
tldr: Improves optimization of SVE-based VLA branches by enabling range analysis for
  vector length constants.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit introduces the `poly_int_indeterminate_bound` target hook
  in `target.def` and utilizes it in `value-query.cc`'s `range_query::get_tree_range`.
  This hook allows targets to specify the minimum and maximum bounds for `POLY_INT_CST`
  values. For SVE, this means the `ranger` pass can now correctly establish that `svcntb()`
  and `svcntw()` results are within architectural limits, enabling the folding of
  comparisons that are always true or false, thus improving VRP (Value Range Propagation)
  optimizations.
primer_glossary:
- term: VLA
  definition: Variable Length Array, a C99 feature allowing array sizes to be determined
    at runtime. In this context, it refers to code structures involving runtime-determined
    vector lengths.
- term: ranger
  definition: A GCC compiler pass responsible for determining the range of values
    that variables can take, used for various optimizations.
- term: VRP
  definition: Value Range Propagation, an optimization pass that determines the possible
    range of values for variables to enable further optimizations.
- term: POLY_INT_CST
  definition: A GCC internal representation for an integer constant that may vary,
    often used in symbolic computations or with variable vector lengths.
- term: SVE
  definition: Scalable Vector Extension, an ARM architecture feature that allows vector
    length to be determined at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1dd02e1deffddc3b6c17b26d78569d93d8a0dac0
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

This patch enhances GCC's `ranger` pass to better optimize branches guarded by variable-length array (VLA) constants, particularly for SVE. By introducing a `poly_int_indeterminate_bound` target hook, GCC can now understand that SVE vector length queries (`svcntb`, `svcntw`) have defined bounds. This allows the compiler to fold away known true/false comparisons, simplifying code generation for loop pre-headers and matching LLVM's optimization capabilities.
