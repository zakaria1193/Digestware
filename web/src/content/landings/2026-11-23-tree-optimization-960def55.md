---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa-sccvn.cc
commit_hash: 960def556c5b7fdc72339748252b4f74be152cbf
source_type: github
author: Richard Biener
headline: VN pass guards against TRUNC_DIV_EXPR on fixed-point types.
tldr: VN pass now correctly handles TRUNC_DIV_EXPR on fixed-point types, preventing
  a potential crash.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Value Numbering (VN) pass, implemented in `tree-ssa-sccvn.cc`,
  performs common subexpression elimination on the SSA-based intermediate representation.
  This commit corrects a bug where `TRUNC_DIV_EXPR` was mishandled when used with
  fixed-point types, as its properties differ from integral division. This could lead
  to incorrect optimizations or crashes if not guarded.
primer_glossary:
- term: TRUNC_DIV_EXPR
  definition: A GCC Tree IR expression representing a division operation that truncates
    the result. It is typically used for integral types.
- term: Value Numbering (VN)
  definition: A compiler optimization pass that identifies and merges equivalent expressions
    within the intermediate representation. It operates on SSA (Static Single Assignment)
    form.
- term: Fixed-point types
  definition: Numeric types that represent fractional numbers using a fixed number
    of bits for the integer and fractional parts, without using a binary exponent.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once, simplifying many compiler analyses
    and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/960def556c5b7fdc72339748252b4f74be152cbf
date: '2026-11-23'
is_stub: true
stub_reason: low_score
---

The Value Numbering (VN) pass in GCC incorrectly assumed that TRUNC_DIV_EXPR could only operate on integral types. This commit corrects that assumption, adding a guard to prevent it from being used with fixed-point types where the usual mathematical properties do not hold. A new test case is included to verify this fix.
