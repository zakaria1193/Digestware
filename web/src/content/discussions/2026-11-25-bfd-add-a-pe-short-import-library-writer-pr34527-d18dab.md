---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- PE/COFF
- import library
discussion_id: SL2P216MB2271B16D2A7B1A18D366EFB4EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH 1/3] bfd: Add a PE short import library writer [PR34527]'
headline: 'bfd: Add a PE short import library writer [PR34527]'
tldr: Adds a new BFD function to create compact PE/COFF short import libraries.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds a new, complex function to BFD, increasing maintenance burden.
- Initial implementation only supports i386 and x86-64, requiring future work for
  broader architecture support.
exchanges: []
primer_expert: Adds `bfd_pe_write_short_import_library` to BFD's PE/COFF support.
  This function generates import libraries using a compact format where each export
  has a short record on disk. It leverages existing archive map code for symbol indexing
  and includes necessary objects for import descriptors, DLL names, and thunks. Support
  is currently limited to i386 and x86-64, with a design allowing for future expansion
  to other architectures like aarch64.
primer_glossary:
- term: BFcache
  definition: A library within binutils that provides an abstraction for reading and
    writing object file formats.
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the standard file format
    for executables, object code, and DLLs in 32-bit and 64-bit Windows operating
    systems.
- term: Import library
  definition: A library that contains information about functions and variables exported
    by a DLL. It allows programs to link against DLLs without explicitly calling loading
    functions.
- term: GNU ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
series_id: 'binutils:bfd: add a pe short import library writer [pr34527]'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB2271B16D2A7B1A18D366EFB4EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch introduces a new function to the BFD library that can write PE/COFF short import libraries. These libraries are more compact than the traditional format and are compatible with tools like GNU ld, MSVC lib, and llvm-dlltool. This functionality is crucial for improving the efficiency of import library generation within the GNU toolchain.
