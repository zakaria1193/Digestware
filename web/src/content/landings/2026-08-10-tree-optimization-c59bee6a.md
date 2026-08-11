---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
commit_hash: c59bee6acb24a0d580f4c98a14e879452096220e
source_type: github
author: Tudor-Stefan Magirescu
headline: 'tree-optimization: Simplify ((X CMP1 Y) - (X CMP2 Y)) REL 0'
tldr: Adds a new optimization pattern to simplify differences of comparisons into
  a single comparison.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: A new pattern has been added to `match.pd` to recognize and fold expressions
  representing the sign of a difference between two comparisons. The pattern specifically
  targets `(a - b) CMP 0` where `a` is `(X CMP1 Y)` and `b` is `(X CMP2 Y)`, and `CMP1`/`CMP2`
  are opposing comparison operators (e.g., `gt`/`lt`, `ge`/`le`). This is distinct
  from the existing `(X - Y) CMP 0` rule which is limited to `eq`/`ne` and cannot
  be extended to signed comparisons without interfering with `ABS_EXPR` synthesis.
  This new pattern correctly handles the full comparison structure, avoiding regressions
  in folding c…
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where the code is represented as an abstract syntax tree
    (or more precisely, a Control Flow Graph of GENERIC trees) and subjected to various
    optimizations.
- term: match.pd
  definition: A file containing patterns used by GCC's pattern matching engine during
    optimization passes to identify and transform specific code structures into more
    efficient forms.
- term: fold
  definition: In compiler optimization, the process of combining or simplifying expressions
    into a simpler equivalent form. For example, folding `2 + 3` into `5`.
- term: sign-of-difference expressions
  definition: Expressions that determine the sign (positive, negative, or zero) of
    the difference between two values, often computed by comparing the values themselves.
- term: ABS_EXPR
  definition: GCC's internal representation for an absolute value expression, often
    synthesized during optimization.
- term: fold_cond_expr_with_comparison
  definition: A GCC optimization function that attempts to simplify conditional expressions
    (like ternary operators) by folding them with comparison operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c59bee6acb24a0d580f4c98a14e879452096220e
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

This commit introduces a new optimization pattern in `match.pd` that simplifies expressions of the form `((X CMP1 Y) - (X CMP2 Y)) REL 0` into a single comparison. This pattern specifically targets differences of two comparisons involving the same operands, where the comparison operators are opposites (e.g., `gt`/`lt` or `ge`/`le`). This enables folding of sign-of-difference expressions into a more efficient comparison, improving generated code.
