---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- gcc
- attribute
commit_hash: ea9ca5b61117e57899e848def9124ea9f40aca49
source_type: github
author: Andrea Pinski
headline: Add returns_twice testcase for PR126815
tldr: Adds a new test case to the GCC test suite to verify a fix for an ICE related
  to functions with `__attribute__((returns_twice))`.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a test case to GCC's torture suite (`gcc.dg/torture/returns-twice-1.c`)
  to verify a fix for PR tree-optimization/126815. The PR involved an ICE related
  to functions marked with `__attribute__((returns_twice))`. The test case reproduces
  the ICE and confirms that adding a statement before the call site does not work,
  thus validating the correction.
primer_glossary:
- term: Internal Compiler Error (ICE)
  definition: An error condition where the compiler itself encounters an unrecoverable
    problem during the compilation process, halting execution.
- term: __attribute__((returns_twice))
  definition: 'A GCC attribute that indicates a function, such as `setjmp`, returns
    twice: once normally and once when control is transferred back via `longjmp`.'
- term: Test suite
  definition: A collection of test programs and scripts used to verify the correctness
    of a software system, in this case, the GCC compiler.
- term: torture test
  definition: A category of tests within a compiler's test suite designed to stress
    specific language features or compiler optimizations, often uncovering edge cases
    and bugs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea9ca5b61117e57899e848def9124ea9f40aca49
date: '2026-08-13'
is_stub: true
stub_reason: low_score
---

A new test case, `returns_twice-1.c`, has been added to the GCC test suite. This test specifically targets an ICE (Internal Compiler Error) identified in PR126815, which occurred when compiling functions declared with the `__attribute__((returns_twice))` attribute. The testcase demonstrates that inserting a statement before the function call does not resolve the issue and verifies the fix. It was tested on x86_64-linux-gnu and passes.
