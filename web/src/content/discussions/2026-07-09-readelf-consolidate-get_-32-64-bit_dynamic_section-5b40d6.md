---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- elf
- dynamic section
- refactoring
- code consolidation
discussion_id: 20260709124052.680684-6-hjl.tools@gmail.com
source_type: public_inbox
title: '[PATCH 5/5] readelf: Consolidate get_[32|64]bit_dynamic_section'
headline: 'readelf: Consolidate get_[32|64]bit_dynamic_section'
tldr: Consolidates 32-bit and 64-bit dynamic section reading functions into a single
  function in readelf.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reduces code duplication by merging 32-bit and 64-bit parsing logic.
- Improves maintainability of the `readelf` tool.
exchanges: []
primer_expert: This is the final patch in a series aimed at refactoring `readelf`'s
  ELF section and program header parsing logic. It merges the separate 32-bit and
  64-bit functions for reading the dynamic section (`.dynamic`) into a unified `get_dynamic_section`
  function. This consolidation simplifies the codebase by removing redundant code
  and standardizing the reading of external dynamic tags using `BYTE_GET_SIZE`. The
  change directly addresses PR binutils/34356.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including dynamic
    section information.
- term: dynamic section
  definition: An ELF section (typically named .dynamic) that contains information
    needed for dynamic linking, such as symbol tables, relocation entries, and library
    dependencies.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: consolidation
  definition: The process of merging multiple functions or code blocks into a single,
    more efficient one.
- term: BYTE_GET_SIZE
  definition: A macro likely used to read a value of a specific size from a byte buffer
    and advance the buffer pointer.
series_id: 'binutils:readelf: consolidate get_[32|64]bit_dynamic_section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260709124052.680684-6-hjl.tools@gmail.com
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch consolidates the `get_32bit_dynamic_section` and `get_64bit_dynamic_section` functions in `readelf.c` into a single `get_dynamic_section` function. The new function is designed to handle both 32-bit and 64-bit ELF dynamic sections, using `BYTE_GET_SIZE` to retrieve external dynamic tags. This change aims to reduce code duplication and improve maintainability within the `readelf` utility, addressing PR binutils/34356.
