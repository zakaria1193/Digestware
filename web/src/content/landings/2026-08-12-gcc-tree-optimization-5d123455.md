---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- x86
- avx512
- vectorization
- optimization
commit_hash: 5d123455af27c526d9aa1e12a47d0177262b0e51
source_type: github
author: Richard Biener
headline: Vectorizer handles MMX/SSE mask interaction with AVX512.
tldr: Vectorizer now correctly converts between integer and vector integer masks for
  AVX512.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The x86 backend has distinct integer and vector integer mask representations.
  AVX512 requires converting between these for vectorization. This patch adds support
  for V2SImode by using vcond_mask in vectorizable_conversion to handle the transition
  from integer mode masks to vector integer mode masks, which was previously missing
  pattern support.
primer_glossary:
- term: AVX512
  definition: An extension to x86 instruction set architecture providing 512-bit wide
    vector registers and instructions, enabling wider data parallelism.
- term: Vectorizer
  definition: A compiler component that transforms loops and scalar code into vector
    instructions for parallel execution on suitable hardware.
- term: V2SImode
  definition: A GCC internal representation for a vector of two single-precision floating-point
    values or two-element integer vectors.
- term: vcond_mask
  definition: An AVX512 instruction that conditionally selects elements from a destination
    vector based on a mask, useful for implementing masked operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5d123455af27c526d9aa1e12a47d0177262b0e51
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

The GCC vectorizer can now handle the interaction between MMX/SSE integer masks and AVX512 vector integer masks. It introduces a conversion for V2SImode using vcond_mask, addressing a gap in pattern recognition for mask representation. This improves vectorization of code using AVX512 instructions.
