---
project: binutils
subsystem: elf
patch_id: null
tags:
- PowerPC
- ELF
- core dump
- registers
- binutils
discussion_id: 5b76e365-0baf-4440-a478-1fbcb8146c7e@linux.ibm.com
source_type: public_inbox
title: 'Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
headline: 'Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
tldr: Proposer pings for review of a patch adding support for new PowerPC Dense Math
  Registers in core files.
proposer: Abhay Kandpal <abhay@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds new functionality for a future hardware feature without immediate runtime impact
  on existing systems.
- Increases the complexity of ELF core file parsing within BFD and readelf.
exchanges:
- author: Abhay Kandpal <abhay@linux.ibm.com>
  role: proposer
  position: Following up on a previously submitted patch to inquire about its review
    status and any required changes.
  quote: Just a gentle ping to see if anyone has had a chance to review this patch,
    or if any further changes are needed on my end.
- author: Abhay Kandpal <abhay@linux.ibm.com>
  role: proposer
  position: 'Describes the patch''s functionality: adding BFD and readelf support
    for NT_PPC_DMR, which stores Dense Math Registers for future PowerPC processors.'
  quote: Add BFD and readelf support for the new NT_PPC_DMR note type, which carries
    the contents of the Dense Math Registers (DMR) available on a future PowerPC processor.
    The DMR register set consists of eight 1024-bit registers introduced by the Dense
    Math facility in a future Power ISA revision.
primer_expert: This patch adds handling for the NT_PPC_DMR ELF note type to binutils'
  BFD library and the readelf utility. This note type is intended to store Dense Math
  Registers (DMR) for a future PowerPC processor revision, enabling core file analysis
  of this new register set. The changes involve new functions and type handlers within
  elf.c and bfd/elf-bfd.h, and updates to readelf.c.
primer_glossary:
- term: NT_PPC_DMR
  definition: A new ELF note type proposed to carry the contents of Dense Math Registers
    (DMR) in core dump files for future PowerPC processors.
- term: BFD
  definition: The Binary File Descriptor library, a low-level interface used by binutils
    for handling various object file formats, including ELF.
- term: readelf
  definition: A command-line utility in binutils that displays information about ELF
    files.
- term: Dense Math Registers (DMR)
  definition: A new set of registers (eight 1024-bit registers) introduced by the
    Dense Math facility in a future Power ISA revision, intended for specialized mathematical
    operations.
- term: ELF note type
  definition: A mechanism within the ELF file format used to store auxiliary data
    beyond standard sections, such as program headers or debugging information. Examples
    include NT_PRPSINFO, NT_FILE, and the proposed NT_PPC_DMR.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/5b76e365-0baf-4440-a478-1fbcb8146c7e@linux.ibm.com
bugzilla_url: null
date: '2026-07-13'
is_stub: false
stub_reason: ''
---

This patch introduces support for the NT_PPC_DMR note type in BFD and readelf, which will carry Dense Math Register contents for future PowerPC processors. The proposer is following up to inquire about the review status of the patch and whether further changes are needed. GDB support will follow in a later patch.
