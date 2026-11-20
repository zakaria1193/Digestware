---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- readelf
- memory leak
- elf
- security
discussion_id: loopr.15.aaazhygnwzem@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] binutils: avoid leaking section header pointers'
headline: 'binutils: avoid leaking section header pointers'
tldr: Fixes a memory leak in readelf when processing thin archives by allocating section
  header pointers only when needed.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The change adds a simple conditional check, with negligible performance impact.
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Fixes a memory leak in readelf by allocating section header pointers only
    when they are NULL.
  quote: 'ElfXX(_get_section_headers) allocates filedata->orig_section_headers on

    every non-probe call, so when it runs more than once for the same

    Filedata the earlier allocation is overwritten and lost.'
primer_expert: This PR fixes a memory leak in `readelf` related to thin archives.
  The `ElfXX(_get_section_headers)` function in `binutils/readelf-nn.c` incorrectly
  reallocates `filedata->orig_section_headers` even if it already holds a valid pointer,
  leading to a leak. The fix ensures this allocation only happens once when `filedata->orig_section_headers`
  is NULL.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including section
    headers, symbols, and relocation entries.
- term: thin archive
  definition: A type of archive file that contains only symbol table information and
    references to external object files, rather than the full object code.
- term: ELF
  definition: Executable and Linkable Format, a common standard for object file formats
    on Unix-like systems.
- term: ASan
  definition: AddressSanitizer, a fast memory error detector for C/C++ that finds
    issues like use-after-free and memory leaks.
- term: xcalloc
  definition: A memory allocation function that initializes allocated memory to zero.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.15.aaazhygnwzem@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch addresses a memory leak in the `readelf` utility that occurs when dumping thin archives. The `ElfXX(_get_section_headers)` function was allocating memory for section headers on every non-probe call, overwriting previous allocations and causing a leak. The fix ensures that `filedata->orig_section_headers` is only allocated if it is currently NULL, resolving the leak and passing an ASan-enabled test case.
