---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- IPA
- predicate
commit_hash: af401d2507d2c50fa551291490a1482660c4d417
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix bogus switch stmt IPA predicates.'
tldr: Fixes incorrect sign extension when setting IPA predicates for switch statements.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The function `set_switch_stmt_execution_predicate` in `ipa-fnsummary.cc`
  incorrectly handled sign extension when converting minimum values for switch statement
  predicates. It used `wide_int_to_tree(type, wi::to_wide(min))` which fails to preserve
  the sign if `type` has higher precision than `min`. This is particularly problematic
  when `min` is negative. The correct approach for extending integer values while
  preserving their sign and accommodating different precision levels is `wi::to_widest`.
  This change replaces the erroneous idiom with the correct one, resolving PR tree-optimization/127764.
primer_glossary:
- term: IPA
  definition: Inter-procedural Analysis. A compiler analysis that examines the behavior
    of a program across multiple procedures (functions), rather than just within a
    single one.
- term: Predicate
  definition: A condition or statement that can be true or false. In this context,
    it refers to information used by the compiler to determine whether a specific
    part of the code (like a switch statement) is guaranteed to be executed.
- term: Switch Statement
  definition: A control flow statement that allows a program to execute different
    code blocks based on the value of an expression.
- term: Sign Extension
  definition: The process of increasing the number of bits of a binary number while
    preserving its sign. For a positive number, leading zeros are added; for a negative
    number (using two's complement), leading ones are added.
- term: Wide Integer
  definition: An integer type that can represent values larger than the standard integer
    types (e.g., `int`, `long long`). GCC uses a `wide_int` (or `wi`) library for
    arbitrary-precision integers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/af401d2507d2c50fa551291490a1482660c4d417
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

A bug in `set_switch_stmt_execution_predicate` has been fixed where it incorrectly extended the sign of minimum values when setting execution predicates for switch statements. This incorrect sign extension, using `wi::to_wide` instead of `wi::to_widest`, could lead to bogus predicates when the precision of the minimum value and the target type differed. The fix uses `wi::to_widest` to preserve the sign correctly, ensuring accurate IPA predicate generation.
