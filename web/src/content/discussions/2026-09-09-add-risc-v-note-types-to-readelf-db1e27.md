---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- RISC-V
- ELF
- notes
discussion_id: 20260909055707.20097-1-heinrich.schuchardt@canonical.com
source_type: public_inbox
title: 'readelf: add support for more RISC-V note types'
headline: Add RISC-V note types to readelf
tldr: Readelf now supports displaying new RISC-V note types for vector, tagged address
  control, and user CFI.
proposer: Heinrich Schuchardt <heinrich.schuchardt@canonical.com>
consensus: Proposed
outcome: needs_revision
impact_score: 3
sentiment_score: 8
technical_tradeoffs:
- Improves visibility into RISC-V binaries by supporting new note types.
- Minimal performance impact, primarily affects parsing of ELF files with these notes.
exchanges:
- author: Heinrich Schuchardt
  role: proposer
  position: Adds definitions and string values for three new RISC-V note types to
    binutils' readelf.
  quote: 'Add definitions and string values for note types


    * NT_RISCV_VECTOR               0x901

    * NT_RISCV_TAGGED_ADDR_CTRL     0x902

    * NT_RISCV_USER_CFI             0x903'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the patch as largely okay, but points out a minor nit regarding
    the formatting of comment lines in the header file.
  quote: 'Largely okay, one nit:'
primer_expert: This patch adds support for new RISC-V ELF note types (NT_RISCV_VECTOR,
  NT_RISCV_TAGGED_ADDR_CTRL, NT_RISCV_USER_CFI) to the `readelf` utility. These notes,
  defined in Linux kernel headers, provide information about RISC-V specific features,
  such as vector registers and control flow integrity state. The change ensures `readelf`
  can correctly parse and display these notes when examining RISC-V ELF binaries.
primer_glossary:
- term: readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files, including headers, section details, symbol tables,
    and notes.
- term: ELF note
  definition: A section in an ELF file that contains miscellaneous information, often
    vendor-specific, for tools or the runtime environment. Notes are identified by
    a name and a type.
- term: NT_RISCV_VECTOR
  definition: An ELF note type specific to RISC-V, intended to describe the state
    of vector registers.
- term: NT_RISCV_TAGGED_ADDR_CTRL
  definition: An ELF note type for RISC-V that conveys control information related
    to tagged memory addressing.
- term: NT_RISCV_USER_CFI
  definition: An ELF note type for RISC-V, likely related to user-space Control Flow
    Integrity (CFI) state, possibly for shadow stack information.
series_id: 'binutils:readelf: add support for more risc-v note types'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260909055707.20097-1-heinrich.schuchardt@canonical.com
bugzilla_url: null
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

This patch updates the `readelf` utility to recognize and display three new RISC-V-specific ELF note types: NT_RISCV_VECTOR, NT_RISCV_TAGGED_ADDR_CTRL, and NT_RISCV_USER_CFI. These additions align binutils with recent definitions in the Linux kernel's ELF headers, enabling better inspection of RISC-V executables.
