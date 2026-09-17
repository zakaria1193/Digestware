---
project: binutils
subsystem: gdb/sparc
patch_id: null
tags:
- gdb
- binutils
- sparc
- coredump
- elf
discussion_id: 20260916151415.386814-1-michal.lach@phoenix-rtos.com
source_type: public_inbox
title: '[PATCH RESEND] gdb/sparc: implement PRSTATUS elf32-sparc handler'
headline: 'gdb/sparc: implement PRSTATUS elf32-sparc handler'
tldr: Patch adds a handler for the PRSTATUS note in SPARC ELF32 coredumps to GDB.
proposer: Michal Lach <michal.lach@phoenix-rtos.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves GDB's ability to interpret SPARC ELF32 coredumps by adding specific parsing
  logic, with minimal impact on other architectures.
exchanges:
- author: Michal Lach <michal.lach@phoenix-rtos.com>
  role: proposer
  position: Submits a patch to add a handler for the PRSTATUS note in SPARC ELF32
    coredumps to GDB, resolving issues with unparsed notes.
  quote: 'Some SPARC ELF32 coredumps emit a PRSTATUS note which is left unparsed

    without a handler in GDB, leading to incorrectly viewed coredumps.'
- author: Jakub Klimek <jakub.klimek@phoenix-rtos.com>
  role: contributor
  position: Original author of the patch, providing context that unparsed PRSTATUS
    notes in SPARC ELF32 coredumps lead to incorrect interpretations in GDB.
  quote: null
primer_expert: This patch targets the GDB debugger and the BFD library's handling
  of SPARC ELF32 core dumps. Specifically, it adds a new backend handler (`elf32_sparc_grok_prstatus`)
  to parse the `PRSTATUS` ELF note. This note contains process status information,
  including signal and process ID, which GDB previously failed to interpret correctly,
  leading to corrupted core dump views.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, used by GNU Binutils and GDB to provide
    a common interface to various object file formats.
- term: SPARC
  definition: A RISC instruction set architecture developed by Sun Microsystems.
- term: ELF32
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and core dumps on Unix-like systems, in its 32-bit variant.
- term: coredump
  definition: A file containing the memory image of a process at the time it crashed,
    used for debugging.
- term: PRSTATUS note
  definition: An ELF note type found in core dumps that contains process status information,
    such as the signal that caused the dump and the process ID.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260916151415.386814-1-michal.lach@phoenix-rtos.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This patch resend addresses an issue in GDB where SPARC ELF32 coredumps contain unparsed PRSTATUS notes, leading to incorrect core dump interpretations. It introduces a handler for the PRSTATUS note within the BFD library's elf32-sparc.c file, enabling GDB to correctly parse these notes and improve core dump analysis.
