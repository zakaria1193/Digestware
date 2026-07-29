---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- binutils
- elf
- refactoring
- code readability
discussion_id: b76972ea-76da-4e40-ae59-2d6342f4cde1@suse.com
source_type: public_inbox
title: '[PATCH RFC 5/5] readelf: move code around'
headline: 'readelf: Code rearrangement for readability'
tldr: Refactors readelf.c to reduce `#ifdef` complexity and potentially improve code
  structure.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Code rearrangement can improve readability but may introduce regressions if not
  done carefully.
- Reducing `#ifdef` complexity is desirable but can be challenging in codebases with
  multiple format variants.
exchanges: []
primer_expert: The `readelf.c` source file handles the parsing and display of ELF
  (Executable and Linkable Format) file information. Due to the differences between
  32-bit and 64-bit ELF formats, extensive use of `#ifdef` directives is often necessary
  to conditionally compile code paths. This patch aims to consolidate some of this
  conditional logic by restructuring the code, particularly around the functions responsible
  for reading program headers and section headers. The intent is to make the code
  cleaner without fundamentally altering its behavior or introducing new features.
primer_glossary:
- term: readelf
  definition: A utility in GNU Binutils that displays information about ELF files
    (e.g., section headers, program headers, symbols).
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and core dumps on Unix-like systems.
- term: '`#ifdef`'
  definition: A C preprocessor directive used for conditional compilation, allowing
    different code blocks to be included based on defined macros.
- term: program headers
  definition: Structures within an ELF file that describe how the operating system
    should load segments of the executable into memory.
- term: section headers
  definition: Structures within an ELF file that describe each section (e.g., code,
    data, symbols) in the object file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/b76972ea-76da-4e40-ae59-2d6342f4cde1@suse.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch attempts to reduce the amount of conditional compilation (`#ifdef`) in `binutils/readelf.c` by rearranging code. The goal is to improve readability and maintainability, though the author notes that a more extensive change like using function pointers for header reading was considered but deemed too complex to yield significant overall benefit.
