---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- optimization
- floating-point
- match.pd
commit_hash: 6c9deef7effbf410e5d4061c4ea6f53e1dca0bad
source_type: github
author: Alexey Lapshin
headline: Fold floating-point compare-and-negate idioms to ABS
tldr: New patterns in match.pd simplify floating-point expressions involving conditional
  negation to absolute value operations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This commit adds new patterns to `match.pd` for simplifying conditional
  negation of floating-point values. Specifically, it targets idioms of the form `(cond
  ? -A : A)` or `(cond ? A : -A)` and folds them into `ABS(A)` or `-ABS(A)`. The folding
  is enabled when NaN propagation or floating-point exceptions (like invalid operation)
  are not observable. This applies to scalar and vector types, provided the target
  supports the necessary vector ABS operations. Integer operands are handled by inverting
  the comparison.'
primer_glossary:
- term: match.pd
  definition: A file containing pattern matching definitions used by GCC to recognize
    and optimize specific code sequences. These patterns are often used to transform
    code into more efficient forms or to generate specific machine instructions.
- term: folding
  definition: An optimization technique where GCC replaces a complex expression or
    code sequence with a simpler, equivalent one. This often involves recognizing
    common idioms or constant expressions.
- term: idiom
  definition: A common and recognizable pattern of code that has a specific meaning
    or intent, often used to express a particular operation concisely.
- term: NaN
  definition: Not a Number. A special floating-point value used to represent undefined
    or unrepresentable results, such as the result of 0/0. Operations involving NaNs
    can have specific trapping or non-trapping behaviors.
- term: signed zeros
  definition: Floating-point numbers that have a sign bit, even when their magnitude
    is zero. While often treated identically, signed zeros can sometimes affect the
    results of comparisons or other operations, particularly in specific numerical
    algorithms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c9deef7effbf410e5d4061c4ea6f53e1dca0bad
date: '2026-10-25'
is_stub: false
stub_reason: ''
---

GCC's pattern matching system now folds common floating-point idioms like `(A < 0 ? -A : A)` into `ABS(A)`. This optimization applies when signed zeros do not need preservation and the operand cannot be NaN, or when the invalid exception is not observable. New test cases verify this folding for scalar and vector types.
