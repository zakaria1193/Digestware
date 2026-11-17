---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
- gcc
- tree-ssa
commit_hash: a2d7bbb3494b789291d90d89e865b5ff063493e4
source_type: github
author: Richard Biener
headline: Re-associative pass avoids truncating pow exponents
tldr: Fixes GCC's re-associative optimization pass to correctly handle large exponents
  in power functions, preventing incorrect code generation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-reassoc.cc` pass, specifically within `acceptable_pow_call`
  and `attempt_builtin_powi`, previously truncated `HOST_WIDE_INT` exponents to `unsigned
  int` when storing them in `operand_entry::count`. This commit rectifies this by
  widening `operand_entry::count` and adding checks to ensure the exponent fits the
  `__builtin_powi` argument type, thus preventing zeroing of large exponents and correctly
  splitting oversized powers. This resolves `PR tree-optimization/128453`.
primer_glossary:
- term: re-associative optimization
  definition: A compiler optimization pass that rearranges the order of associative
    operations (like addition and multiplication) to potentially improve performance
    or enable other optimizations. It operates on the compiler's intermediate representation.
- term: HOST_WIDE_INT
  definition: A GCC internal type representing the widest integer type available on
    the host machine where the compiler is running. Used for intermediate calculations
    that might exceed standard integer types.
- term: __builtin_powi
  definition: A GCC built-in function that computes a power with an integer exponent.
    It is often used by the compiler as an optimization target for expressions involving
    powers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2d7bbb3494b789291d90d89e865b5ff063493e4
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's re-associative optimization pass where large integer exponents in `pow` calls were being truncated. The `operand_entry::count` field was too small, causing exponents to wrap around to zero or be mishandled by `attempt_builtin_powi`. The fix widens the `count` field and adds checks to ensure exponents fit within the target type for `__builtin_powi`, preventing incorrect removal of `pow` calls and ensuring powers exceeding the exponent limit are split correctly.
