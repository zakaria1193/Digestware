---
project: gcc
subsystem: match-sat-alu.pd
patch_id: null
tags:
- optimization
- aarch64
- vectorization
commit_hash: 28f6899c51c456302943d549ab78d9bb022f36d8
source_type: github
author: Kyrylo Tkachov
headline: Recognize complement tests for unsigned saturating addition.
tldr: GCC can now recognize complement tests for unsigned saturating addition, optimizing
  it to a single instruction on AArch64.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `match-sat-alu.pd` file defines patterns for recognizing and optimizing
  saturating arithmetic. This change adds recognition for expressions that use comparisons
  with complements of operands to detect overflow in unsigned saturating addition
  (`unsigned_integer_sat_add`). For instance, `MAX - Y` is equivalent to `~Y`. The
  optimization transforms constructs like `X > ~Y ? MAX : X + Y` into a single saturating
  add instruction, benefiting architectures like AArch64.'
primer_glossary:
- term: match-sat-alu.pd
  definition: A pattern description file used by GCC's backend to recognize and optimize
    specific arithmetic operations, particularly saturating arithmetic.
- term: saturating addition
  definition: An arithmetic operation that, if the result exceeds the maximum representable
    value for the operand type, clamps the result to the maximum value instead of
    wrapping around or causing an overflow error.
- term: complement
  definition: In binary representation, the bitwise complement of a number is obtained
    by inverting all of its bits (0 becomes 1, and 1 becomes 0). For unsigned integers,
    the complement of Y is equivalent to MAX_VALUE - Y.
- term: AArch64
  definition: The 64-bit ARM architecture, widely used in mobile devices and increasingly
    in servers and desktops. GCC has a backend to generate code for this architecture.
- term: uqadd
  definition: An AArch64 SIMD instruction that performs an unsigned saturating addition.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/28f6899c51c456302943d549ab78d9bb022f36d8
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

The `match-sat-alu.pd` pattern matching has been extended to recognize comparisons involving the complement of an operand for unsigned saturating addition. This allows the compiler to replace code like `X > ~Y ? MAX : X + Y` with a single `uqadd` instruction on AArch64, reducing four vector operations to one.
