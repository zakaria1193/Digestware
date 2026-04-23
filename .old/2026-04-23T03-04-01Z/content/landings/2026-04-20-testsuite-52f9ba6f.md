---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- m32
commit_hash: 52f9ba6f33514cefa4b4de67b570b03531bbfef7
source_type: github
author: Jakub Jelinek
headline: 'Testsuite: Remove -m32 from an i386 test.'
tldr: This commit removes the `-m32` flag from a test case, ensuring it's properly
  tested in both 32-bit and 64-bit environments.
why_it_matters: Ensures that test cases are executed in the appropriate environments,
  improving test coverage and reliability.
impact_score: 4
impact_rationale: Refactors the testsuite to improve test coverage by removing an
  unnecessary flag.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testsuite contains tests that should be executed in various configurations.
  The `-m32` flag forces compilation for a 32-bit architecture. Removing this flag
  from `gcc.target/i386/pr122021-0.c` allows the test to be executed during both `i686-linux`
  and `x86_64-linux` testing with appropriate target board flags, improving coverage.
primer_general: The GCC testsuite verifies that the compiler works correctly on different
  target platforms. The `-m32` option tells the compiler to generate code for a 32-bit
  architecture. This commit removes this option from a specific test case because
  the test is not specific to 32-bit systems and should be tested in both 32-bit and
  64-bit configurations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/52f9ba6f33514cefa4b4de67b570b03531bbfef7
date: '2026-04-20'
---

The test `gcc.target/i386/pr122021-0.c` was using the `-m32` flag, which limited its execution to 32-bit environments. This commit removes the flag, allowing the test to be run in both 32-bit (`i686-linux`) and 64-bit (`x86_64-linux`) environments using `--target_board=unix{-m32,-m64}`. The test itself does not contain any architecture-specific code that necessitates the flag.
