---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- rtx
- bugfix
commit_hash: dea5f4b6aec73809732e5ef957692ec90dcc2e3b
source_type: github
author: Kyrylo Tkachov
headline: Fix truncation of AND of LSHIFTRT for wide modes
tldr: Corrects an optimization bug involving bitwise AND and right shifts on wide
  integer types.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_context::simplify_truncation` function was incorrectly
  simplifying `(truncate:M (and:OM (lshiftrt:OM x C) C2))` to `(and:M (lshiftrt:M
  (truncate:M x) C) C2)` when `OM` was wider than `HOST_BITS_PER_WIDE_INT`. This occurred
  because `GET_MODE_MASK` was capped, causing the comparison of masks to always succeed.
  The fix adds checks to ensure no bit of `C2` falls outside the bits defined by the
  narrowed shift and requires `M` to be HWI computable for accurate `GET_MODE_MASK`
  behavior, resolving incorrect bit manipulation for wide modes.
primer_glossary:
- term: simplify-rtx
  definition: A GCC optimization pass that simplifies Register Transfer Language (RTL)
    expressions.
- term: RTL
  definition: Register Transfer Language, GCC's internal intermediate representation
    used for lower-level optimizations and machine code generation.
- term: LSHIFTRT
  definition: Logical Shift Right operation in RTL.
- term: AND
  definition: Bitwise AND operation.
- term: Truncate
  definition: An operation that reduces the number of bits in a value, typically by
    discarding the most significant bits.
- term: Wide Modes
  definition: GCC internal data types (modes) that represent integers wider than a
    machine word, such as TImode (128 bits on a 64-bit host).
- term: HOST_BITS_PER_WIDE_INT
  definition: A macro defining the number of bits in a host's 'wide' integer type,
    typically used for intermediate calculations in GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dea5f4b6aec73809732e5ef957692ec90dcc2e3b
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in the `simplify_truncation` pass that incorrectly handled the truncation of a bitwise AND operation applied to a right-shifted value when using wide integer modes. The issue occurred when the source operand mode (`OM`) was wider than a host word, leading to incorrect code generation for certain bitwise operations. The fix involves more direct checks to ensure that mask bits are within the defined range of the narrowed shift operation, preventing incorrect bit manipulation.
