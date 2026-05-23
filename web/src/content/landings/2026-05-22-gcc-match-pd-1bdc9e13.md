---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- gcc
- optimization
- bit manipulation
commit_hash: 1bdc9e13987fc7451a4f11cfdf8b6dfb827cf9f5
source_type: github
author: Jakub Jelinek
headline: Match.pd now handles BUILT_IN_BITREVERSE8 like the other bitreverses.
tldr: GCC's pattern-matching pass now recognises `__builtin_bitreverse8` when optimising
  bit-reversal operations.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file in GCC defines patterns for tree-based optimizations.
  `BUILT_IN_BITREVERSE*` are compiler intrinsics for reversing the bits in an integer.
  The pattern-matching pass uses these patterns to identify opportunities to replace
  generic code with optimized bit-reversal implementations.  This patch modifies the
  `BITREVERSE` macro in `match.pd` to include `BUILT_IN_BITREVERSE8`.
primer_general: Compilers often include built-in functions that map directly to specific
  CPU instructions or optimized library routines.  These builtins can expose hardware
  features or provide performance benefits.  To take advantage, the compiler needs
  to recognise these builtins during optimization.  This commit updates GCC's pattern-matching
  pass to recognise the `__builtin_bitreverse8` intrinsic, which reverses the order
  of bits in a byte, allowing the compiler to generate more efficient code when this
  operation is used.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1bdc9e13987fc7451a4f11cfdf8b6dfb827cf9f5
date: '2026-05-22'
is_stub: false
---

GCC's pattern matching pass (match.pd) missed `BUILT_IN_BITREVERSE8` when optimizing bit-reversal operations; this commit adds it to the `BITREVERSE` operator list.  The change comes with additional test cases for `__builtin_bitreverse{8,16,64,128}`.
