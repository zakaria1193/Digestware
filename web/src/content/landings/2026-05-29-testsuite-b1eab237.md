---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- sse2
- cascadelake
commit_hash: b1eab23769c4338d97eee797a2134bbed4e3c9a9
source_type: github
author: Roger Sayle
headline: 'Testsuite: Tweak sse2-p{add,sub}[bdw]-2.c tests for -march=cascadelake'
tldr: The sse2-p{add,sub}[bdw]-2.c tests now support the -march=cascadelake option,
  ensuring proper functionality on newer Intel architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adjusts test cases to accommodate the Cascadelake microarchitecture.  The
  tests involve SSE2 packed arithmetic instructions.  Without knowledge of the specific
  requirements or instruction scheduling characteristics of Cascadelake, the changes
  may seem minor.
primer_general: This commit modifies test cases within the GCC compiler's test suite
  to ensure compatibility with Intel's Cascadelake processors.  The tests specifically
  target SSE2 instructions, which are a set of instructions that allow the processor
  to perform arithmetic operations on multiple data elements simultaneously (Single
  Instruction, Multiple Data, or SIMD). By updating these tests, the compiler can
  be verified to generate correct code when targeting Cascadelake processors and utilizing
  SSE2 instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b1eab23769c4338d97eee797a2134bbed4e3c9a9
date: '2026-05-29'
is_stub: false
---

This commit updates the gcc.target/i386/sse2-p{add,sub}[bdw]-2.c tests to correctly handle the -march=cascadelake option. This ensures that these tests, which verify SSE2 packed addition and subtraction instructions, function as expected when compiling for Intel's Cascadelake architecture.
