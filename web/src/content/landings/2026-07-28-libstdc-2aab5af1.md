---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- random
- optimization
commit_hash: 2aab5af1738b3adc2e673977b4cd0d5c393b4252
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Extend Lemire''s algorithm to all power-of-two ranges.'
tldr: Libstdc++ now uses Lemire's algorithm for all power-of-two sized random number
  generation ranges.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch generalizes the use of Lemire's algorithm within `libstdc++`'s
  `uniform_int_distribution`. Previously, `operator()` utilized Lemire's algorithm
  (`_S_nd`) only when the range size was `2^32` or `2^64`. Now, it employs `_S_nd`
  whenever the engine's range (`__urngrange`) is a power of two. The `_S_nd` function
  is modified to accept a `_Bits` parameter and masks the result of `__product` conversion
  to `_Up` to the lowest `_Bits`. This ensures correctness for any power-of-two range
  size. A test case is added for `ranlux24` and `ranlux48` engines.
primer_glossary:
- term: Lemire's algorithm
  definition: An efficient algorithm for generating uniform random numbers within
    a range, particularly effective for ranges that are powers of two.
- term: uniform_int_distribution
  definition: A C++ standard library class that generates random integers uniformly
    distributed over a specified range.
- term: power of two
  definition: A number that can be expressed as 2 raised to an integer exponent (e.g.,
    2, 4, 8, 16, 32, 64).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2aab5af1738b3adc2e673977b4cd0d5c393b4252
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

This change expands the application of Lemire's algorithm in libstdc++ to cover all random number generators producing values in ranges that are powers of two. Previously, this optimization was limited to 2^32 and 2^64 ranges. By masking the conversion of `__product` to the lowest `_Bits` width, the algorithm is now more universally applicable. This improves the efficiency of random number generation for a wider set of configurations, with the masking operation being optimized away by compilers when the bit width matches the target type.
