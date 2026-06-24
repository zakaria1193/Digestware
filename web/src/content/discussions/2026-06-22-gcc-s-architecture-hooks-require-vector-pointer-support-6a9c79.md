---
project: gcc
subsystem: rfc
patch_id: null
tags:
- gcc
- vectorization
- machine-modes
- abi
- rtl
discussion_id: 82bf28f3-5543-4925-98d9-5ddf7dc23855@baylibre.com
source_type: public_inbox
title: 'Re: RFC: Allow "(mem:<vectype> (reg:<vectype>))"'
headline: GCC's architecture hooks require vector pointer support
tldr: GCC's target architecture hooks `TARGET_POINTER_MODE` and `TARGET_ADDR_SPACE_POINTER_MODE`
  need modifications to support vector pointer types, to avoid issues…
proposer: Andrew Stubbs <ams@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 6
technical_tradeoffs:
- Maintaining scalar return types for some pointer mode hooks while introducing vector
  acceptance in `TARGET_ADDR_SPACE_VALID_POINTER_MODE` could lead to inconsistencies
  or complex interaction logic.
- LRA's transformations of memory operations with vector types might introduce inefficiencies
  or incorrect code if not carefully managed.
exchanges:
- author: Andrew Stubbs <ams@baylibre.com>
  role: proposer
  position: Proposes to address issues related to GCC's architecture hooks for pointer
    modes by allowing `TARGET_ADDR_SPACE_VALID_POINTER_MODE` to accept vector types,
    while encountering new challenges with LRA's handling of vector memory operations.
  quote: I've been working on this proposal some more. I've solved the above problem
    by keeping all the hooks returning pointer/address types scalar, but changing
    TARGET_ADDR_SPACE_VALID_POINTER_MODE to accept vector types, so the backend can
    approve them. When the target independent code encounters a vector of addresses
    it checks that the inner mode matches the appropriate hook values.
- author: Richard Biener <richard.guenther@gmail.com>
  role: reviewer
  position: Acknowledges the receipt of the updated proposal and the ongoing work.
  quote: 'On 18/03/2026 17:12, Andrew Stubbs wrote: > On 17/03/2026 15:25, Andrew
    Stubbs wrote: >> I have run out of places that ICE or cause test failures (for
    C) when >> the mode is a vector. Do you have any other suggestions to find them?
    >> >> (I already plan to test C++ and Fortran.) > > I found some problems ....'
- author: Michael Matz <matz@suse.de>
  role: reviewer
  position: Raises a question about the rationale of combining scalar and vector pointer
    modes, noting the need for consistency across the architecture hooks.
  quote: 'TARGET_POINTER_MODE and TARGET_ADDR_SPACE_POINTER mode only return one mode,
    but now we have multiple valid modes: DImode, V2DImode, V4DImode, etc. They also
    return scalar_int_mode so I can''t even invent a new address space for the vector
    pointers.'
primer_expert: In GCC, `machine modes` define the size and type of data that the machine
  can operate on, including scalar integer modes (`DImode`) and vector integer modes
  (`V2DImode`, `V4DImode`). Architecture-specific hooks, such as `TARGET_POINTER_MODE`
  and `TARGET_ADDR_SPACE_POINTER_MODE`, are used by the compiler to determine the
  appropriate machine mode for pointers within different address spaces. This RFC
  highlights a challenge when these hooks are expected to return only scalar pointer
  types, while the compiler's intermediate representation (RTL) may involve vector
  memory operations (e.g., `(mem:<v…
primer_general: Compilers work by translating high-level programming language code
  into low-level machine instructions. A part of this involves figuring out how data
  is stored in memory and how to access it. For modern processors, this can include
  "vector" operations, where a single instruction can process multiple pieces of data
  at once. This proposal addresses a problem in how GCC (the GNU Compiler Collection)
  handles "pointers" (memory addresses) that are part of these vector operations.
  Historically, GCC's internal rules (called "hooks") assumed pointers were always
  single, scalar values. However, some advanced processor features require "vector
  pointers" – essentially, a list of memory addresses that can be processed in parallel.
  This RFC explains the challenges of adapting GCC's internal architecture to properly
  support these vector pointers, especially when it comes to memory access instructions,
  to ensure that compiled programs can take full advantage of modern hardware.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/a41b8b32-d2eb-4ba5-b326-6d40d5f446eb@baylibre.com
bugzilla_url: null
date: '2026-06-22'
is_stub: false
---

This RFC proposes allowing vector types in GCC's memory and register operands, particularly for vector pointers. The current architecture hooks, such as `TARGET_POINTER_MODE`, only return scalar modes, making it difficult to support vector pointers. The proposer has resolved some initial problems by allowing `TARGET_ADDR_SPACE_VALID_POINTER_MODE` to accept vector types but is encountering new issues with how the Live Range Allocator (LRA) transforms memory operations involving vector types.
