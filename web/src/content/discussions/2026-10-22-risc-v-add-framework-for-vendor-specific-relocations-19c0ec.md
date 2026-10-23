---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- relocation
- elf
- ABI
discussion_id: 20261022124553.3922763-2-ycl669@andestech.com
source_type: public_inbox
title: '[PATCH v3 1/2] RISC-V: Add framework for vendor-specific relocations'
headline: 'RISC-V: Add framework for vendor-specific relocations.'
tldr: Adds a framework to binutils to support vendor-specific RISC-V relocations,
  enabling custom relocation types beyond the standard set.
proposer: Ethan Y. C. Liang <ycl669@andestech.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enables extensibility for RISC-V relocations by allowing vendors to define custom
  types.
- Adds complexity to relocation handling and requires careful adherence to the psABI
  specification.
exchanges:
- author: Ethan Y. C. Liang
  role: proposer
  position: Proposes adding a framework to binutils for RISC-V vendor-specific relocations.
  quote: 'The RISC-V psABI reserves relocation numbers 192-255 for vendor-specific

    relocations [1].  Each of them must be preceded by an R_RISCV_VENDOR at

    the same offset, whose symbol identifies the vendor.  This patch adds

    the framework for them; no vendor is added yet.'
primer_expert: This patch implements the framework in binutils (specifically BFD,
  `readelf`, `objdump`, and `ld`) to support the RISC-V psABI's mechanism for vendor-specific
  relocations. These custom relocations occupy the 192-255 range and must be preceded
  by an `R_RISCV_VENDOR` relocation whose symbol identifies the vendor. The patch
  defines how to register new vendors, how the tools should interpret and display
  these relocations, and how `ld` and `gas` should handle them, including error checking
  for malformed vendor relocations.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture based on RISC principles.
- term: psABI
  definition: Processor-Specific Application Binary Interface. Defines the low-level
    conventions for function calls, data types, and other aspects of program execution
    for a specific processor architecture and operating system.
- term: relocation
  definition: Information in an object file that describes how to modify memory addresses
    and other references when the code or data is loaded into memory or linked with
    other modules. Relocations are necessary to make code position-independent or
    to resolve external references.
- term: R_RISCV_VENDOR
  definition: A specific type of relocation for RISC-V that signals the presence of
    a vendor-specific relocation following it.
- term: GAS
  definition: GNU Assembler. The assembler used in the GNU toolchain.
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to handle various object file formats.
- term: ld
  definition: The GNU linker, which combines object files and libraries into an executable.
series_id: 'binutils:risc-v: add framework for vendor-specific relocations'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261022124553.3922763-2-ycl669@andestech.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This patch introduces a framework within binutils to handle vendor-specific relocations for the RISC-V architecture, as defined by the RISC-V psABI. It allows vendors to define their own relocation types within a reserved range (192-255), each preceded by an R_RISCV_VENDOR relocation. The changes affect `readelf`, `objdump`, and `ld`, enabling them to recognize and process these custom relocations. GAS will emit the `R_RISCV_VENDOR` directive before each vendor-specific relocation it generates.
