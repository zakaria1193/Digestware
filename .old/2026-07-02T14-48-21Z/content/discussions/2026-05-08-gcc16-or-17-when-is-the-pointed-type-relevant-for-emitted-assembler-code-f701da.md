---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- pointers
- alias analysis
- TBAA
discussion_id: 188b9599fcf75de7cc1f85f642599995e6ec06f5.camel@starynkevitch.net
source_type: public_inbox
title: 'GCC16 or 17: when is the pointed type relevant for emitted assembler code?'
headline: 'Gcc16 or 17: when is the pointed type relevant for emitted assembler code?'
tldr: Basile asks if using `void*` and explicit casts affects assembly code generation
  in GCC, sparking a discussion on type-based alias analysis.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Using void* can reduce type safety and potentially hinder compiler optimizations
  like type-based alias analysis.
- Using specific pointer types enables more aggressive optimizations but requires
  careful type management.
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Asks whether using only `void*` pointers with explicit casts affects assembly
    code generation.
  quote: If every generated pointer was void* and at every dereferencing occurrence
    explicitly casted to the actual data pointer, does that make any difference in
    generated assembler code?
- author: Richard Biener <richard.guenther@gmail.com>
  role: reviewer
  position: Explains that different pointer types enable type-based alias analysis
    (TBAA) for memory access disambiguation, which is not possible with `void*`.
  quote: when *p1 and *p2 have different pointer types we can disambiguate the two
    memory accesses.  If they are both void *, we can't.
primer_expert: Type-based alias analysis (TBAA) is a compiler optimization technique
  that uses type information to determine whether two pointers can point to the same
  memory location.  This enables the compiler to make assumptions about memory accesses
  and perform optimizations such as reordering or eliminating loads and stores. This
  is related to the `-fstrict-aliasing` flag.
primer_general: In C and C++, pointers are variables that store the memory address
  of other variables.  Type-based alias analysis is a compiler optimization that analyzes
  pointer types to determine if two pointers might point to the same memory location
  (aliasing). If the compiler can determine that two pointers cannot alias, it can
  perform optimizations to improve performance. Using `void*` disables this optimization.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/188b9599fcf75de7cc1f85f642599995e6ec06f5.camel@starynkevitch.net
bugzilla_url: null
date: '2026-05-08'
---

Basile Starynkevitch asks whether using `void*` for all pointers and casting them at each dereference impacts the generated assembly code in GCC 16 or 17. Richard Biener responds that using specific pointer types enables type-based alias analysis (TBAA), which helps the compiler disambiguate memory accesses. When all pointers are `void*`, this optimization is not possible.
