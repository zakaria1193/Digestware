---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCCJIT
- JIT
- downcasting
- dynamic typing
- serialization
discussion_id: 5815119ebbc2fac15cdc17976856aaa4d28add15.camel@starynkevitch.net
source_type: public_inbox
title: GCCJIT dynamic down casting (GCC16 or future GCC17)
headline: Gccjit dynamic down casting (GCC16 or future GCC17)
tldr: Basile Starynkevitch asks about dynamic downcasting capabilities in GCCJIT to
  determine the type of a `gcc_jit_object` pointer.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Implementing dynamic downcasting may introduce runtime overhead.
- Adding type information to `gcc_jit_object` may increase memory usage.
- The design needs to consider the potential impact on performance and ABI stability.
- Alternative solutions might involve a different approach to serialization.
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Asks about dynamic downcasting capabilities in GCCJIT to identify the
    type of a `gcc_jit_object` pointer.
  quote: But is there any dynamic downcasting (or way to dynamically query the GCCJIT
    "class" of any gcc_jit_object pointer)?
- author: David Malcolm <dmalcolm@redhat.com>
  role: other
  position: No stance expressed.
  quote: null
primer_expert: GCCJIT is a library for creating GCC intermediate representation (IR)
  at runtime.  It allows programs to generate and compile code on the fly.  This question
  concerns the ability to determine the type of a `gcc_jit_object` at runtime, which
  is needed for serialization purposes. The request is whether one can query the kind
  of a JIT object.
primer_general: GCCJIT is a library that allows programs to generate machine code
  at runtime. It's useful for implementing features like dynamic languages or just-in-time
  compilation. This discussion is about how to determine the specific type of an object
  created with GCCJIT, which is needed for tasks like saving the generated code to
  a file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/5815119ebbc2fac15cdc17976856aaa4d28add15.camel@starynkevitch.net
bugzilla_url: null
date: '2026-05-07'
---

Basile Starynkevitch asks about dynamic downcasting capabilities in GCCJIT.  Specifically, he wants to determine the underlying type of a `gcc_jit_object` pointer (e.g., struct, lvalue, field, etc.) at runtime. He needs this functionality for serializing GCCJIT representations to JSON in his RefPerSys software.
