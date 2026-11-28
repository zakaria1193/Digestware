---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- avx512
- optimization
- middle-end
- vectorization
commit_hash: c6a54d3c1476fe9f28721d75696af5723ab0d2bc
source_type: github
author: Richard Biener
headline: middle-end/129022 - mishandled QImode AVX512 mask in VIEW_CONVERT folding
tldr: Fixes incorrect handling of AVX512 mask types during VIEW_CONVERT folding, preventing
  compiler errors.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `fold_view_convert_vector_encoding` function in `fold-const.cc`
  mishandles AVX512 mask types (like `__mask8`, `__mask16`, `__mask32`, `__mask64`),
  which are represented using QImode and have a `TYPE_SIZE` of 8. The function's element
  bits computation erroneously assumes these are standard integer types, leading to
  incorrect folding. This patch modifies the function to detect these boolean vectors
  with padding and reject them, falling back to the general `VIEW_CONVERT` logic which
  handles them correctly.
primer_glossary:
- term: AVX512
  definition: Advanced Vector Extensions 512. An instruction set extension for x86
    microprocessors that increases the width of SIMD registers to 512 bits, allowing
    for wider vector operations.
- term: QImode
  definition: In GCC's internal representation, a machine mode representing a single
    byte (8 bits).
- term: VIEW_CONVERT
  definition: An operation in GCC's intermediate representation that reinterprets
    the bits of one type as another type, often used for type punning or vector element
    conversions.
- term: folding
  definition: An optimization technique where constant expressions or operations are
    evaluated at compile time rather than at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c6a54d3c1476fe9f28721d75696af5723ab0d2bc
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

AVX512 mask vectors, which use QImode and have a TYPE_SIZE of 8, were causing issues in the `fold_view_convert_vector_encoding` function. This function incorrectly computed element bits for these mask types, leading to compilation errors. The fix makes the function bail out on these specific boolean vectors, falling back to a more generic VIEW_CONVERT handling that avoids the error.
