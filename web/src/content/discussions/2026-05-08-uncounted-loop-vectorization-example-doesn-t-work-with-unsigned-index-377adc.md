---
project: gcc
subsystem: gcc
patch_id: null
tags: []
discussion_id: RBlv2bEIAjMT7EObrykvjwAIayfw7zt694lcYZussS7znSTokffPSGSvvkr5BMTNeJDwORowmtXj12FGWUoHrFkt6fgv2O_aUQEsMOX3Cdk=@nicula.xyz
source_type: public_inbox
title: Uncounted loop vectorization example doesn't work with unsigned index
headline: Uncounted loop vectorization example doesn't work with unsigned index
tldr: The uncounted loop vectorization in GCC 16 doesn't work with unsigned loop indexes
  in the example.
proposer: Ionuț Nicula <nicula@nicula.xyz>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Loop vectorization is a compiler optimization that transforms a loop
  to execute multiple iterations in parallel using SIMD instructions.  The compiler
  analyzes the loop's data dependencies and control flow to safely execute multiple
  iterations concurrently, improving performance on suitable hardware. The standard
  test case is gcc/testsuite/gcc.dg/vect/vect-uncounted_1.c.
primer_general: Vectorization is a compiler optimization technique that transforms
  scalar operations into vector operations, enabling the processor to perform the
  same operation on multiple data elements simultaneously. This is especially useful
  in loops, where the same sequence of operations is repeated multiple times. Compilers
  may struggle when the number of loop iterations isn't known ahead of time.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/RBlv2bEIAjMT7EObrykvjwAIayfw7zt694lcYZussS7znSTokffPSGSvvkr5BMTNeJDwORowmtXj12FGWUoHrFkt6fgv2O_aUQEsMOX3Cdk=@nicula.xyz
bugzilla_url: null
date: '2026-05-08'
---

Ionuț Nicula reports that the uncounted loop vectorization example in GCC 16 fails when using an *unsigned* type for the loop index, while working correctly with signed integers. This may be a limitation in the current implementation. Users who rely on loop vectorization with unsigned indexes should be aware of this limitation.
