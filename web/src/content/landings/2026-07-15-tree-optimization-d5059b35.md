---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- integer types
commit_hash: d5059b35e03e63c7686288c3554c2922a2c37468
source_type: github
author: Jakub Jelinek
headline: 'match.pd: Guard x+x -> x*2 simplification'
tldr: The x+x -> x*2 simplification is now guarded to ensure '2' is representable
  in the type.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` pattern `(set (x+x) (x*2))` is too aggressive for types
  like `_BitInt(1)`, `unsigned :1`, `signed :2`, etc., where the literal `2` is not
  representable. In such cases, the multiplication may result in `x*0` or `x*-2` (on
  signed types). This commit restricts the optimization to only apply when the literal
  `2` can be correctly represented in the target type, potentially to `x << 1` for
  cases where `x*2` is not representable but `x*2` is equivalent to `x << 1`.
primer_glossary:
- term: match.pd
  definition: A file containing patterns for instruction selection and optimization
    passes within GCC. It describes how to match source-level constructs to target
    machine instructions.
- term: _BitInt
  definition: A C++ extension that allows for arbitrary-width integer types, specified
    by the number of bits in their width.
- term: simplification
  definition: An optimization technique where an expression or code sequence is replaced
    by an equivalent but simpler or faster one.
- term: tree-optimization
  definition: A phase in the compilation process where GCC analyzes and transforms
    the program's intermediate representation (the 'tree') to improve performance
    or reduce code size.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d5059b35e03e63c7686288c3554c2922a2c37468
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

A simplification that transforms `x + x` into `x * 2` is now guarded to prevent incorrect transformations on types where the literal `2` cannot be represented. This addresses a bug where certain small fixed-width integer types could lead to multiplication by zero or -2 instead of the intended value. A new test case verifies this behavior.
