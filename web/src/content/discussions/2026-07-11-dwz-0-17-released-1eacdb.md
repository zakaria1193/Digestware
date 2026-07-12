---
project: gcc
subsystem: gcc
patch_id: null
tags:
- debugging
- DWARF
- optimization
- GCC
- binutils
discussion_id: 20260711201828.GF31804@gnu.wildebeest.org
source_type: public_inbox
title: DWZ 0.17 released
headline: DWZ 0.17 released
tldr: DWZ, a tool for optimizing DWARF debugging information, has released version
  0.17, adding support for compressed debug sections.
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased support for compressed input may add minor overhead during processing
  for uncompressed inputs.
- Improved size optimization for libraries and executables using DWARF debug information.
exchanges: []
primer_expert: DWZ (DWARF Optimization and Duplicate Removal tool) is a utility that
  processes DWARF debugging information within ELF binaries and shared libraries.
  It aims to reduce the size of debug sections by deduplicating information using
  DWARF v5's macro extension features (partial units and imported units). This release
  (0.17) adds support for input ELF files that use compressed debug sections (e.g.,
  zlib, zstd).
primer_glossary:
- term: DWZ
  definition: DWARF Optimization and Duplicate Removal tool. A utility that reduces
    the size of DWARF debugging information by identifying and consolidating duplicated
    data and optimizing its representation.
- term: DWARF
  definition: A standardized debugging data format used by many compilers and debuggers.
    It provides information about variables, types, functions, and source code locations.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: compilation unit (CU)
  definition: A logical unit of source code, typically a single source file, for which
    the compiler generates a distinct set of DWARF debugging information.
- term: DW_TAG_partial_unit
  definition: A DWARF debugging information entry type that represents a compilation
    unit containing only a subset of the debugging information, often used for deduplication.
- term: DW_TAG_imported_unit
  definition: A DWARF debugging information entry type that imports debugging information
    from another compilation unit, used in conjunction with DW_TAG_partial_unit for
    deduplication.
- term: compressed debug sections
  definition: ELF sections containing DWARF debugging information that have been compressed
    using algorithms like zlib or zstd to reduce file size. DWZ 0.17 can now process
    these.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260711201828.GF31804@gnu.wildebeest.org
bugzilla_url: null
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

Mark Wielaard announced the release of DWZ version 0.17. DWZ optimizes DWARF debugging information for size by replacing duplicated information with equivalent representations and using compilation units. This release adds support for handling compressed debug sections on input.
