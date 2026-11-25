---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- PE
- import library
- Windows
discussion_id: SL2P216MB2271B106C6F5D71A6F5088A7EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH 3/3] ld: Add --short-implib for PE targets [PR34527]'
headline: 'ld: Add --short-implib for PE targets [PR34527]'
tldr: Introduces a `--short-implib` option for PE targets to create import libraries
  with concise member names.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds a new linker option and associated logic, increasing code complexity but providing
  a useful feature for PE target development.
exchanges:
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Submits the final patch in a series to introduce `--short-implib` for
    PE targets, enabling the generation of import libraries with abbreviated symbol
    names and ensuring deterministic output.
  quote: 'Add an option to write the import library given by --out-implib with short
    import members, using bfd_pe_write_short_import_library. Name the import symbols
    as make_one does: with --kill-at or a stdcall fixup the DLL exports the undecorated
    name, but callers refer to the decorated one.'
primer_expert: This patch, part of a series addressing PR binutils/34527, introduces
  the `--short-implib` option to the PE linker (`ld`). This option leverages `bfd_pe_write_short_import_library`
  to generate import libraries with abbreviated symbol names, improving efficiency
  and compatibility. The implementation ensures that symbol naming conventions (e.g.,
  handling `--kill-at` and stdcall decorations) are consistent with `dlltool`. It
  also makes the generated archive deterministic when `--no-insert-timestamp` is used.
  New tests are added to validate the functionality across various scenarios, including
  st…
primer_glossary:
- term: PE targets
  definition: Targets that produce files in the Portable Executable format, primarily
    used by Windows operating systems for executables and DLLs.
- term: import library
  definition: A special library file used by Windows linkers that contains information
    about exported functions and variables from a DLL. It allows programs to link
    against DLLs without directly referencing the DLL at compile time.
- term: short import members
  definition: Exported symbols within an import library that have been abbreviated
    or shortened, potentially for space or compatibility reasons.
- term: deterministic archive
  definition: An archive file (like a library) that will have the exact same content
    and layout each time it is generated from the same input, regardless of factors
    like timestamps or the order of operations.
- term: stdcall
  definition: A calling convention commonly used on Windows, where the callee cleans
    up the stack and arguments are pushed from right to left. It often involves name
    decoration (mangling).
series_id: 'binutils:ld: add --short-implib for pe targets [pr34527]'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB2271B106C6F5D71A6F5088A7EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch, the third in a series, adds the `--short-implib` option to the PE target linker. This option allows the creation of import libraries where the members (exported symbols) have shorter, more compact names. It ensures that these short import libraries are deterministic and compatible with existing tools like `dlltool`. New test cases are included to verify the functionality, including scenarios with decorated names and stdcall fixups.
