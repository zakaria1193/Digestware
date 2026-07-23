---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- embedded
- vector
discussion_id: amGJcET5P8VdW3hb@atctlc04
source_type: public_inbox
title: '[PING][PATCH 0/7] RISC-V: Add support for Andes floating-point and vector
  extensions'
headline: 'RISC-V: Add support for Andes floating-point and vector extensions'
tldr: Patch series proposes adding support for several Andes RISC-V extensions in
  binutils, enhancing floating-point and vector processing.
proposer: '"Ethan Y. C. Liang" <ycl669@andestech.com>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Ethan Y. C. Liang <ycl669@andestech.com>
  role: proposer
  position: Pings the maintainer for an update on the patch series and offers further
    assistance.
  quote: Just a quick ping on the patch series. Let me know if you need anything from
    my side.
primer_expert: This series adds support for Andes-specific RISC-V extensions (XAndes...)
  to GNU Binutils. It primarily affects `gas` (assembler) and `bfd` (binary file descriptor)
  for the RISC-V target, enabling recognition and processing of new instructions related
  to floating-point (e.g., `XAndesBFHCvt`) and vector operations (e.g., `XAndesVBFHCvt`,
  `XAndesVPackFPH`, `XAndesVQMac`).
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles, designed to be simple, modular, and extensible.
- term: Andes Technology Corporation
  definition: A company that designs and licenses RISC-V Processor IP cores, offering
    various extensions for specialized applications.
- term: Binutils
  definition: A collection of programming tools for developing programs for computers,
    including the assembler (gas), linker (ld), and binary file analysis tools.
- term: Extensions
  definition: In the context of ISAs like RISC-V, extensions are optional sets of
    instructions that add new capabilities beyond the base ISA.
- term: Floating-point
  definition: A method of representing real numbers in computers using a fixed number
    of digits before and after a decimal point, often involving a sign, exponent,
    and significand.
- term: Vector operations
  definition: Operations that perform the same instruction on multiple data points
    simultaneously, often used for performance-intensive tasks in scientific computing
    and multimedia.
- term: bfd
  definition: Binary File Descriptor library, a part of GNU Binutils used to abstract
    the details of different object file formats (like ELF, COFF).
- term: gas
  definition: The GNU Assembler, the assembler provided by the GNU toolchain, responsible
    for converting assembly language code into machine code.
series_id: 'binutils:risc-v: add support for andes floating-point and vector extensions'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/amGJcET5P8VdW3hb@atctlc04
bugzilla_url: null
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

This patch series introduces support for seven new Andes RISC-V extensions to the binutils project. These extensions, including capabilities for floating-point conversion and vector operations, have been in commercial use by Andes for several years. The proposer seeks feedback to ensure a smooth integration with the open-source ecosystem.
