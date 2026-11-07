---
project: binutils
subsystem: mips
patch_id: null
tags:
- mips
- binutils
- bfd
- dwarf
- debugging
discussion_id: alpine.DEB.2.21.2611050419141.6502@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH 3 11/16] MIPS: Fix line info in compressed MIPS function'
headline: 'MIPS: Fix line info in compressed MIPS function'
tldr: Discussion on a patch that improves DWARF line number information for MIPS compressed
  functions.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a second lookup attempt for line information, which could slightly increase
  debugging lookup time in specific MIPS compressed function scenarios.
exchanges:
- author: Maciej W. Rozycki
  role: contributor
  position: Provides the patch which retries line info lookup for MIPS compressed
    functions by setting the ISA bit in the offset.
  quote: 'The bfd_find_nearest_line_discriminator may not be able to find filename

    and line if pc points to start of a MIPS compressed function.  This is

    because ISA bit is set in the line number entries.  For example, if start

    of a function is 0x80200750 then line number entries start from 0x80200751

    (31st bit is set).  Set ISA bit of the pc and search again.'
- author: Maciej W. Rozycki
  role: reviewer
  position: Comments that the patch retries after other handlers fail by setting the
    ISA bit, which aligns with a similar GDB commit.
  quote: 'So this sets the ISA bit and retries once all the handlers have failed.

    This would be conceptually analogous to GDB commit 3e29f34a4eef ("MIPS:

    Keep the ISA bit in compressed code addresses"), which makes sense to me.'
primer_expert: 'This patch for `bfd`''s MIPS ELF backend addresses an issue with DWARF
  line number information for MIPS compressed instructions (MIPS16/microMIPS). The
  problem is that when the program counter (`pc`) points to the start of a compressed
  function, the DWARF line number entries might have the ISA bit (indicating compressed
  mode) set in their address, while the `pc` itself might not. The `_bfd_elf_find_nearest_line`
  function, when called with such a `pc`, fails to find the correct line. The patch
  adds a retry mechanism: if the initial lookup fails and the `pc` is not already
  marked as compressed,…'
primer_glossary:
- term: MIPS
  definition: A family of reduced instruction set computing (RISC) architectures developed
    by MIPS Computer Systems.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library, a GNU library used for accessing and
    manipulating various executable binary file formats.
- term: DWARF
  definition: Debugging With Attributed Record Formats, a standardized debugging data
    format used by many compilers and debuggers.
- term: compressed MIPS function
  definition: Refers to MIPS code generated using compression techniques (like MIPS16
    or microMIPS) to reduce instruction size, which can affect address interpretation.
- term: line info
  definition: Debugging information that maps machine code addresses back to source
    code lines.
- term: ISA bit
  definition: Instruction Set Architecture bit. In the context of MIPS compressed
    code, this bit in an address might indicate whether the instruction at that address
    is compressed.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611050419141.6502@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This discussion concerns a patch for MIPS ELF handling in the BFD library that aims to improve the accuracy of DWARF line number information for compressed MIPS functions. The patch proposes a strategy where, if the standard line number lookup fails, it retries by setting the Instruction Set Architecture (ISA) bit in the program counter offset. This is based on an observation that line number entries for compressed functions might have the ISA bit set, causing the initial lookup to fail if the PC does not also have this bit set. A reviewer notes that this approach is analogous to a GDB commit that preserves the ISA bit.
