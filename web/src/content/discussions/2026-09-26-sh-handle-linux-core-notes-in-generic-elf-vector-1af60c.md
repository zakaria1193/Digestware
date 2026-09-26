---
project: binutils
subsystem: sh
patch_id: null
tags:
- binutils
- sh
- core dump
- debugging
- elf
discussion_id: 20260926041603.736177-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH] sh: handle Linux core notes in the generic ELF vector'
headline: 'sh: Handle Linux core notes in generic ELF vector'
tldr: Patch modifies the SH ELF backend to correctly handle Linux core notes, fixing
  an issue where GDB could not find registers in core dumps.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The SH ELF backend in binutils was incorrectly prioritizing a generic
  ELF format over the Linux-specific one for core dumps. This patch changes the `bfd_check_format_matches`
  logic to ensure the Linux-specific notes (NT_PRSTATUS, NT_PRPSINFO) are processed,
  which are necessary for GDB to reconstruct register information in core dumps. Previously,
  `elf32-shl` was picked, which didn't handle these notes.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: Core file
  definition: A file that contains a memory image of a process at the time it terminated
    abnormally (crashed). It's used for debugging.
- term: NT_PRSTATUS
  definition: A note type in ELF core files that contains process status information,
    including register values.
- term: NT_PRPSINFO
  definition: A note type in ELF core files that contains process information, such
    as process ID, command name, and user/group IDs.
- term: Registers
  definition: Small, fast storage locations within a CPU that hold data currently
    being processed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260926041603.736177-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-26'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the SH ELF backend where the generic ELF vector was not properly handling Linux-specific core notes like NT_PRSTATUS and NT_PRPSINFO. This resulted in core files lacking a .reg section, preventing GDB from displaying registers. The fix ensures these notes are handled in the generic vector, which is inherited by the Linux vector.
