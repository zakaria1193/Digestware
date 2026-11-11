---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- bugfix
- builtin
commit_hash: 4d11a05988d3f57e947b705ed81247654a86004d
source_type: github
author: Richard Biener
headline: Expand pow calls as multiplications when powi builtin is unavailable
tldr: GCC now expands `pow` calls with constant integer exponents into multiplications
  when `__builtin_powi` is not available for the type.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `reassoc` pass in GCC's tree optimizer incorrectly dropped calls
  to `__builtin_pow` when the exponent was a constant integer and `attempt_builtin_powi`
  failed to find a suitable `__builtin_powi` intrinsic for the base type (e.g., `_Float64`).
  The `try_special_add_to_ops` function would record the `__builtin_pow` call's occurrence
  count, but the subsequent failure to expand it via `attempt_builtin_powi` led to
  it being treated as a single occurrence of the base, effectively removing the `pow`
  operation. This patch modifies `attempt_builtin_powi` to instead linearize such
  `pow` calls into a…
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where optimizations are performed on the compiler's intermediate
    representation, known as 'tree'.
- term: pow
  definition: A standard library function (or intrinsic) for calculating a number
    raised to a power.
- term: powi
  definition: Often refers to a built-in intrinsic function for calculating powers
    with an integer exponent, typically more efficient than a general floating-point
    power function.
- term: reassoc
  definition: The 'reorder expressions' optimization pass in GCC, which rearranges
    associative and commutative operations to improve code efficiency and enable further
    optimizations.
- term: Intrinsic
  definition: A function that is recognized and handled directly by the compiler,
    often mapping to a specific machine instruction for better performance.
- term: _Float64
  definition: A distinct floating-point type, often representing an IEEE 754 quadruple-precision
    format, separate from the standard 'double' type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4d11a05988d3f57e947b705ed81247654a86004d
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

Previously, GCC could incorrectly drop `pow` function calls when they involved a constant integer exponent and the target type did not have a corresponding `__builtin_powi` intrinsic (e.g., `_Float64`). This commit modifies the reassoc pass to expand such `pow` calls into a series of multiplications, similar to how it handles integral types, preventing loss of these operations and improving optimization.
