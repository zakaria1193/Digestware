---
project: binutils
subsystem: gprof
patch_id: null
tags:
- binutils
- gprof
- debug
- DWARF
- compression
discussion_id: 20261116181535.95867-1-guanli.oerv@isrc.iscas.ac.cn
source_type: public_inbox
title: '[PATCH] gprof: Enable decompression before checking separate debug files'
headline: 'gprof: Enable decompression before checking separate debug files'
tldr: Patch enables DWARF decompression in gprof before reading section headers, fixing
  incorrect source line reporting with compressed separate debug files.
proposer: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Li Guan
  role: proposer
  position: Submits a patch to fix incorrect source line reporting in gprof when using
    compressed DWARF debug files.
  quote: Set BFD_DECOMPRESS before bfd_check_format(), as core_init() already does
    for the main executable, so the separate debug file is opened with the same section
    decompression behavior.
primer_expert: This patch modifies the `gprof` tool's handling of core files, specifically
  when dealing with separate debug information that uses DWARF compression. The issue
  arises because the BFD library's `bfd_check_format()` function, called during the
  processing of separate debug files, does not have decompression enabled by default.
  This leads to incorrect interpretation of section headers when DWARF is compressed,
  resulting in lost source location information. The patch preemptively sets the `BFD_DECOMPRESS`
  flag on the debug BFD object, ensuring proper decompression and accurate source
  mapping, mirr…
primer_glossary:
- term: gprof
  definition: A Unix performance analysis tool that generates call graph profiles
    of a program.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about source code, types, and variables.
- term: compressed DWARF
  definition: DWARF debugging information that has been compressed using algorithms
    like zlib to reduce file size.
- term: separate debug files
  definition: Debug information that is stored in separate files from the executable,
    allowing for smaller executables and easier management of debug data.
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to read and write various executable file formats.
- term: BFD_DECOMPRESS
  definition: A flag within the BFD library that indicates whether compressed sections
    should be automatically decompressed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116181535.95867-1-guanli.oerv@isrc.iscas.ac.cn
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in gprof where compressed DWARF debug information in separate files causes incorrect source line reporting, showing "<unknown>:0" instead of the expected file and line numbers. The fix involves enabling the BFD_DECOMPRESS flag before BFD reads section headers, ensuring that compressed sections are handled correctly, similar to how the main executable is processed.
