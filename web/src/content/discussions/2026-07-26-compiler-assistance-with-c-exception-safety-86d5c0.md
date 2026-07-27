---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c++
- exceptions
- compiler diagnostics
- frontend
discussion_id: CAP2b4GMiDA74ygCZXD2WO3hdp2f=sGfGQ7raTFRjkOrG+7ewXw@mail.gmail.com
source_type: public_inbox
title: Compiler assistance with making a C++ codebase exception safe
headline: Compiler assistance with C++ exception safety
tldr: Proposes a compiler warning for implicit exception handling in C++ codebases
  transitioning from -fno-exceptions.
proposer: Julian Waters <tanksherman27@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Increased compiler complexity and potential slowdown due to added analysis for implicit
  exception handling.
- Potential for false positives if the warning is too aggressive or cannot accurately
  distinguish between intentional and entirely unnecessary exception-handling code.
exchanges:
- author: Julian Waters <tanksherman27@gmail.com>
  role: proposer
  position: Suggests adding a compiler warning to flag implicit exception handling
    in C++ code to aid in making codebases exception-safe.
  quote: Given how it can be rather difficult to see where exactly invisible exceptions
    and exception handling will appear implicitly in code, would a warning that shows
    any implicit exception handling in user code be worthwhile to implement, or is
    it just a silly idea?
- author: LIU Hao <lh_mouse@126.com>
  role: contributor
  position: Acknowledges the issue of implicit exceptions and the difficulty in tracking
    them, as described by the proposer.
  quote: 'C++ exceptions can be a problematic issue when trying to enable them

    on a codebase that used to be compiled with -fno-exceptions set.

    Mysterious compiler and linker errors that used to not be an issue

    will suddenly appear if you try to remove the flag, or worse,

    exceptions and exception handling can invisibly be inserted into the

    assembled code in places where you don''t want them to be in. In my…'
primer_expert: This discussion concerns the GCC C++ frontend's handling of exceptions.
  Specifically, it addresses the challenge of migrating large codebases from -fno-exceptions
  to enabling exceptions, where the compiler might implicitly generate exception-handling
  code (e.g., setting up unwind tables) even for functions that don't explicitly throw
  or catch exceptions. The proposer suggests a diagnostic to help identify these implicit
  handlers.
primer_glossary:
- term: -fno-exceptions
  definition: A GCC compiler flag that disables exception handling support in the
    generated code, potentially reducing code size and improving performance by omitting
    exception-related runtime machinery.
- term: LTO
  definition: Link-Time Optimization. A process where the compiler optimizes code
    across multiple source files during the linking stage, potentially enabling more
    aggressive optimizations than traditional whole-program optimization.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used by GCC
    to represent code before it is translated into machine code. Optimizations are
    often performed on RTL.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAP2b4GMiDA74ygCZXD2WO3hdp2f=sGfGQ7raTFRjkOrG+7ewXw@mail.gmail.com
bugzilla_url: null
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

The proposer observes that C++ codebases previously compiled with -fno-exceptions can exhibit unexpected compiler and linker errors when exceptions are enabled. Even with LTO, a large number of exception handlers were found in temporary files when they were not intentionally used. The proposal suggests implementing a compiler warning to flag any implicit exception handling in user code, aiming to assist developers in making their codebases exception-safe.
