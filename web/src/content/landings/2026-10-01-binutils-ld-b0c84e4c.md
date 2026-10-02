---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- risc-v
- elf
- linker
- PIC
commit_hash: b0c84e4cd5dae13d186b6099c080137d250a986a
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: 'RISC-V: Add DT_RELR support for position-independent code'
tldr: RISC-V now supports DT_RELR for efficient handling of position-independent code
  relocations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch brings `DT_RELR` support to RISC-V ELF, enabling the linker
  to generate RELR-based dynamic executables and shared objects. It introduces the
  `DT_RELR` dynamic tag and updates `bfd/elfnn-riscv.c` to handle `relr-relocs.ld`
  and associated special symbols like mapping symbols and `__DATA_BEGIN__`. `binutils/readelf.c`
  is updated to display these relocations, and `ld/emulparams/elf32lriscv-defs.sh`
  is modified to enable `DT_RELR` only for Linux. Test cases for RELR relocations
  and relaxation are also added. This is crucial for efficient PIC on RISC-V.
primer_glossary:
- term: DT_RELR
  definition: A dynamic tag in an ELF file that indicates the presence of RELR (relative
    relocations) in the dynamic section. RELR is a more compact format for relocations
    used in position-independent code.
- term: Position-Independent Code (PIC)
  definition: Code that can be loaded and executed at any memory address without modification.
    It's essential for shared libraries and modern executable security.
- term: Relocation
  definition: Information in an object file that describes how to modify code or data
    after it has been linked, typically to resolve addresses or symbol references.
- term: ELF
  definition: Executable and Linkable Format. A common file format for object files,
    executables, and shared libraries on Unix-like systems.
- term: DT_RELR
  definition: A dynamic tag in an ELF file that indicates the presence of RELR (relative
    relocations) in the dynamic section. RELR is a more compact format for relocations
    used in position-independent code.
- term: Dynamic Section
  definition: A section within an ELF file that contains information required by the
    dynamic linker, such as the shared libraries the program depends on and relocation
    information.
- term: readelf
  definition: A utility that displays information about ELF files, including headers,
    sections, and symbols.
- term: linker
  definition: A program that combines object files and libraries into an executable
    or library, resolving symbol references and performing relocations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261001084709.3F6E24B99F77@sourceware.org
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

This commit introduces support for `DT_RELR` in the RISC-V ELF toolchain, enhancing the handling of position-independent code (PIC). It includes modifications to the assembler, linker, and readelf utility to correctly process and display these relocations, mirroring implementations from AArch64 and LoongArch.
