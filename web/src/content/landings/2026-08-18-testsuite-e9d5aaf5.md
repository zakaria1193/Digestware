---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- x86
- optimization
commit_hash: e9d5aaf572e8d14b0edd4294f69f5a4e8c689c54
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Fix recent test FAILs on ia32'
tldr: Minor adjustments made to GCC test suite to resolve recent failures on the ia32
  architecture.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Recent regressions have been observed on ia32 in the `tree-ssa` test
  suite. This commit applies targeted fixes to several `dg` tests (`divmul-mod-1.c`,
  `round-up-ior-1.c`, `vec-mask-zero-1.c`, `vector-alignup-1.c`, `vec-narrow-1.C`,
  `vec-narrow-minmax-2.C`) that were exhibiting excess errors or incorrect scan-tree-dump
  outputs. The changes involve tweaking test expectations to align with the observed
  behavior on ia32, ensuring these optimization passes remain stable.
primer_glossary:
- term: tree-ssa
  definition: A GCC optimization pass that transforms the compiler's intermediate
    representation (GIMPLE) into Static Single Assignment (SSA) form, which simplifies
    many optimization algorithms.
- term: ia32
  definition: The 32-bit Intel Architecture, commonly referring to x86 processors
    in their 32-bit mode.
- term: scan-tree-dump
  definition: A debugging and testing utility within GCC that analyzes the compiler's
    intermediate representation at various stages to verify optimization correctness.
- term: g++.dg
  definition: A subdirectory within the GCC testsuite containing regression tests
    specifically for the GNU C++ compiler (g++).
- term: vec-narrow
  definition: Refers to optimization tests involving the narrowing of vector data
    types, where a wider vector is converted into a narrower one.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e9d5aaf572e8d14b0edd4294f69f5a4e8c689c54
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

This commit addresses several test failures observed on the ia32 architecture within the GCC test suite. The failures were related to `tree-ssa` test cases, including those involving division-multiplication-modulo operations, round-up bitwise operations, and vector mask zeroing. Adjustments were made to the test configurations and expected outputs to resolve these issues, ensuring the integrity of the test suite on this platform.
