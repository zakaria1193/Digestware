---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler internals
- VN
commit_hash: 8395fa7c79eecf102b276ffee37436e75a522978
source_type: github
author: Philipp Tomsich
headline: VN finds inverse widening lookups for PLUS/MINUS
tldr: Value Numbering now recognizes (T)A + C == (T)(A + C) to improve optimization.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The Value Numbering (VN) pass in GCC uses a rewrite rule system to
  identify equivalent expressions. Prior to this change, in `visit_nary_op`, only
  forward canonicalization of `(T)(A + C)` to `(T)A + (T)C` was supported. This commit
  adds a `match.pd` rule using the `op!` qualifier within `mprts_hook` to achieve
  the reverse: rewriting `(T)A +- CST` to `(T)(A +- CST'')`. This specifically targets
  signed inner types with undefined overflow, avoiding issues with unsigned type wrapping
  or bitfield representations. It relies on `wi::min_precision` for correct fit checks,
  handling cases like `-1` fitt…'
primer_glossary:
- term: Value Numbering (VN)
  definition: A compiler optimization pass that assigns a unique number (value number)
    to each distinct expression or value. If two expressions have the same value number,
    the compiler knows they compute the same result, enabling common subexpression
    elimination and other optimizations. VN typically operates on the compiler's intermediate
    representation (IR).
- term: Canonicalization
  definition: The process of transforming an expression or data structure into a standard
    or normal form. In compilers, this often means rewriting expressions into a consistent
    format to simplify analysis and comparison, allowing passes like Value Numbering
    to operate more effectively.
- term: Widening Conversion
  definition: An implicit or explicit conversion of a value from a type with a smaller
    range or precision to a type with a larger range or precision. For example, converting
    an 8-bit integer to a 32-bit integer. This can sometimes change the observed value
    if the original type had different overflow behavior.
- term: Undefined Overflow
  definition: In C and C++, signed integer overflow results in undefined behavior.
    This means the compiler can assume it never happens and may optimize code based
    on this assumption, leading to incorrect results if overflow does occur. Unsigned
    integer overflow, however, is well-defined (wraps modulo 2^N).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8395fa7c79eecf102b276ffee37436e75a522978
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This change enhances Value Numbering (VN) by adding an inverse widening lookup for PLUS and MINUS operations. Previously, VN could canonicalize expressions like (T)(A + C) to (T)A + (T)C, but not the reverse. By adding a pattern to rewrite (T)A +- CST into (T)(A +- CST'), VN can now discover equivalences regardless of the initial expression form, potentially leading to better constant folding and reduced miscompiles.
