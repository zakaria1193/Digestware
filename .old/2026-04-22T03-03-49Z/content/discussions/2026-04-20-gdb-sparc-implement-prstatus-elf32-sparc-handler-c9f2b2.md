---
project: binutils
subsystem: gdb/sparc
patch_id: null
tags:
- gdb
- sparc
- elf32
- core dump
- PRSTATUS
discussion_id: c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
source_type: public_inbox
title: 'Re: [PATCH] gdb/sparc: implement PRSTATUS elf32-sparc handler'
headline: 'gdb/sparc: Implement PRSTATUS elf32-sparc handler'
tldr: This patch adds a handler in GDB for parsing PRSTATUS notes in SPARC ELF32 core
  dumps, enabling correct display of core dump information.
stakes: Without this patch, SPARC ELF32 core dumps may not be displayed correctly
  in GDB, hindering debugging efforts.
proposer: Simon Marchi <simark@simark.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the BFD library.
- Increases the size of the GDB binary.
- May introduce new bugs in core dump handling.
exchanges:
- author: Simon Marchi <simark@simark.ca>
  role: proposer
  position: Asks for a review of the patch, noting that it targets code in the "bfd"
    directory.
  quote: 'Adding binutils@sourceware.org, since this targets code in "bfd".


    Can someone from binutils review this?'
primer_expert: This patch modifies `bfd/elf32-sparc.c` to handle PRSTATUS notes, which
  are part of the ELF core dump format.  These notes contain process status information.  The
  code adds a function `elf32_sparc_grok_prstatus` to parse the note and create a
  ".reg/999" section in the BFD.  This allows GDB to access and display the process
  status information from the core dump.
primer_general: Core dumps are snapshots of a program's memory and registers at the
  time of a crash, used for debugging.  They are often stored in the ELF format, which
  can include notes containing additional information.  This patch addresses an issue
  where GDB, the GNU Debugger, cannot properly interpret a specific type of note (PRSTATUS)
  found in core dumps generated on SPARC ELF32 systems.  The PRSTATUS note contains
  information about the process's status at the time of the crash, such as signal
  number, process ID, and register values.  By adding a handler for this note type,
  the patch enables GDB to correctly display this information, making debugging easier.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
bugzilla_url: null
date: '2026-04-20'
---

This patch implements a handler for PRSTATUS notes in SPARC ELF32 core dumps.  The lack of such a handler causes GDB to display core dumps incorrectly. The patch adds the `elf32_sparc_grok_prstatus` function to parse the PRSTATUS note and create a ".reg/999" section.
