---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa-reassoc
- __builtin_pow
- floating-point
commit_hash: 34e1afc66c3239bf5d5dbe8005f8930d84fa20bf
source_type: github
author: Richard Biener
headline: Restrict power exponent checks to constant integers
tldr: Fixes `__builtin_pow` handling by ensuring exponent checks only apply to constant
  integer exponents.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit revises `stmt_is_power_of_op` within `tree-ssa-reassoc.cc`
  to enforce that it only identifies power operations with constant integer exponents
  when undistributing factors. Previously, it would incorrectly process non-constant
  or floating-point exponents, leading to truncation (e.g., `2.5` to `2`) and subsequent
  incorrect decrements by `decrement_power`. This caused miscompilations in expressions
  involving `__builtin_pow` and multiplication chains. The change ensures that only
  valid, constant integer exponents are considered for factor removal, preventing
  these errors and potential…
primer_glossary:
- term: undistribute
  definition: An optimization step that breaks down a combined operation (like a power)
    into its constituent parts, often to enable other optimizations like reassociation.
- term: reassociation
  definition: An optimization that rearranges the order of operations (e.g., changing
    `(a + b) + c` to `a + (b + c)`) without changing the result, typically to improve
    performance or enable further optimizations.
- term: SSA
  definition: Static Single Assignment. An intermediate representation where every
    variable is assigned exactly once, simplifying many dataflow analyses and optimizations.
- term: ICE
  definition: Internal Compiler Error. An error that occurs within the compiler itself,
    often due to unexpected conditions or bugs in the compiler's logic.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/34e1afc66c3239bf5d5dbe8005f8930d84fa20bf
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This commit corrects a miscompilation issue involving `__builtin_pow` and the undistribution of factors from multiplication chains. Previously, the `stmt_is_power_of_op` function incorrectly processed non-constant or non-integer exponents in `pow` calls, leading to truncation and incorrect results. The fix modifies `stmt_is_power_of_op` to strictly require a constant integer exponent, ensuring that factors are removed from elsewhere in the chain and preventing misinterpretation of mathematical expressions.
