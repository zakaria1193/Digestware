---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- compiler
commit_hash: 85f255021606d2bf147c7083e8b49e8987d5c393
source_type: github
author: Shivam Gupta
headline: Reduce (t * u) / v when gcd(u, v) > 1.
tldr: Optimizes division expressions by reducing constants when they share common
  factors.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-optimization` pass, using `match.pd` patterns, now reduces
  the constants in `(t * u) / v` expressions when `gcd(u, v) > 1`. The expression
  is rewritten as `(t * (u / g)) / (v / g)`, where `g = gcd(u, v)`. This transformation
  is applied if `t * u` is guaranteed not to overflow. This optimization aims to reduce
  the magnitude of constants involved in division, leading to potentially cheaper
  division-by-constant sequences and mitigating overflow risks. The optimization requires
  a single-use multiplication.
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler that operates on an intermediate representation
    called 'tree' to perform various code optimizations.
- term: gcd
  definition: Greatest Common Divisor. The largest positive integer that divides two
    or more integers without leaving a remainder.
- term: overflow
  definition: A condition that occurs when an arithmetic operation produces a result
    that is too large to be stored in the allocated memory space for that data type.
- term: division-by-constant
  definition: An optimization where a division operation by a constant value is replaced
    by a sequence of shifts, additions, and subtractions, which can be faster on some
    architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/85f255021606d2bf147c7083e8b49e8987d5c393
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

GCC's tree optimization pass now simplifies integer divisions of the form `(t * u) / v` when `u` and `v` share a common divisor greater than one. By dividing `u` and `v` by their greatest common divisor (`gcd`), the compiler generates smaller constants, which can lead to more efficient division operations and potentially avoid overflow issues. This optimization is applied when `t * u` is known not to overflow.
