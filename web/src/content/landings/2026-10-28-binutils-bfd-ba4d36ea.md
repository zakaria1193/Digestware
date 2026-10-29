---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- elf
- cleanup
- bfd
- moxie
- msp430
commit_hash: ba4d36ea5aabeaf1ca5507b01b468146dd647370
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Remove unused check_relocs functions for Moxie, MSP430, and MT architectures
tldr: Unused `check_relocs` functions for Moxie, MSP430, and MT ELF backends have
  been removed.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ELF backends for Moxie, MSP430, and MT architectures in BFD included
  `elf_backend_check_relocs` entries that pointed to `moxie_elf_check_relocs`, `elf32_msp430_check_relocs`,
  and `mt_elf_check_relocs`, respectively. These functions themselves were empty stubs.
  This commit removes these empty functions and the corresponding `elf_backend_check_relocs`
  definitions, cleaning up unused code in `elf32-moxie.c`, `elf32-msp430.c`, and `elf32-mt.c`.
primer_glossary:
- term: check_relocs
  definition: A function within BFD's ELF backend responsible for validating relocation
    entries in an object file during the linking process.
- term: relocations
  definition: Information in an object file that describes how to modify certain addresses
    or symbols when linking. For example, a relocation entry might indicate that a
    specific address needs to be updated with the actual address of a function.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a generic interface for reading and writing various binary file formats, including
    ELF.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223624.77A214BA23D0@sourceware.org
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

The `check_relocs` functions for the Moxie, MSP430, and MT ELF backends in BFD have been removed as they contained no functional code. These functions were declared but did not implement any specific logic for checking relocations, making them dead code. Their removal simplifies the BFD codebase by eliminating unnecessary function definitions.
