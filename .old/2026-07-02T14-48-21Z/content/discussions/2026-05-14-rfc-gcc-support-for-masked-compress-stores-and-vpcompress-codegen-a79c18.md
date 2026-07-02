---
project: gcc
subsystem: rfc
patch_id: null
tags:
- gcc
- loop vectorization
- AVX-512
- VPCOMPRESS
- code generation
discussion_id: 20260514062146.3464666-1-Raghesh.Aloor@amd.com
source_type: public_inbox
title: 'RFC: GCC support for masked compress stores and VPCOMPRESS-style codegen'
headline: 'RFC: GCC support for masked compress stores and VPCOMPRESS codegen'
tldr: Proposes extending GCC's loop vectorizer to generate AVX-512 VPCOMPRESS instructions
  for predicated stores into a buffer.
proposer: Raghesh Aloor <Raghesh.Aloor@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased compiler complexity to recognize and optimize the specific loop pattern.
- Potential for increased code size if VPCOMPRESS is not profitable in all cases.
- Requires careful tuning of heuristics to determine when VPCOMPRESS is beneficial.
- May introduce new dependencies on AVX-512 instruction set.
exchanges: []
primer_expert: This proposal focuses on enabling VPCOMPRESS codegen in GCC's loop
  vectorizer, specifically targeting loops with predicated stores into a buffer, a
  pattern commonly found after if-conversion. The goal is to improve performance on
  x86-64 architectures with AVX-512 support by utilizing VPCOMPRESS instructions to
  compress the stored data based on the predicate mask. The interaction with the loop
  vectorizer and code generation backend are key aspects of this work.
primer_general: Loop vectorization is a compiler optimization technique that transforms
  loops to execute multiple iterations simultaneously, leveraging Single Instruction,
  Multiple Data (SIMD) instructions.  Predicated execution involves conditionally
  executing instructions within a loop based on a predicate or mask. AVX-512 is an
  extension to the x86 instruction set that provides wider registers (512 bits) and
  support for masked operations, allowing for more efficient vectorization of loops
  with conditional stores. VPCOMPRESS is a specific AVX-512 instruction that compresses
  elements of a vector based on a mask. This proposal aims to improve performance
  by enabling GCC to automatically generate VPCOMPRESS instructions for loops with
  specific patterns of predicated stores, which can be challenging to optimize otherwise.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260514062146.3464666-1-Raghesh.Aloor@amd.com
bugzilla_url: null
date: '2026-05-14'
is_stub: false
---

This RFC proposes extending GCC's loop vectorizer to recognize loops with predicate-guarded stores into a buffer with an offset incremented under the same predicate, enabling the backend to emit AVX-512 VPCOMPRESS instructions when profitable. This change addresses PR tree-optimization/91198, where GCC failed to generate AVX-512 compress/expand instructions in relevant cases. The initial prototype patch for phase 1 will be sent to the gcc-patches list soon, with the aim of improving performance on code that can benefit from masked compress stores.
