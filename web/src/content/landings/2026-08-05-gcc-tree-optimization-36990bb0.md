---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- idiom
commit_hash: 36990bb0d14c4840d0250f000559d7a2a569fbc9
source_type: github
author: Naveen
headline: Recognize add/sub absolute-value idiom
tldr: GCC now optimizes Y + abs(X) and Y - abs(X) expressions to improve code efficiency.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'Recognizes the idiom `X >=/> 0 ? Y + X : Y - X` and its variants in
  the SSA form. It transforms these into an unsigned addition/subtraction and back,
  which can simplify control flow and enable further optimizations, provided signed
  overflow is not a concern. This is handled by `match.pd` pattern matching.'
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler that operates on an intermediate representation
    called GENERIC, which is structured as a tree. Optimizations here aim to improve
    code efficiency before it's lowered to RTL.
- term: absolute value
  definition: The non-negative value of a number without regard to its sign. For example,
    the absolute value of -5 is 5, and the absolute value of 5 is 5.
- term: SSA form
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once, simplifying many optimization
    analyses.
- term: signed overflow
  definition: An arithmetic condition that occurs when the result of an operation
    on signed integers exceeds the maximum representable value or goes below the minimum
    representable value for that type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/36990bb0d14c4840d0250f000559d7a2a569fbc9
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

GCC's tree optimizer now recognizes and simplifies expressions involving addition or subtraction of an absolute value. The transformation is applied to signed integral types by performing the operation in the unsigned domain, preserving wrapping semantics and avoiding signed overflow. This optimization is not applied if signed overflow traps or is sanitized.
