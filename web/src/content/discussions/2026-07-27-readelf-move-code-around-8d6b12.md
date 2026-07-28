---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- refactoring
- ELF
- code-quality
- maintainability
discussion_id: b76972ea-76da-4e40-ae59-2d6342f4cde1@suse.com
source_type: public_inbox
title: '[PATCH RFC 5/5] readelf: move code around'
headline: 'readelf: move code around'
tldr: Refactors `readelf.c` to reduce `#ifdef` directives and improve code organization.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces code duplication and `#ifdef` complexity in `readelf.c`.
- Improves maintainability by consolidating logic for 32-bit and 64-bit ELF handling.
- Marginally decreases readability for those unfamiliar with the `ElfXX` macro trick.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Submits the final patch (5/5) in a series that rearranges code within
    `readelf.c` to reduce `#ifdef` directives and improve code organization.
  quote: 'Try to limit recently introduced #ifdef-ary at least a little.

    --- I was hoping for the overall effect to be better, yet I also didn''t want

    to go too far with the re-arrangement. One aspect I noticed: Instead of

    the trivial get_elf_symbols() wrapper we could use a function pointer

    instead. That, however, already wouldn''t quite extend to

    get_section_headers() and get_dynamic_section(), let alone

    g…'
primer_expert: This patch is part of a series aimed at refactoring `readelf.c`. It
  specifically addresses the code duplication and conditional compilation required
  to handle both 32-bit and 64-bit ELF file formats. The author moves sections of
  code, including the definitions for `get_program_headers` and `get_dynamic_section`,
  and utilizes C preprocessor macros (`ElfXX`) to include the same source file (`readelf.c`)
  twice with different `ElfXX` definitions, thereby reducing explicit `#ifdef` blocks
  for 32-bit vs. 64-bit handling. The intent is to simplify the source file and reduce
  maintenance burden.
primer_glossary:
- term: readelf
  definition: A utility in GNU Binutils that displays information about ELF (Executable
    and Linkable Format) files.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on Unix-like systems.
- term: '#ifdef'
  definition: 'A C preprocessor directive used for conditional compilation. Code blocks
    enclosed in #ifdef/#endif are only included in the compilation if a specified
    macro is defined.'
- term: Function pointer
  definition: A variable that stores the memory address of a function, allowing functions
    to be called indirectly.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/b76972ea-76da-4e40-ae59-2d6342f4cde1@suse.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch is the fifth in a series, aiming to refactor the `readelf.c` source file by rearranging code to minimize conditional compilation (`#ifdef`) blocks. The goal is to improve code cleanliness and maintainability. While the author notes that a more significant refactoring (e.g., using function pointers) might offer greater benefits, this patch focuses on a more modest code movement to limit the presence ofifdef-heavy sections.
