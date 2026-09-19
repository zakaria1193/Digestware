---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- floating-point
- powerpc
- long double
commit_hash: 3c5f42d64a7318745a712ef1cc53e8853e32961b
source_type: github
author: Jakub Jelinek
headline: Defer floating-point constant evaluation for IBM double-double
tldr: Testcase avoids evaluating problematic floating-point operations on powerpc64.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `g++.dg/cpp29/std-floating1.C` was intended to verify constant
  evaluation of floating-point operations per P3899R3. On `powerpc64-linux`, `long
  double` is often IBM double-double. GCC's `real.cc` emulation, which uses a fixed
  106-bit mantissa and double's exponent range, cannot accurately represent this type's
  true dynamic precision (up to ~1000 bits). This leads to inexact results for operations
  like `minld*minld`. The patch adds `dg-bogus` directives to xfail these specific
  tests, acknowledging the emulation's limitations without breaking the test suite.
primer_glossary:
- term: constant evaluation
  definition: The process by which the compiler computes the value of an expression
    at compile time, rather than at runtime.
- term: long double
  definition: A floating-point data type that provides higher precision than `double`.
    Its exact format and precision vary by platform.
- term: IBM double-double
  definition: A specific format for representing high-precision floating-point numbers,
    commonly used on IBM architectures. It consists of two double-precision floating-point
    numbers.
- term: xFAIL
  definition: A test directive that marks a test case as expected to fail for specific
    reasons, allowing the test suite to continue running without reporting a hard
    failure.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3c5f42d64a7318745a712ef1cc53e8853e32961b
date: '2026-09-18'
is_stub: true
stub_reason: low_score
---

A testcase for C++23 floating-point semantics (g++.dg/cpp29/std-floating1.C) has been modified to handle issues on powerpc64 targets where `long double` uses the IBM double-double format. Due to limitations in GCC's `real.cc` emulation of this type, certain floating-point operations (like min/max with or without multiplication) can be imprecise. The test now xfails these specific cases, indicating they are known issues rather than outright failures.
