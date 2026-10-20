---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
commit_hash: b2dbf7c3ee78dba8b038d69bcf62195bc4896ca0
source_type: github
author: Richard Biener
headline: testsuite/127942 - fixup dg-optimized checks
tldr: Correct testsuite checks for vectorization to use dump-file scanning.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testsuite directive `dg-optimized` was intended to check optimized
  output, but it was not effectively verifying generated code, particularly for vectorization
  tests. This commit reverts the use of `dg-optimized` for specific vectorization
  tests (like `bb-slp-pr126306-1.c`) in favor of scanning compiler dump files. This
  change addresses issues related to insufficient coverage and excessive errors encountered
  when attempting to use `dg-optimized` for vectorization scenarios, such as those
  involving `vect64`.
primer_glossary:
- term: testsuite
  definition: A collection of tests used to verify the correctness and performance
    of the compiler. GCC has extensive testsuites for various components and optimizations.
- term: dg-optimized
  definition: A GCC testsuite directive that marks a test case expected to pass when
    compiled with optimization flags. It's typically used to check generated code.
- term: vectorization
  definition: An optimization technique that transforms scalar code (operating on
    single data items) into vector code (operating on multiple data items simultaneously
    using SIMD instructions).
- term: dump-file scanning
  definition: A method of testing in the GCC testsuite where the output of compiler
    dump files (e.g., generated assembly or intermediate representations) is searched
    for specific patterns or keywords to verify compiler behavior.
- term: SLP
  definition: Straight-Line Peculiar optimization. A vectorization technique that
    identifies opportunities to vectorize straight-line code sequences.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b2dbf7c3ee78dba8b038d69bcf62195bc4896ca0
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

The `dg-optimized` checks in the GCC testsuite were found to be ineffective, as they did not actually verify any generated code. This commit replaces these ineffective checks with traditional dump-file scanning for vectorization tests. This approach avoids issues with coverage and excess errors that arose when trying to fully rely on `dg-optimized` for vectorization, specifically addressing problems found with `vect64`.
