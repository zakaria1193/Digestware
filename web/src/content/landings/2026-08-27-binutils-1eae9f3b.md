---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bugfix
- dwarf
- debugging
- readelf
commit_hash: 1eae9f3bb7eae31d1fbc5663dae13973a52da61a
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Remove arbitrary size limit for decompressed DWO sections
tldr: Binutils readelf no longer imposes an arbitrary limit on decompressed DWO section
  sizes.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Removes the sanity check in `bfd_section_size_insane` that limited
  compressed sections to 10x their file size, and the corresponding size limit in
  `readelf.c`'s `uncompress_section_contents`. This resolves PRs 26946, 28834, and
  34481 by allowing readelf to correctly handle very large decompressed DWO sections,
  such as those generated from code with extremely long string literals.
primer_glossary:
- term: DWO files
  definition: Debug With Other files. These files contain split DWARF debugging information,
    allowing for more modular debugging data. They are typically generated alongside
    object files.
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files. It can show various sections, symbols, and debugging information,
    including DWARF data.
- term: BFD
  definition: The Binary File Descriptor library, a low-level API for reading and
    writing various binary file formats used by GNU Binutils.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about source code variables, types, and structure.
discussion_id_link: public_inbox:binutils#34481
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260827132254.B2DBB4BA79B9@sourceware.org
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This commit removes the arbitrary limit on the uncompressed size of DWO sections in `binutils/readelf.c` and the sanity check for compressed sections in `bfd/section.c`. This addresses issues where excessively large, but valid, decompressed debug strings in DWO files would exceed the previous ten times file size limit, preventing proper processing.
