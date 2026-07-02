---
project: gcc
subsystem: testsuite/arm
patch_id: null
tags:
- testsuite
- arm
- optimization
commit_hash: 822ffdda4630d7cded883126d392c58c2b526690
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: arm: Use `noipa` for long call tests'
tldr: Switches ARM long call tests from `noinline` to `noipa` to ensure functions
  are not optimized away.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Tests in `gcc.target/arm/` that verify long call functionality previously
  used the `noinline` attribute. With recent changes in GCC's interprocedural analysis
  (IPA), specifically since revision `ga5ab19d9db2d13`, functions marked `noinline`
  might still be subject to optimization that removes them. By switching to `noipa`,
  the tests now instruct GCC to disable interprocedural optimizations that would eliminate
  the functions, ensuring the long call sequences remain intact for testing.
primer_general: This change updates test cases within the GCC compiler's test suite
  for ARM processors. Specifically, tests designed to check how the compiler handles
  "long calls" (function calls that require special mechanisms due to distance or
  position) have been modified. Previously, these tests used a directive called `noinline`
  to prevent the compiler from removing the functions being called. However, modern
  compiler optimizations can sometimes bypass `noinline`. The update replaces `noinline`
  with `noipa`, a stronger directive that more effectively prevents the compiler from
  optimizing away the tested functions, thus ensuring the tests accurately reflect
  the compiler's behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/822ffdda4630d7cded883126d392c58c2b526690
date: '2026-06-29'
is_stub: true
stub_reason: low_score
---

ARM's long call test cases in the GCC testsuite have been updated to use the `noipa` attribute instead of `noinline`.
This change prevents the compiler from optimizing away the functions being tested, which was causing test failures in newer GCC versions.
Using `noipa` (interprocedural analysis no-inline) ensures that the functions are preserved for testing purposes, allowing the long call mechanism to be correctly exercised.
