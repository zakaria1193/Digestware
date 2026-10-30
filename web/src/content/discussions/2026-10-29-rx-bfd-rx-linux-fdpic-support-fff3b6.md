---
project: binutils
subsystem: rx
patch_id: null
tags:
- binutils
- rx
- bfd
- fdpic
- elf
discussion_id: 20261029120303.1987315-2-yoshinori.sato@nifty.com
source_type: public_inbox
title: 'RX: bfd rx-linux FDPIC support'
headline: 'RX: bfd rx-linux FDPIC support'
tldr: Adds FDPIC support to the BFD backend for the RX architecture on Linux, enabling
  new relocation types and FDPIC-specific object handling.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Significantly increases the complexity of the BFD backend for RX by adding FDPIC
  support.
- Introduces many new internal structures and functions, requiring careful review
  and testing.
exchanges: []
primer_expert: This patch series adds FDPIC support to the BFD backend for the `rx-linux`
  target. It touches `elf-bfd.h` to add a target identifier, and significantly modifies
  `elf32-rx.c`. The changes include adding FDPIC relocation types to `rx_elf_howto_table`
  and `rx_reloc_map`, introducing new link hash table structures (`elf_rx_link_hash_table`,
  `rx_elf_hash_table`), defining constants for FDPIC PLT entries, and implementing
  functions like `fdpic_elf_rx_plt_entry` and `fdpic_object_p`. It also enhances relocation
  handling and object creation logic for FDPIC.
primer_glossary:
- term: RX
  definition: A family of 32-bit microcontrollers developed by Renesas Electronics.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to provide
    a common interface for handling various object file formats, including ELF.
- term: FDPIC
  definition: Fully Distributable Position-Independent Code. A system for generating
    position-independent code that can be loaded and executed at any memory address
    without modification, including support for shared libraries and position-independent
    data sections.
- term: rx-linux
  definition: A target triplet indicating the RX architecture combined with the Linux
    operating system.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like operating systems.
- term: Relocation
  definition: The process by which the linker or loader adjusts memory addresses in
    code or data to their final locations in memory. This is necessary for position-independent
    code and linking object files.
series_id: 'binutils:rx: bfd rx-linux fdpic support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029120303.1987315-2-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch introduces support for FDPIC (Fully Distributable Position-Independent Code) into the BFD (Binary File Descriptor) library for the RX architecture on Linux. It modifies the `elf32-rx.c` file to handle FDPIC relocation types, introduces new structures and functions for FDPIC object data, and adds a check to determine if an object is FDPIC. This is a crucial part of enabling FDPIC support for the RX target in binutils.
