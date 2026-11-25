---
project: binutils
subsystem: pe
patch_id: null
tags:
- binutils
- PE/COFF
- import library
- dlltool
- ld
discussion_id: SL2P216MB2271BDA5D093BF89CCC67E2AEF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH 0/3] PE: Add --short-implib to dlltool and ld [PR34527]'
headline: 'PE: Add --short-implib to dlltool and ld [PR34527]'
tldr: Introduces --short-implib option to dlltool and ld for generating compact PE/COFF
  import libraries.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the complexity of dlltool and ld by adding a new feature.
- The new format is not a complete replacement, maintaining compatibility with the
  old format.
exchanges: []
primer_expert: This is a three-part series that adds support for generating PE/COFF
  short import libraries. Patch 1/3 adds a shared BFD writer (`bfd_pe_write_short_import_library`),
  patch 2/3 integrates this writer into `dlltool` as the `--short-implib` option,
  and patch 3/3 does the same for `ld` (`--out-implib`). The default import library
  format remains unchanged. The generated libraries are compatible with MSVC and LLVM,
  and tests cover linking and deterministic output verification.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the standard file format
    for executables, object code, and DLLs in 32-bit and 64-bit Windows operating
    systems.
- term: dlltool
  definition: A GNU binutils utility that creates DLL import libraries, or extracts
    information from them.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: Import library
  definition: A library that contains information about functions and variables exported
    by a DLL. It allows programs to link against DLLs without explicitly calling loading
    functions.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for reading and writing various object file formats.
series_id: 'binutils:pe: add --short-implib to dlltool and ld [pr34527]'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB2271BDA5D093BF89CCC67E2AEF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This series introduces the capability to create PE/COFF short import libraries using the --short-implib option in both dlltool and ld. GNU ld already supports reading these libraries, and this series adds the generation side. The new format is more compact and has been verified for compatibility with MSVC and LLVM. This significantly improves the GNU toolchain's ability to produce efficient import libraries.
