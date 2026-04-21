---
project: binutils
subsystem: gdb/sparc
patch_id: null
tags:
- gdb
- sparc
- elf32
- core dump
- bfd
discussion_id: c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
source_type: public_inbox
title: 'Re: [PATCH] gdb/sparc: implement PRSTATUS elf32-sparc handler'
headline: 'gdb/sparc: Implement PRSTATUS elf32-sparc handler'
tldr: This patch adds a handler to GDB for parsing PRSTATUS notes in SPARC ELF32 core
  dumps, allowing for correct viewing of core dumps.
stakes: Ensures proper handling of SPARC core dumps in GDB, improving debugging for
  SPARC-based systems.
proposer: Simon Marchi <simark@simark.ca>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the BFD library.
- Increases the size of the BFD library.
- May require updates if the PRSTATUS note format changes in the future.
exchanges:
- author: Simon Marchi <simark@simark.ca>
  role: proposer
  position: Requests review of the patch, as it targets code in the `bfd` library.
  quote: Adding binutils@sourceware.org, since this targets code in "bfd". Can someone
    from binutils review this?
primer_expert: This patch modifies `bfd/elf32-sparc.c` to add a handler for `PRSTATUS`
  notes in ELF32 SPARC core dumps.  These notes contain process status information,
  including signal, PID, and register data.  The patch adds `elf32_sparc_grok_prstatus`
  to parse these notes and create a `.reg` section, allowing GDB to access the register
  data. This is architecture-specific code within the BFD library used by both GDB
  and binutils.
primer_general: The Binary File Descriptor (BFD) library is a part of binutils that
  provides a generic interface for manipulating different object file formats.  It
  allows tools like GDB and objdump to work with various architectures and file formats
  without needing to know the specifics of each one.  This patch modifies the BFD
  library to correctly interpret core dumps produced by SPARC systems running a 32-bit
  ELF operating system. Core dumps contain the state of a program at the point of
  failure, and this change allows GDB to accurately display that state, by correctly
  parsing the `PRSTATUS` note.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c0910b51-6808-4b72-8b77-f7dcc54eae3b@simark.ca
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces a new function, `elf32_sparc_grok_prstatus`, to handle PRSTATUS notes found in SPARC ELF32 core dumps. The handler extracts information such as signal, PID, and registers from the note, creates a `.reg` section with the register data, and allows GDB to display core dumps correctly.
