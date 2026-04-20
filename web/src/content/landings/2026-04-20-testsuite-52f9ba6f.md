---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- architecture
commit_hash: 52f9ba6f33514cefa4b4de67b570b03531bbfef7
source_type: github
author: Jakub Jelinek
headline: 'Testsuite: Remove -m32 from gcc.target/i386 test [PR122021]'
tldr: Removes the `-m32` flag from a test case, ensuring it's tested appropriately
  for both 32-bit and 64-bit targets.
why_it_matters: Ensures tests are executed correctly across different target architectures
  by removing unnecessary architecture specifiers.
impact_score: 4
impact_rationale: Fixes test setup to ensure correct execution on different architectures.
performance_win: false
breaking_change: false
outcome: committed
primer: The GCC testsuite validates the compiler's correctness. Tests are often architecture-specific,
  and the `-m32` flag tells the compiler to generate 32-bit code. However, some tests
  are architecture-independent and should be run in both 32-bit and 64-bit modes to
  ensure broader compatibility.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/52f9ba6f33514cefa4b4de67b570b03531bbfef7
date: '2026-04-20'
---

This commit removes the `-m32` flag from a test in `gcc.target/i386/`.  The test isn't specific to ia32 and should be run during both i686-linux and x86_64-linux testing.  The change makes the test run with `--target_board=unix{-m32,-m64}`.
