---
project: gcc
subsystem: gcc/generic
patch_id: null
tags:
- gcc
- ubsan
- optimization
- security
commit_hash: ab84bf1409c2b4f6e328ab9a18123ec40a6ff4e8
source_type: github
author: Dominic P
headline: Do not fold branchless min/max when overflow is sanitized
tldr: Prevent GCC from simplifying expressions that hide signed integer overflow warnings.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `gimple_match_no_overflow_p` function in `generic-match-head.cc`
  used `TYPE_OVERFLOW_UNDEFINED` as a proof of non-overflow for arithmetic operations.
  However, with `-fsanitize=signed-integer-overflow`, the front-end folds expressions
  like `y + (x - y < 0 ? x - y : 0)` into `MIN_EXPR` before `pass_ubsan` instruments
  the code. This commit modifies `gimple_match_no_overflow_p` to return false for
  sanitized types, preventing premature folding and ensuring overflow is detected.'
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation for code after the front-end has parsed
    it. It's a three-address, low-level form that simplifies optimization.
- term: signed integer overflow
  definition: Occurs when an arithmetic operation on signed integers produces a result
    that is outside the range representable by the data type. In C/C++, signed overflow
    leads to undefined behavior.
- term: UBSan (Undefined Behavior Sanitizer)
  definition: A runtime instrumentation tool in GCC that detects various types of
    undefined behavior, including signed integer overflow, which can lead to incorrect
    program behavior or security vulnerabilities.
- term: folding
  definition: An optimization technique where constant expressions are evaluated at
    compile time rather than runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab84bf1409c2b4f6e328ab9a18123ec40a6ff4e8
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

GCC's generic matching logic incorrectly folded branchless min/max expressions when signed integer overflow sanitization was enabled. This simplification obscured the overflow, preventing the sanitizer from reporting it. The fix ensures that sanitized types are excluded from this folding, preserving the sanitizer's ability to detect overflows.
