---
project: binutils
subsystem: readelf
patch_id: null
tags:
- binutils
- readelf
- elf
- security
- bugfix
discussion_id: CAO9RCZV_ftevjQsCV6F6yEVwBnSSUQ97M2xvE6OLnDKBxBULYQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH] readelf: fix SHT_GROUP, DT_RELR and string dump bounds'
headline: 'readelf: fix SHT_GROUP, DT_RELR and string dump bounds'
tldr: Addresses multiple bugs in readelf related to section group processing, DT_RELR
  relocation dumping, and string section boundary checks.
proposer: mustafa <mustafa@medios.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The changes involve adding more checks and using safer allocation functions, which
  may have a minor performance impact but significantly improve robustness and security.
exchanges:
- author: mustafa <mustafa@medios.digiscrypt.com>
  role: proposer
  position: 'Fixes three separate issues in readelf: section group processing bounds,
    DT_RELR relocation buffer overflows, and string dump boundary issues.'
  quote: Three separate problems in readelf, all reachable from a crafted file.
primer_expert: 'This PR tackles three vulnerabilities/bugs in `readelf`: 1) `process_section_groups`
  is fixed to handle zero `sh_entsize` and small `sh_size` values correctly, preventing
  division-by-zero and incorrect member counts. 2) Heap buffer overflows in `process_relocs`
  when dumping `DT_RELR` relocations after other relocation types are fixed by ensuring
  proper buffer allocation with `xcmalloc` and `xcrealloc`. 3) `dump_section_as_strings`
  is corrected to prevent reading past buffer bounds, especially for decompressed
  sections, by properly bounding `maxlen`.'
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including section
    headers, symbols, and relocation entries.
- term: SHT_GROUP
  definition: A section header type indicating a section containing group of symbols.
- term: DT_RELR
  definition: A dynamic tag in the ELF header that indicates a table of relative relocations.
- term: ELF
  definition: Executable and Linkable Format, a common standard for object file formats
    on Unix-like systems.
- term: heap buffer overflow
  definition: A type of security vulnerability where a program writes data beyond
    the allocated buffer in the heap, potentially corrupting other data or executing
    malicious code.
- term: xcmalloc
  definition: A memory allocation function that checks for allocation errors.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAO9RCZV_ftevjQsCV6F6yEVwBnSSUQ97M2xvE6OLnDKBxBULYQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch corrects three distinct issues in the `readelf` utility: 1) It prevents division by zero and out-of-bounds reads when processing `SHT_GROUP` sections by adding checks for `sh_entsize` and `sh_size`. 2) It resolves a heap buffer overflow when dumping `DT_RELR` relocations by ensuring proper buffer sizing and allocation. 3) It fixes an issue where `dump_section_as_strings` could read past the end of a buffer by adding boundary checks.
