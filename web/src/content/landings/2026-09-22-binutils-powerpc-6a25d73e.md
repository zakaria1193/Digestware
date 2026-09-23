---
project: binutils
subsystem: binutils/powerpc
patch_id: null
tags:
- binutils
- PowerPC
- core dump
- ELF
- new feature
commit_hash: 6a25d73ee2ab48ad66fbd2ab8f5584b2a30c70dd
source_type: public_inbox
author: Abhay Kandpal <abhay@sourceware.org>
headline: 'PowerPC: Add NT_PPC_DMR core file support'
tldr: Adds support for the new NT_PPC_DMR note type in BFD and readelf for PowerPC
  core files.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change adds BFD and `readelf` support for the `NT_PPC_DMR` note
  type, defined in `include/elf/common.h`. New functions `elfcore_grok_ppc_dmr` and
  `elfcore_write_ppc_dmr` are added to `bfd/elf.c` to handle reading and writing these
  notes. The `readelf.c` utility is updated to recognize and display this new note
  type. GDB support is planned as a follow-up.
primer_glossary:
- term: PowerPC
  definition: A family of RISC instruction set architectures developed by Apple, IBM,
    and Motorola. Used in various devices, including older Apple Macintosh computers
    and servers.
- term: NT_PPC_DMR
  definition: A specific note type within the ELF (Executable and Linkable Format)
    standard, used in core dump files. This particular type, NT_PPC_DMR, is designated
    for storing the Dense Math Registers (DMR) of a PowerPC processor.
- term: core file
  definition: A file produced by a Unix-like operating system when a program crashes.
    It contains a snapshot of the program's memory state at the time of the crash,
    used for debugging.
- term: BFD
  definition: Binary File Descriptor library. A GNU library that provides a common
    interface for reading and writing various executable file formats.
- term: readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files, including sections, symbols, and notes.
- term: Dense Math Registers (DMR)
  definition: A set of eight 1024-bit registers introduced by the Dense Math facility
    in a future Power ISA revision, designed for high-performance mathematical operations.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executable,
    object code, shared libraries, and core dumps on Unix-like systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260922095320.50BE24BA5433@sourceware.org
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This commit introduces support for the `NT_PPC_DMR` note type in the Binary File Descriptor (BFD) library and the `readelf` utility. This new note type is intended to carry the contents of the Dense Math Registers (DMR), which will be available on a future PowerPC processor. This lays the groundwork for handling core dumps from systems using this new register set.
