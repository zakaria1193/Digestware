---
project: binutils
subsystem: bfd/dwarf2
patch_id: null
tags:
- binutils
- bfd
- dwarf2
- addr2line
- debugging
discussion_id: 20260916035145.68086-1-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3] bfd/dwarf2: break equal-range function ties by DIE offset, not
  pointer'
headline: 'bfd/dwarf2: break equal-range function ties by DIE offset, not pointer'
tldr: Fixes addr2line to use DIE offset for tie-breaking, improving consistency.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves consistency and determinism of `addr2line` output.
- Fixes a bug related to DWARF parsing and tie-breaking.
- The chosen tie-breaking mechanism (DIE offset) is stable and reflects the structure
  of the DWARF information.
exchanges:
- author: Sam Price <thesamprice@gmail.com>
  role: proposer
  position: Proposes breaking ties in `lookup_address_in_function_table` by using
    DIE offset instead of `struct funcinfo` pointers, which vary due to allocator
    behavior.
  quote: Those come from bfd_zalloc.  Addresses increase within an objalloc chunk,
    but a new chunk can land below the old one, so which of the two functions addr2line
    named depended on where the allocator happened to put them.  On the same binary,
    23 of 200 addr2line -f -i runs named a different inlined function for the same
    address.  Only the function name moved; file and line never did.
primer_expert: This patch modifies the DWARF parsing logic within binutils' BFD library,
  specifically in `bfd/dwarf2.c`, affecting the `addr2line` utility. The `lookup_address_in_function_table`
  function currently resolves addresses to functions. When multiple functions cover
  the same address range (common with inlined subroutines), it breaks ties by comparing
  `struct funcinfo` pointers. This approach is unstable as these pointers depend on
  `bfd_zalloc`'s allocation order. The patch proposes using the Debug Information
  Entry (DIE) offset, a stable identifier, for tie-breaking to ensure deterministic
  results.
primer_glossary:
- term: addr2line
  definition: A utility that translates addresses into line number and function name
    information from object files, using DWARF debugging information.
- term: BFD
  definition: Binary File Descriptor library, a part of binutils that provides a common
    interface for reading and writing various executable binary file formats.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about source code, variables, types, and scopes.
- term: DIE
  definition: Debug Information Entry. A fundamental unit within DWARF data, representing
    a symbol, type, or other program construct.
- term: inlined subroutine
  definition: A function call that has been replaced by the actual code of the called
    function at the call site by the compiler, to improve performance. In DWARF, this
    is represented by a DW_TAG_inlined_subroutine DIE.
- term: objalloc
  definition: An object allocator, likely within BFD, used for managing memory for
    DWARF data structures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260916035145.68086-1-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in binutils' addr2line tool where tie-breaking between functions with identical source code ranges was based on pointer comparison of `struct funcinfo`. Since these pointers could vary due to memory allocation order, addr2line sometimes reported different inlined functions for the same address. The change proposes using the Debug Information Entry (DIE) offset instead, which is a stable identifier, ensuring consistent reporting of inlined functions.
