---
project: gcc
subsystem: range-op
patch_id: null
tags:
- optimization
- performance
commit_hash: 91e9ceecaa124cb2b38ca8db798055e461f4aa5a
source_type: github
author: linden
headline: 'range-op: avoid copying the bounds in operator_div::wi_fold'
tldr: Remove redundant copies of bounds parameters in operator_div::wi_fold.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `range-op.cc`, the `operator_div::wi_fold` function accepted four
  `const` references to `range_t` objects representing bounds. For clarity, it copied
  these into local variables with more descriptive names. This commit eliminates these
  copies by renaming the parameters directly, reducing overhead without affecting
  the function's logic or the Range Optimization pass's behavior.
primer_glossary:
- term: range-op
  definition: A GCC optimization pass that analyzes and manipulates the possible range
    of values for variables. It uses range information to perform optimizations like
    constant folding or dead code elimination.
- term: const reference
  definition: A way to pass arguments to functions in C++ that allows the function
    to access the argument's value without making a copy, while also guaranteeing
    that the function will not modify the original argument.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/91e9ceecaa124cb2b38ca8db798055e461f4aa5a
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

The operator_div::wi_fold function in range-op.cc unnecessarily copied its four const-reference bound parameters into local variables for naming clarity. This commit removes these copies by directly using the parameter names, which have been updated for better readability. This change offers a minor performance improvement by avoiding redundant data copies.
