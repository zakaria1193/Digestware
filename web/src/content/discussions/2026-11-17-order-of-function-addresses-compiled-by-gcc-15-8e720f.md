---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- linker
- shared objects
- runtime
discussion_id: 4e2d84a2a15018ea1f61a84adae36190fcfa468a.camel@starynkevitch.net
source_type: public_inbox
title: order of function adresses compiled by GCC (15 or later) on Linux
headline: Order of function addresses compiled by GCC (15+)
tldr: Developers are asking if GCC guarantees a specific order of function addresses
  in shared objects, which could impact runtime introspection.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- 'Runtime introspection vs. optimization: Guaranteeing symbol order might constrain
  compiler/linker optimizations for better performance or code locality.'
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Asks whether GCC guarantees a specific order of function addresses in
    shared objects, and if textual source order correlates with runtime address order.
  quote: 'Assume a recent GCC (15 or later) on a 64 bits processor and Linux system
    (eg ARM64 or AMD64)


    Assume compilation of a single C or C++ file (foo.c or foo.cxx) into a shared
    (dlopenable) object foo.so (so with options -O2 -fPIC -shared)


    Assume also that no function is declared with attributes (other than format).


    Is there in practice an order of the addresses (as obtained by dlsym) of the extern…'
- author: Richard Biener <richard.guenther@gmail.com>
  role: reviewer
  position: Acknowledges the question about function address ordering in shared objects,
    implying it's a valid concern for runtime introspection.
  quote: 'On Tue, Nov 17, 2026 at 11:42 AM Basile STARYNKEVITCH

    <basile@starynkevitch.net> wrote:

    > ...

    > Is there in practice an order of the addresses (as obtained by

    dlsym) of the external functions of foo.so?'
- author: Ben Boeckel <ben.boeckel@kitware.com>
  role: other
  position: Quotes Richard Biener's reply, indicating interest in the discussion about
    function address ordering and GCC's behavior.
  quote: 'On Tue, Nov 17, 2026 at 16:02:36 +0100, Richard Biener via Gcc wrote:

    > On Tue, Nov 17, 2026 at 11:42 AM Basile STARYNKEVITCH

    > <basile@starynkevitch.net> wrote:

    > > Assume a recent GCC (15 or later) on a 64 bits processor and Linux

    > > system (eg ARM64 or AMD64)

    > >

    > > Assume compilation of a single C or C++ file (foo.c or foo.cxx) into a

    > > shared (dlopenable) object foo.so (so with options -…'
primer_expert: This thread discusses function symbol ordering in GCC-generated shared
  objects (.so files) on Linux. The core question is whether compiler optimizations
  (e.g., function grouping, reordering for locality) or linker behavior can alter
  the order of function symbols as they appear in the dynamic symbol table, impacting
  runtime analysis tools that rely on symbol address proximity or ordering. The context
  is specifically GCC 15+ and PIC/shared object compilation.
primer_glossary:
- term: dlsym
  definition: A POSIX function that retrieves the address of a symbol (like a function)
    from a dynamically loaded object (e.g., a shared library).
- term: dladdr
  definition: A function that returns information about a symbol found at a given
    address, including its name and the path to the shared object it belongs to.
- term: shared object
  definition: A file containing compiled code and data that can be loaded by multiple
    programs simultaneously at runtime. On Linux, these typically have a .so extension.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. It's essential for shared libraries.
- term: GCC 15+
  definition: Refers to version 15 or later of the GNU Compiler Collection, a widely
    used C/C++ compiler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/4e2d84a2a15018ea1f61a84adae36190fcfa468a.camel@starynkevitch.net
bugzilla_url: null
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

A developer is inquiring about the ordering of function addresses obtained via `dlsym` when compiling with GCC 15 or later on Linux, particularly for shared objects. The question arises from a desire to use `dladdr` and `dlsym` for runtime introspection. The concern is whether textual source code order correlates with runtime address order and under what conditions GCC might reorder functions.
