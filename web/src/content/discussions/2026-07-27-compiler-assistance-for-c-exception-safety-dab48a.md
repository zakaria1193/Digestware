---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c++
- exceptions
- compiler options
- lto
discussion_id: CAP2b4GOFrRX_U17HC1WZRrK0tguEER+EhCU-83T+OXQXmdaLaw@mail.gmail.com
source_type: public_inbox
title: 'Re: Compiler assistance with making a C++ codebase exception safe'
headline: Compiler assistance for C++ exception safety
tldr: Discusses GCC options for exception handling, clarifying their scope and limitations
  for porting codebases.
proposer: Julian Waters <tanksherman27@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enabling C++ exceptions can significantly increase code size and complexity due
  to the runtime support required for exception handling.
- Compiler optimizations like LTO may not always eliminate all exception handling
  code, leading to potential bloat and performance overhead.
exchanges:
- author: Julian Waters <tanksherman27@gmail.com>
  role: proposer
  position: Explains that GCC options related to exception specifications (like throw()
    to noexcept) do not address the core issue of invisible exception handling code
    insertion, which complicates porting to exception-enabled codebases.
  quote: 'To my knowledge those options relate to exception specifications

    rather than exceptions as a whole, the former just turns throw() into

    noexcept, which doesn''t seem like it''ll help much with C++17 and above

    code. The latter can be pretty helpful, but I think it only controls

    the case where exception specifications are violated, such as a

    noexcept method calling a method with no exception specifica…'
- author: LIU Hao <lh_mouse@126.com>
  role: other
  position: Initiated the discussion by describing mysterious compiler/linker errors
    and unexpected exception handler insertions when `-fno-exceptions` is removed.
  quote: 'C++ exceptions can be a problematic issue when trying to enable them

    on a codebase that used to be compiled with -fno-exceptions set. Mysterious compiler
    and linker errors that used to not be an issue

    will suddenly appear if you try to remove the flag, or worse, exceptions and exception
    handling can invisibly be inserted into the assembled code in places where you
    don''t want them to be in. In my…'
primer_expert: This thread discusses the complexities of enabling C++ exceptions in
  a large codebase that previously relied on `-fno-exceptions`. The issue revolves
  around the compiler (GCC) implicitly inserting exception handling code, even in
  code that does not explicitly use exceptions or standard library components that
  throw. Optimizations like Link-Time Optimization (LTO) do not appear to eliminate
  these handlers, leading to unexpected behavior and build failures. Participants
  are clarifying the scope of compiler flags related to exception specifications versus
  the fundamental generation of exception-…
primer_glossary:
- term: -fno-exceptions
  definition: A GCC compiler flag that disables the generation of code for C++ exception
    handling, suppressing runtime support for `throw`, `try`, and `catch`.
- term: noexcept
  definition: A C++ specifier that indicates a function is not expected to throw exceptions.
    Compilers may optimize code more aggressively when `noexcept` is used.
- term: LTO
  definition: Link-Time Optimization is a compiler optimization technique where the
    linker performs optimizations across multiple object files, potentially leading
    to better code than traditional link-time optimizations.
- term: Exception specifications
  definition: In C++, constructs like `throw()` that declare which exceptions a function
    might throw. These have been superseded by `noexcept` in modern C++.
- term: exception handler
  definition: A block of code designed to catch and manage exceptions that are thrown
    during program execution.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/CAP2b4GOFrRX_U17HC1WZRrK0tguEER+EhCU-83T+OXQXmdaLaw@mail.gmail.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This discussion addresses challenges in enabling C++ exceptions on codebases previously compiled with `-fno-exceptions`. Participants clarify that options like `throw()` to `noexcept` conversion and pragmas targeting exception specifications primarily affect exception contracts, not the implicit insertion of exception handling code. The core problem remains understanding where and why exceptions are introduced, especially with optimizations like LTO, which may not eliminate all implied exception handlers.
