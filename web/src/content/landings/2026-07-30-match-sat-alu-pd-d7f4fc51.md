---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- aarch64
- saturating arithmetic
- vector
commit_hash: d7f4fc514a7f5d951e9738fb3c23a14cf49bfd8d
source_type: github
author: Kyrylo Tkachov
headline: AArch64 recognizes unsigned saturating subtraction.
tldr: Optimizes unsigned saturating subtraction on AArch64, reducing instruction count.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit enhances `match-sat-alu.pd` by adding patterns that identify
  unsigned saturating subtraction. Unsigned subtraction `X - Y` saturates to 0 if
  `X < Y` (i.e., if the subtraction borrows). The patterns recognize this by checking
  if the result `R` is greater than the minuend `X`, or by comparing `R` against `X`.
  The optimization transforms complex sequences involving comparisons and conditional
  selections into a single efficient vector saturating subtract instruction on AArch64.
primer_glossary:
- term: saturating subtraction
  definition: An arithmetic operation where the result is capped at the minimum representable
    value (zero for unsigned integers) if the true difference falls below it.
- term: unsigned integer
  definition: An integer data type that can only represent non-negative values.
- term: AArch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and servers.
- term: match-sat-alu.pd
  definition: A GCC machine description file that defines patterns for recognizing
    and optimizing saturating arithmetic operations on various ALUs.
- term: borrow
  definition: In unsigned subtraction, a borrow occurs when the minuend is smaller
    than the subtrahend, indicating that the result would underflow if not for the
    unsigned representation's wrap-around behavior.
- term: uqsub
  definition: The AArch64 instruction for unsigned saturating subtraction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d7f4fc514a7f5d951e9738fb3c23a14cf49bfd8d
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

GCC can now recognize patterns for unsigned saturating subtraction on AArch64, such as `R = X - Y; R > X ? 0 : R`. This optimization replaces sequences of three instructions with a single `uqsub` (unsigned saturating subtract) instruction. The change also removes several expected-failure test cases for these patterns.
