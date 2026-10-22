---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- avx512
- bugfix
commit_hash: f4b64250a70482fbb51d6bb97fae481f90aa9649
source_type: github
author: Richard Biener
headline: Prevent mixed AVX512/AVX2 mask styles with loop masking
tldr: Ensures consistent mask types for AVX512 loop masking.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When AVX512 loop masking is enabled, it conventionally assumes integer-type
  masks throughout. However, if only a subset of AVX512 features is active, it's possible
  to encounter mixed-style masks (e.g., some integer, some float masks). This scenario
  is not supported. The patch in `tree-vect-loop.cc` updates `vect_verify_full_masking_avx512`
  to enforce that all loop masks must be of integer mode. If this condition isn't
  met, loop masking is disabled for that loop to avoid compiler internal errors (ICEs)
  during the transformation phase.
primer_glossary:
- term: AVX512
  definition: Advanced Vector Extensions 512. A set of SIMD instructions for x86 processors
    that operate on 512-bit vectors.
- term: AVX2
  definition: Advanced Vector Extensions 2. A set of SIMD instructions for x86 processors
    that operate on 256-bit vectors.
- term: loop masking
  definition: A vectorization technique that uses masks to control which elements
    within a vector are processed in each iteration, particularly useful for loops
    with conditional execution or non-power-of-two iterations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f4b64250a70482fbb51d6bb97fae481f90aa9649
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This change prevents the vectorizer from using mixed AVX512 and AVX2 style masks when loop masking is enabled with AVX512, which is an unsupported configuration. It adds a verification step in `vect_verify_full_masking_avx512` to ensure all loop masks are of integer type. If inconsistencies are detected, loop masking is disabled instead of causing an internal compiler error during transformation.
