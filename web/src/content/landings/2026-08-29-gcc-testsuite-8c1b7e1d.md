---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- integer overflow
- memmove
commit_hash: 8c1b7e1d9f3d8f52dd991060afbb34676e52d836
source_type: github
author: Georg-Johann Lay
headline: Fix torture test for memmove overflow on 16-bit int systems
tldr: A torture test now uses a 32-bit integer type to prevent memmove overflow on
  systems with 16-bit ints.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Addresses PR 121103 by fixing a test case in gcc.dg/torture/pr121103-1.c.
  The test failed on platforms where `int` is 16 bits due to a `memmove` operation
  writing 8 bytes into a 7-byte buffer. The fix changes the type of the destination
  buffer `B.n` to `__INT32_TYPE__` to ensure sufficient space, preventing the stringop-overflow
  warning and test failure.
primer_glossary:
- term: memmove
  definition: A C standard library function that copies a block of memory from one
    location to another. It handles overlapping memory regions safely.
- term: torture test
  definition: A type of test case in the GCC testsuite designed to exercise specific
    compiler optimizations and code generation features under various conditions.
- term: __INT32_TYPE__
  definition: A GCC-specific type macro that represents a signed integer type guaranteed
    to be at least 32 bits wide.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8c1b7e1d9f3d8f52dd991060afbb34676e52d836
date: '2026-08-29'
is_stub: true
stub_reason: low_score
---

This commit fixes a GCC torture test (pr121103-1.c) that failed due to a buffer overflow when using `memmove`. On systems where `int` is 16 bits, the destination buffer 'B' was only 7 bytes, but the test attempted to write 8 bytes. By changing the type of `B.n` to `__INT32_TYPE__`, the test now correctly accounts for the buffer size, resolving the overflow issue.
