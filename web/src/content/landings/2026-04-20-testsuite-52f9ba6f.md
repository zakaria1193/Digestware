---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- x86_64
- build
commit_hash: 52f9ba6f33514cefa4b4de67b570b03531bbfef7
source_type: github
author: Jakub Jelinek
headline: 'Testsuite: Remove -m32 from gcc.target/i386 test'
tldr: Removes the `-m32` flag from an i386 test case that isn't specific to the 32-bit
  architecture.
why_it_matters: Ensures tests are executed on appropriate architectures and avoids
  redundant testing.
impact_score: 4
impact_rationale: Minor testsuite cleanup; limited user impact.
performance_win: false
breaking_change: false
outcome: committed
primer: The GCC testsuite contains a collection of programs used to verify the compiler's
  correctness.  Tests under `gcc.target` typically check code generation for a specific
  target architecture. The `-m32` flag tells GCC to compile code for a 32-bit x86
  architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/52f9ba6f33514cefa4b4de67b570b03531bbfef7
date: '2026-04-20'
---

This commit removes the `-m32` option from `gcc.target/i386/pr122021-0.c`. The test isn't specific to ia32 and should be tested during i686-linux or x86_64-linux testing with appropriate target board options.
