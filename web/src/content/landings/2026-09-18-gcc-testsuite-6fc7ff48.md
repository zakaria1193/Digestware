---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- bit-integer
- compiler correctness
commit_hash: 6fc7ff484d354ee4e85ca7e4f555063a06800c6a
source_type: github
author: Jakub Jelinek
headline: Fix bitint testcase that incorrectly uses ~0 for signed types
tldr: Corrects a testcase involving bit-integers to use memset for predictable initialization.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `gcc.dg/bitint-142.c` relied on the behavior of `~0` with
  signed `_BitInt(N)` types, which is target-dependent due to sign extension semantics.
  On targets with `bitint_ext_undef`, `~0` might set only the lower N bits. On others
  (`bitint_ext_full`), it could sign-extend, setting all bits. The fix replaces `z
  = ~0` with `memset(&z, ~0, sizeof(z))` to reliably set all bits, aligning the test's
  expectation with the intended manipulation of padding bits.
primer_glossary:
- term: _BitInt(N)
  definition: A GCC-specific integer type with N bits, allowing for arbitrary bit
    widths beyond standard integer types.
- term: padding bits
  definition: Extra bits in a data type that are not used for storing the value itself,
    often present for alignment or internal representation reasons. These bits can
    have undefined or unpredictable values.
- term: sign extension
  definition: The process of filling the most significant bits of a number with copies
    of the sign bit when converting it to a larger data type. This preserves the sign
    of the number.
- term: memset
  definition: A C standard library function that fills a block of memory with a specified
    byte value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6fc7ff484d354ee4e85ca7e4f555063a06800c6a
date: '2026-09-18'
is_stub: true
stub_reason: low_score
---

A testcase for GCC's bit-integer support (gcc.dg/bitint-142.c) has been fixed. The original test used `~0` to initialize a signed `_BitInt(7)` variable, which had unintended side effects on certain targets due to sign extension. The corrected version now uses `memset` to explicitly set all bits, ensuring consistent behavior across different target architectures.
