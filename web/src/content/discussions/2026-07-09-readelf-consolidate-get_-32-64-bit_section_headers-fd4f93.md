---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- elf
- section headers
- refactoring
- code consolidation
discussion_id: 20260709124052.680684-2-hjl.tools@gmail.com
source_type: public_inbox
title: '[PATCH 1/5] readelf: Consolidate get_[32|64]bit_section_headers'
headline: 'readelf: Consolidate get_[32|64]bit_section_headers'
tldr: Consolidates 32-bit and 64-bit section header reading functions into one in
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
primer_expert: This is the first patch in a series to refactor `readelf`'s ELF file
  parsing. It merges the distinct functions for reading 32-bit and 64-bit ELF section
  headers (`get_32bit_section_headers` and `get_64bit_section_headers`) into a single
  `get_section_headers` function. This generalized function uses the `BYTE_GET_SIZE`
  macro to read header fields from the external ELF file, providing a unified approach
  and eliminating redundant code. This change is part of the effort to address PR
  binutils/34356.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including section
    header details.
- term: section headers
  definition: Data structures within an ELF file that describe each section, such
    as its name, type, size, and memory address.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: consolidation
  definition: The process of merging multiple functions or code blocks into a single,
    more efficient one.
- term: BYTE_GET_SIZE
  definition: A macro likely used to read a value of a specific size from a byte buffer
    and advance the buffer pointer.
series_id: 'binutils:readelf: consolidate get_[32|64]bit_section_headers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260709124052.680684-2-hjl.tools@gmail.com
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch consolidates the `get_32bit_section_headers` and `get_64bit_section_headers` functions in `readelf.c` into a single `get_section_headers` function. The new function handles both 32-bit and 64-bit ELF section headers, utilizing the `BYTE_GET_SIZE` macro for reading external ELF section header fields. This consolidation aims to reduce code duplication and enhance maintainability within the `readelf` utility, addressing PR binutils/34356.
