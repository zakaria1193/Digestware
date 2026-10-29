---
project: gcc
subsystem: vect-generic
patch_id: null
tags:
- gcc
- vectorization
- optimization
- signed division
commit_hash: e88c76e0a7ef568ebff9c09f18c7f9516d6a0d24
source_type: github
author: Igor Shevlyakov
headline: Handle signed division by negative powers of two in vectorization
tldr: Vector division by negative powers of two is now correctly handled, improving
  vectorization accuracy.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `expand_vector_divmod` function in `tree-vect-generic.cc` now correctly
  handles signed division by negative powers of two. Previously, it relied on a power-of-two
  shift path only for positive divisors, falling back for negative ones. This update
  implements the scalar division logic (`x / -2^k == -(x / 2^k)`) for vectors. It
  introduces a `negate_p` flag for `TRUNC_DIV` to track the divisor's sign and applies
  a vector negate operation if necessary. Certain edge cases (mixed signs, unsupported
  negate/subtract, INT_MIN magnitude) still use the multiply-high path.
primer_glossary:
- term: Vectorization
  definition: The process by which a compiler automatically converts a scalar loop
    into a loop that operates on multiple data elements simultaneously using special
    vector instructions.
- term: Signed division
  definition: Arithmetic division where the dividend and divisor can be positive or
    negative, and the result's sign follows standard mathematical rules.
- term: Power of two
  definition: A number that can be expressed as 2 raised to some integer exponent
    (e.g., 2, 4, 8, 16).
- term: TRUNC_DIV
  definition: Truncating division, where the result of a division is rounded towards
    zero (e.g., 7 / 3 = 2, -7 / 3 = -2).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e88c76e0a7ef568ebff9c09f18c7f9516d6a0d24
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

This commit extends vector division by powers of two to handle negative divisors. Previously, only positive divisors were supported, with negative divisors falling back to a less efficient sequence. The change ensures correct results for signed division by negative powers of two, similar to scalar division, by adjusting the quotient's sign when needed.
