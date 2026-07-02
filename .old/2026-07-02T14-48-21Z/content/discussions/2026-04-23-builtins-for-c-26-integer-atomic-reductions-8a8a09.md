---
project: gcc
subsystem: gcc
patch_id: null
tags: []
discussion_id: 9f3b700b-23dd-4eef-9aae-7fdf2e28e2f1@nvidia.com
source_type: public_inbox
title: 'Re: [RFC] Builtins for C++26 integer atomic reductions'
headline: Builtins for C++26 integer atomic reductions
tldr: The author provides a detailed explanation with litmus tests demonstrating the
  necessity of new builtins for C++26 integer atomic reductions due to memory mode…
proposer: Matthew Malcomson <mmalcomson@nvidia.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The discussion concerns the C++ memory model and the need for compiler
  builtins to correctly implement atomic reductions.  The author uses litmus tests
  to illustrate how relaxed atomic loads and compare-and-swap (CAS) operations can
  lead to reordering issues around thread fences, necessitating new builtins to guarantee
  memory model semantics for C++26.
primer_general: In concurrent programming, atomic operations are crucial for managing
  shared data accessed by multiple threads, preventing data races and ensuring consistency.  The
  C++ memory model defines how these atomic operations behave, particularly regarding
  memory ordering.  This proposal argues that existing atomic operations are insufficient
  for implementing certain reduction operations (e.g., incrementing a variable) under
  the C++26 standard, requiring new compiler builtins to guarantee correct behavior
  in multi-threaded scenarios. Litmus tests are small programs designed to expose
  subtle memory ordering issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/9f3b700b-23dd-4eef-9aae-7fdf2e28e2f1@nvidia.com
bugzilla_url: null
date: '2026-04-23'
is_stub: false
---

The author provides a detailed explanation of why new builtins are required for C++26 integer atomic reductions.  They use litmus tests to demonstrate the memory model semantics that necessitate these new builtins.  This discussion highlights the complexities of ensuring correct atomic operations in multi-threaded C++ code.
