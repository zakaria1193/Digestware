---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- arm
- elf
- linking
- cleanup
- bfd
commit_hash: b4b3d0c060dbfc622331a85c6059ef1531d335c2
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Remove dead code in arm check_relocs function
tldr: Dead code checking for zero symbol count has been removed from the ARM ELF relocations
  checker.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `elf32_arm_check_relocs` function in `elf32-arm.c` is part of BFD's
  ELF backend for the ARM architecture. It was responsible for validating relocations.
  The commit removes a check for `nsyms > 0`, where `nsyms` is derived from `NUM_SHDR_ENTRIES
  (symtab_hdr)`. This check became obsolete after changes elsewhere in BFD that ensure
  object files with relocations must have a valid `.symtab` section. The code path
  it guarded was effectively unreachable.
primer_glossary:
- term: .symtab
  definition: The symbol table section in an ELF file. It contains information about
    symbols (functions, variables) defined in the object file.
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
url: https://inbox.sourceware.org/binutils-cvs/20261028223645.580754BA2E23@sourceware.org
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

The `elf32_arm_check_relocs` function in BFD's ARM ELF support contained dead code that checked for a zero symbol count. This check is now unnecessary because object files with relocations but lacking a proper symbol table are rejected earlier in the linking process. The removal simplifies the function and improves clarity.
