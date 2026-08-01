---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- compiler internals
- bit-integers
commit_hash: acd94fdfa20bf1195061d57a57e85cdd6beaa571
source_type: github
author: Jakub Jelinek
headline: Fix narrow shift count types in shift-compare patterns
tldr: Corrected patterns in `match.pd` to handle narrow shift count types accurately,
  preventing miscompilation of shifts combined with comparisons.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch fixes two `match.pd` patterns that simplify expressions
  involving shifts and comparisons. The problem occurs when the shift count type is
  very narrow (e.g., `unsigned _BitInt(4)`) and is compared against a compile-time
  constant that doesn't fit into that narrow type. The incorrect simplification leads
  to miscompilation. The first pattern now simplifies to `cmp == NE_EXPR` if the result
  of the comparison (`cand`) cannot be represented in the target type. The second
  pattern avoids simplification if `log2` does not fit into the target type (`TREE_TYPE`).
primer_glossary:
- term: match.pd
  definition: A file containing pattern matching rules used by the GCC compiler for
    optimization passes.
- term: shift count type
  definition: The data type of the value used to specify the number of positions to
    shift bits in a shift operation.
- term: narrow type
  definition: A data type that has a small number of bits, limiting the range of values
    it can represent.
- term: _BitInt
  definition: A C++ extension allowing integer types of arbitrary bit widths.
- term: miscompile
  definition: When a compiler incorrectly translates source code into machine code,
    resulting in a program that does not behave as intended.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/acd94fdfa20bf1195061d57a57e85cdd6beaa571
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This commit addresses two issues in `match.pd` where shift operations combined with comparisons were miscompiled due to narrow shift count types. Specifically, when the shift count type (e.g., `unsigned _BitInt(4)`) could not represent the comparison value, the compiler incorrectly simplified the comparison. The fix ensures that such cases are correctly handled, either by simplifying to a comparison against `NE_EXPR` or by not simplifying if the necessary logarithmic value doesn't fit the type.
