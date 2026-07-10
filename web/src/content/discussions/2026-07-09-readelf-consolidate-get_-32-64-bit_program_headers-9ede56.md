---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- elf
- program headers
- refactoring
- code consolidation
discussion_id: 20260709124052.680684-4-hjl.tools@gmail.com
source_type: public_inbox
title: '[PATCH 3/5] readelf: Consolidate get_[32|64]bit_program_headers'
headline: 'readelf: Consolidate get_[32|64]bit_program_headers'
tldr: Consolidates 32-bit and 64-bit program header reading functions into one in
  readelf.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reduces code duplication by merging 32-bit and 64-bit parsing logic.
- Improves maintainability of the `readelf` tool.
exchanges: []
primer_expert: This patch continues the refactoring of `readelf`'s ELF parsing by
  merging the separate implementations for reading 32-bit and 64-bit program headers
  (`get_32bit_program_headers` and `get_64bit_program_headers`) into a single, unified
  `get_program_headers` function. This generalized function leverages the `BYTE_GET_SIZE`
  macro for reading fields from the external ELF file, thereby reducing code redundancy
  and simplifying the parsing logic for program headers. This change is part of the
  ongoing effort to address PR binutils/34356.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including program
    header details.
- term: program headers
  definition: Data structures within an ELF file that describe segments of the file,
    such as code, data, and stack, and how they should be mapped into memory.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: consolidation
  definition: The process of merging multiple functions or code blocks into a single,
    more efficient one.
- term: BYTE_GET_SIZE
  definition: A macro likely used to read a value of a specific size from a byte buffer
    and advance the buffer pointer.
series_id: 'binutils:readelf: consolidate get_[32|64]bit_program_headers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260709124052.680684-4-hjl.tools@gmail.com
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch consolidates the `get_32bit_program_headers` and `get_64bit_program_headers` functions in `readelf.c` into a single `get_program_headers` function. The new function efficiently handles both 32-bit and 64-bit ELF program headers, using the `BYTE_GET_SIZE` macro for reading external ELF program header fields. This consolidation aims to eliminate code duplication and enhance the maintainability of the `readelf` utility, addressing PR binutils/34356.
