---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- bugfix
- undefined-behavior
commit_hash: 35e1e59d818b8a8274c889532b020be36d014449
source_type: github
author: Tamar Christina
headline: Fix UB in vect-early-break_144-pr125804.c
tldr: A GCC test case has been updated to remove undefined behavior related to signed
  shifts, improving test stability.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect-early-break_144-pr125804.c` test case, part of the GCC test
  suite, contained undefined behavior (UB) related to signed shifts. On 32-bit systems,
  shifting a signed integer value beyond its valid range or into the sign bit can
  lead to implementation-defined or undefined behavior, which can cause inconsistent
  test failures. This patch concretely identifies and remedies these problematic shift
  operations within the test, ensuring it operates within well-defined C semantics.
  This change stabilizes the test's reliance on vectorization and early-break conditions
  without introducing new ar…
primer_general: Imagine a programmer writes code that, in some situations, doesn't
  have a clear, predictable outcome according to the C programming language rules.
  This is called "undefined behavior" (UB). Compilers like GCC are designed to optimize
  code, but when they encounter UB, they can do unexpected things, sometimes even
  crashing or producing incorrect results. This commit fixes a specific instance of
  UB in one of GCC's own test cases, `vect-early-break_144-pr125804.c`. The UB was
  caused by how signed numbers were being shifted (a bit manipulation operation) on
  32-bit computer systems. Even if this issue didn't always cause a crash or error
  on every machine, it created an unstable test. By removing the UB, the test case
  becomes more reliable, helping GCC developers ensure the compiler works correctly
  across all supported systems without relying on unpredictable behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/35e1e59d818b8a8274c889532b020be36d014449
date: '2026-06-20'
is_stub: false
---

This commit addresses and fixes undefined behavior (UB) present in the `vect-early-break_144-pr125804.c` GCC test case. The UB, specifically related to signed shifts on 32-bit systems, was identified as a potential cause for reported test failures, even if not universally reproducible. By correcting the problematic code within the test, this patch aims to eliminate the UB and stabilize test results across different architectures and configurations.
