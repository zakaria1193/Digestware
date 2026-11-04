---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- ada
- vectorization
commit_hash: c0c0ebf5b45db66b5a487fb3e24f3cbb3a2818f5
source_type: github
author: Eric Botcazou
headline: Ada test case added for vectorization optimization bug
tldr: New Ada test case added to verify a fix for a vectorization optimization bug.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a new Ada test case (`gnat.dg/specs/vect1.ads`) to
  the GCC testsuite. This test is specifically designed to exercise and validate the
  fix for bug report PR tree-optimization/127475, which likely pertains to issues
  encountered during the vectorization optimization phase for Ada code.
primer_glossary:
- term: testsuite
  definition: A collection of test programs and scripts used to verify the correctness
    and functionality of a compiler or software system.
- term: Ada
  definition: A structured, statically typed, imperative, and object-oriented high-level
    programming language, widely used in defense and aerospace systems.
- term: vectorization
  definition: An optimization technique that transforms code to operate on multiple
    data elements simultaneously using specialized CPU instructions (e.g., SIMD).
- term: PR tree-optimization
  definition: Problem Report related to the tree optimization passes within the GCC
    compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c0c0ebf5b45db66b5a487fb3e24f3cbb3a2818f5
date: '2026-11-03'
is_stub: true
stub_reason: low_score
---

A new Ada test case has been added to the GCC testsuite to address a bug related to vectorization optimization. The test case specifically targets PR tree-optimization/127475, ensuring that the fix implemented for this issue is correctly verified.
