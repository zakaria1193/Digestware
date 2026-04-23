---
project: binutils
subsystem: gdb/sparc
patch_id: null
tags:
- gdb
- sparc
- core dump
- PRSTATUS
- bfd
discussion_id: c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
source_type: public_inbox
title: 'Re: [PATCH] gdb/sparc: implement PRSTATUS elf32-sparc handler'
headline: Requests review for SPARC PRSTATUS handling in GDB
tldr: A patch implementing PRSTATUS handling for SPARC ELF32 core dumps needs review
  from binutils experts.
stakes: Enables correct viewing of SPARC ELF32 core dumps in GDB by implementing parsing
  of the PRSTATUS note, improving debugging capabilities for this architecture.
proposer: Simon Marchi <simark@simark.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in `bfd/elf32-sparc.c` to handle PRSTATUS notes.
- Potential for errors in parsing PRSTATUS notes if the format is not as expected.
- Reliance on the correctness of the PRSTATUS note format in core dumps.
exchanges:
- author: Simon Marchi
  role: other
  position: Requests a review from binutils experts for a patch implementing PRSTATUS
    handling for SPARC ELF32 core dumps in GDB.
  quote: 'Adding binutils@sourceware.org, since this targets code in "bfd".


    Can someone from binutils review this?'
primer_expert: This patch adds a handler for PRSTATUS notes within the `bfd/elf32-sparc.c`
  file. PRSTATUS notes contain information about the process status at the time of
  a core dump, including signal information, process ID, and register values. The
  patch implements the `elf32_sparc_grok_prstatus` function to parse these notes and
  extract relevant data for GDB. The code modifies the BFD (Binary File Descriptor)
  library, which provides a generic interface for accessing different object file
  formats.
primer_general: When a program crashes, it can create a 'core dump,' which is a snapshot
  of the program's memory and state at the time of the crash. This allows developers
  to debug the program and understand what went wrong. Core dumps often contain notes
  with extra information about the process. This patch adds support for reading a
  specific type of note (PRSTATUS) in core dumps created on SPARC processors. This
  allows the GDB debugger to display the process's status, signal, and registers,
  aiding in debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
bugzilla_url: null
date: '2026-04-20'
---

Simon Marchi is requesting a review from the binutils team for a patch that implements PRSTATUS note handling for SPARC ELF32 core dumps in GDB. The patch adds code to `bfd/elf32-sparc.c` to parse PRSTATUS notes, which are currently unparsed, leading to incorrectly viewed core dumps.
