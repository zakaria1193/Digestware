---
project: gcc
subsystem: gcc
patch_id: null
tags:
- libgomp
- ABI
- C++
- abidiff
discussion_id: 8733tjh9v7.fsf@seketeli.org
source_type: public_inbox
title: 'Re: Transitioning libgomp from C to C++ implementation'
headline: Transitioning libgomp from C to C++ implementation
tldr: Advice on using abidiff to compare C and C++ libgomp implementations for ABI
  stability.
proposer: Dodji Seketeli <dodji@seketeli.org>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring ABI stability when transitioning from C to C++ requires careful tooling
  and review to prevent regressions.
exchanges:
- author: Dodji Seketeli <dodji@seketeli.org>
  role: proposer
  position: Explains how to use `abidiff` to check for ABI compatibility between C
    and C++ versions of libgomp.
  quote: "For each platform you wish to ensure ABI stability for, build a\nlibgomp.so.old\
    \ version (the last C-only implementation maybe?) and a\nlibgomp.so.new (the new\
    \ C++ implementation) and basically do:\n\n    $ abidiff libgomp.so.old libgomp.so.new\n\
    \nNo change should be reported beside potential new entry points\nadditions.\n\
    \nAlso, maybe review the reported additions to be sure they don't have C++\nmangling."
primer_expert: This exchange concerns the transition of libgomp, GCC's OpenMP runtime
  library, from a C implementation to C++. The core issue is ensuring the C++ implementation
  maintains binary compatibility (ABI) with the existing C version. The advice focuses
  on using `libabigail`'s `abidiff` tool to detect any ABI regressions or unexpected
  C++ name mangling.
primer_glossary:
- term: libgomp
  definition: The GNU OpenMP runtime library, which provides support for OpenMP directives
    in GCC.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code communicates
    at the binary level, including function calling conventions and data structure
    layouts. Maintaining ABI compatibility is crucial for allowing independently compiled
    components to interoperate.
- term: abidiff
  definition: A tool from the libabigail library used to compare the ABIs of two versions
    of a library or executable, highlighting differences.
- term: C++ mangling
  definition: The process by which C++ compilers alter function and variable names
    to encode additional information (like argument types and namespaces) into the
    symbol names, allowing for function overloading and other C++ features. This can
    affect symbol resolution if not handled carefully across library versions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/8733tjh9v7.fsf@seketeli.org
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

Dodji Seketeli provides guidance on how to verify ABI compatibility when transitioning libgomp from C to C++. The recommended approach involves using the `abidiff` tool to compare old and new library versions, ensuring no unintended changes or C++ mangling are introduced.
