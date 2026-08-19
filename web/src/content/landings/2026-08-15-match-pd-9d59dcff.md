---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- bitwise
- boolean logic
commit_hash: 9d59dcff40a4f39ee82f9c59a67f9466d7a8bc66
source_type: github
author: Shivam Gupta
headline: 'match.pd: Simplify boolean comparisons of masked bits'
tldr: New pattern in match.pd simplifies comparisons of masked bits, canonicalizing
  them into XOR-mask tests for better optimization.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: A new generalized rule has been added to `match.pd` to canonicalize
  boolean comparisons of masked power-of-two bits. The patterns `((x & c) == 0) OP
  ((y & c) == 0)` and `((x & c) != 0) OP ((y & c) == 0)` (where `OP` is `==`, `!=`,
  or `^`, and `c` is a power-of-two mask) are now folded into `((x ^ y) & c) == 0`
  or `((x ^ y) & c) != 0`. This addresses an issue where GCC produced different GIMPLE
  forms for the same logical expression based on whether it originated from a function
  return or an inline expression, improving optimization consistency for bitwise parity
  checks.
primer_glossary:
- term: match.pd
  definition: A pattern-matching file within GCC used for optimizing GIMPLE (GCC's
    intermediate representation) code. It defines rules to recognize and transform
    specific code patterns into more efficient forms.
- term: GIMPLE
  definition: GCC's Internal Gimple Representation. It's a three-address, low-level
    intermediate representation used by the compiler's optimization passes.
- term: XOR
  definition: Exclusive OR, a bitwise logical operation that outputs true if and only
    if the inputs differ.
- term: canonicalize
  definition: To transform an expression or representation into a standard, simplified
    form that is equivalent to the original.
- term: PR tree-optimization/112533
  definition: A bug report filed against the tree-optimization pass of the GCC compiler,
    concerning the simplification of boolean comparisons of masked bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9d59dcff40a4f39ee82f9c59a67f9466d7a8bc66
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

This commit introduces a new rule into `match.pd` to simplify boolean comparisons involving masked bits, specifically targeting expressions like `(~A & 1) == (~B & 1)`. The optimization recognizes that these comparisons, especially when dealing with power-of-two masks, can be canonicalized into a more efficient XOR-mask form: `((x ^ y) & c) == 0` or `((x ^ y) & c) != 0`. This applies to various combinations of equality and inequality operators and aims to improve optimization effectiveness, particularly at `-O1`, resolving PR tree-optimization/112533.
