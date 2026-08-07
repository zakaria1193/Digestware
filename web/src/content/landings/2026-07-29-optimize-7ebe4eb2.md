---
project: gcc
subsystem: optimize
patch_id: null
tags:
- optimization
- match
commit_hash: 7ebe4eb29d8fc0167f98705b53b4fddb28f0cffb
source_type: github
author: Kyrylo Tkachov
headline: 'match: Fold remainder comparison with its dividend.'
tldr: Optimization to simplify X % Y == X comparisons by checking X < Y.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The match.pd optimization pass now recognizes the pattern `(X % Y)
  == X`. For unsigned integers, this condition simplifies to `X < Y`. This transformation
  is analogous to the existing `(X / Y) == 0` simplification. Care is taken to preserve
  potential zero-divisor exceptions, especially when non-call exceptions are enabled.
primer_glossary:
- term: match.pd
  definition: The pattern-matching optimization pass in GCC, responsible for recognizing
    and transforming specific code patterns into more efficient forms.
- term: remainder operation
  definition: An arithmetic operation that yields the remainder after division of
    one number by another. In C/C++, this is the '%' operator.
- term: zero-divisor exception
  definition: An exception raised when an attempt is made to divide by zero. Compilers
    may need to preserve this behavior or handle it specifically.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7ebe4eb29d8fc0167f98705b53b4fddb28f0cffb
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

The match optimization pass now simplifies expressions of the form X % Y == X. For non-negative operands, this condition is true if and only if the dividend X is less than the divisor Y. This avoids an unnecessary division operation. The optimization is similar to the existing rule for (X / Y) == 0 and preserves exceptions for potential zero divisors.
