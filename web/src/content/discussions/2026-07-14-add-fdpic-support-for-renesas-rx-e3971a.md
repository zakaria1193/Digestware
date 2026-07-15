---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- rx
- fdpic
- linker
- embedded
discussion_id: 20260714131613.398963-1-yoshinori.sato@nifty.com
source_type: public_inbox
title: Add FDPIC support for Renesas RX
headline: Add FDPIC support for Renesas RX
tldr: Enables binutils to generate FDPIC binaries for the Renesas RX architecture,
  confirmed to work with BusyBox.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Implementing FDPIC support adds complexity to the toolchain but enables greater
  flexibility and memory efficiency in embedded systems.
- Ensuring correctness requires careful handling of new relocation types and linker
  script configurations.
exchanges:
- author: Yoshinori Sato <yoshinori.sato@nifty.com>
  role: proposer
  position: Submits a series of patches to add FDPIC support for the Renesas RX architecture
    to binutils.
  quote: 'This set of patches enables binutils to generate FDPIC binaries

    for the RX architecture.


    I have confirmed that BusyBox built with this toolchain runs

    successfully on an RX62N evaluation board.'
primer_expert: This RFC series introduces support for Fully Dynamic Position Independent
  Code (FDPIC) for the Renesas RX architecture in GNU binutils. FDPIC is a type of
  PIC that allows for dynamic linking and position independence even when code and
  data sections are far apart. The patches modify BFD to handle FDPIC relocations,
  gas to support FDPIC target options and directives, and ld to properly link FDPIC
  objects. The successful BusyBox execution on an RX62N board validates the implementation.
primer_glossary:
- term: FDPIC
  definition: Fully Dynamic Position Independent Code. A type of code that can be
    loaded and executed at any memory address, with dynamic linking capabilities.
- term: Renesas RX
  definition: A family of 32-bit microcontrollers from Renesas Electronics.
- term: binutils
  definition: A collection of programming tools for manipulating binary files, including
    the assembler (gas), linker (ld), and disassembler (objdump).
- term: PIC
  definition: Position Independent Code. Code that can be loaded and executed at any
    memory address without modification.
- term: BusyBox
  definition: A software utility that combines tiny versions of many common Unix utilities
    into a single small executable. Often used in embedded systems.
- term: GOTFUNCDESC
  definition: Global Offset Table Function Descriptor. Likely a structure used in
    FDPIC linking to resolve function addresses.
series_id: binutils:add fdpic support for renesas rx
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260714131613.398963-1-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Yoshinori Sato is proposing a set of patches to enable binutils support for generating FDPIC (Far Data PIC) binaries on the Renesas RX architecture. The changes span BFD, gas, and ld, introducing necessary FDPIC relocation types and target-specific configurations. Sato has successfully used a toolchain built with these patches to compile and run BusyBox on an RX62N board, confirming the functionality. This version (v3) includes fixes for a segmentation fault in `ld` and incorrect offset calculations for GOTFUNCDESC.
