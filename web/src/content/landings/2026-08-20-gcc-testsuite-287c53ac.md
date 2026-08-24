---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- i386
- vectorization
commit_hash: 287c53ac300cb752710b4f154456d646b50a60d1
source_type: github
author: H.J. Lu
headline: 'vect-cbranch-cond-any-128.c: Compile with -mtune=generic'
tldr: Ensures test case compilation uses a generic tuning for i386 to avoid cost model
  differences.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The i386 testsuite includes a case for conditional vectorized branches.
  Compiling it with -mtune=generic ensures consistent code generation across different
  target tuning options, preventing spurious test failures due to subtle differences
  in instruction scheduling or selection.
primer_glossary:
- term: -mtune=generic
  definition: A GCC flag that optimizes code for a generic processor, rather than
    a specific CPU model. This can help ensure consistent behavior and prevent failures
    in test suites that might be sensitive to CPU-specific optimizations.
- term: vect-cbranch-cond-any-128.c
  definition: A GCC test case file in the i386 target suite that likely tests vectorized
    conditional branches for 128-bit data types.
- term: cost models
  definition: Internal mechanisms within the compiler that estimate the performance
    of different code sequences. Differences in cost models can lead to different
    instruction choices and ordering.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/287c53ac300cb752710b4f154456d646b50a60d1
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

This commit updates the test suite by compiling vect-cbranch-cond-any-128.c with -mtune=generic. This change prevents test failures caused by variations in code sequences generated from different default cost models on i386 architecture.
