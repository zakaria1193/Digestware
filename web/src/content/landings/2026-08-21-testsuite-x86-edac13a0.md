---
project: gcc
subsystem: testsuite/X86
patch_id: null
tags:
- testsuite
- x86
- darwin
commit_hash: edac13a0fdf0b3d4adfcc549f58f128c8f117245
source_type: github
author: Iain Sandoe
headline: Fix missing asm macro in ms-sysv do-test.
tldr: Corrects a regression in x86_64 Darwin ms-sysv tests by adding a missing macro.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ASMNAME` macro is used in GCC's testsuite to ensure correct function
  naming, especially across different platforms or assembly syntaxes. This commit
  fixes an issue in the `ms-sysv` ABI test suite for x86_64 Darwin where `do_test_unaligned`
  was called without this macro, leading to test failures. By adding `ASMNAME`, the
  function call is correctly recognized by the assembler, passing the tests.
primer_glossary:
- term: ms-sysv ABI
  definition: The Microsoft variant of the System V Application Binary Interface,
    a calling convention used on some systems.
- term: x86_64 Darwin
  definition: The 64-bit Intel architecture running on Apple's macOS operating system.
- term: ASMNAME macro
  definition: A macro used in GCC's testsuite to provide a consistent, platform-independent
    way to refer to assembly function names.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/edac13a0fdf0b3d4adfcc549f58f128c8f117245
date: '2026-08-21'
is_stub: true
stub_reason: low_score
---

This commit addresses a regression in the ms-sysv tests on x86_64 Darwin platforms. A recent change missed a function name macro, causing all ms-sysv tests to fail. The fix wraps the call to do_test_unaligned in the ASMNAME macro, resolving the issue and restoring test functionality.
