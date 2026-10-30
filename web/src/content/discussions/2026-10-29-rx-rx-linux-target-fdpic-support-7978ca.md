---
project: binutils
subsystem: rx
patch_id: null
tags:
- binutils
- rx
- elf
- fdpic
- relocation
discussion_id: 20261029120303.1987315-5-yoshinori.sato@nifty.com
source_type: public_inbox
title: 'RX: rx-linux target FDPIC support'
headline: 'RX: rx-linux target FDPIC support'
tldr: Adds FDPIC relocation types and flags to the ELF header definitions for the
  RX architecture on Linux.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds new ELF relocation types and flags, increasing the complexity of the ELF parsing
  and handling logic.
- Requires corresponding changes in other tools (gas, ld) to fully utilize these new
  definitions.
exchanges: []
primer_expert: This patch is part of a series to enable FDPIC support for the RX target.
  It specifically modifies `include/elf/rx.h` to define new ELF relocation types necessary
  for FDPIC, such as `R_RX_GOT`, `R_RX_PLT`, and various GOT-related entries. It also
  introduces `EF_RX_PIC` and `EF_RX_FDPIC` flags to the ELF header to indicate the
  code's position-independent nature.
primer_glossary:
- term: RX
  definition: A family of 32-bit microcontrollers developed by Renesas Electronics.
- term: FDPIC
  definition: Fully Distributable Position-Independent Code. A system for generating
    position-independent code that can be loaded and executed at any memory address
    without modification, including support for shared libraries and position-independent
    data sections.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like operating systems.
- term: Relocation
  definition: The process by which the linker or loader adjusts memory addresses in
    code or data to their final locations in memory. This is necessary for position-independent
    code and linking object files.
- term: GOT
  definition: Global Offset Table. A data structure used in position-independent code
    (PIC) to store addresses of dynamically resolved external functions and global
    variables.
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables and shared
    libraries to resolve addresses of external functions at runtime, typically in
    conjunction with the GOT.
series_id: 'binutils:rx: rx-linux target fdpic support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029120303.1987315-5-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch updates the ELF definitions for the RX architecture on Linux to include support for FDPIC (Fully Distributable Position-Independent Code). It adds new relocation types related to GOT (Global Offset Table), PLT (Procedure Linkage Table), and other FDPIC-specific mechanisms, as well as defines flags for PIC and FDPIC in the ELF header.
