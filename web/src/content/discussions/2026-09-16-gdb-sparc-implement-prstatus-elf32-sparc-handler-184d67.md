---
project: binutils
subsystem: gdb/sparc
patch_id: null
tags:
- GDB
- SPARC
- ELF
- core dump
- debugging
discussion_id: 874ifpdvuy.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH RESEND] gdb/sparc: implement PRSTATUS elf32-sparc handler'
headline: 'gdb/sparc: implement PRSTATUS elf32-sparc handler'
tldr: Adds a handler for SPARC ELF32 PRSTATUS notes in GDB to correctly parse core
  dumps.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves core dump analysis for SPARC ELF32 on GDB.
- Adds specific handling for a particular NOTE type, increasing code complexity.
exchanges:
- author: Jose E. Marchesi
  role: proposer
  position: Approves the patch for implementing the PRSTATUS handler for SPARC ELF32
    core dumps.
  quote: FWIW this looks good to me.
- author: Jakub Klimek
  role: contributor
  position: 'Explains the problem: unparsed PRSTATUS notes in SPARC ELF32 core dumps
    lead to incorrect coredump views.'
  quote: 'Some SPARC ELF32 coredumps emit a PRSTATUS note which is left unparsed

    without a handler in GDB, leading to incorrectly viewed coredumps.'
primer_expert: This patch adds the `elf32_sparc_grok_prstatus` function to `bfd/elf32-sparc.c`.
  This function handles the PRSTATUS note type, which is part of the ELF core dump
  format for SPARC 32-bit systems. It parses specific fields like `pr_cursig` and
  `pr_pid` and uses `_bfd_elfcore_make_pseudosection` to create a section for register
  data, addressing a gap in GDB's core dump parsing for this architecture.
primer_glossary:
- term: SPARC
  definition: A RISC instruction set architecture originally developed by Sun Microsystems.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: core dump
  definition: A file that records the memory image of a crashed process. Debuggers
    can use core dumps to inspect the state of the program at the time of the crash.
- term: PRSTATUS
  definition: A specific NOTE type in ELF core dumps that contains process status
    information, including signal, PID, and register values.
- term: bfd
  definition: Binary File Descriptor library, part of binutils, which provides a generic
    interface to object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/874ifpdvuy.fsf@gnu.org
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This patch introduces a handler in GDB for the PRSTATUS NOTE section found in SPARC ELF32 core dumps. Previously, these notes were unparsed, leading to incorrect core dump analysis. The new handler extracts signal and process ID information, and defines a pseudo-section for register data, improving core dump interpretation for this architecture.
