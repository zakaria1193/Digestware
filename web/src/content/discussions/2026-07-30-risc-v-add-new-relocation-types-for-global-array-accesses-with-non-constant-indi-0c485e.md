---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- relocation
- compiler
discussion_id: 20260730010330.4124332-1-wengliqin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v4] RISC-V: Add new relocation types for global array accesses with
  non-constant indices'
headline: 'RISC-V: Add new relocation types for global array accesses with non-constant
  indices'
tldr: Introduces new RISC-V relocation types (R_RISCV_BASE_IDX_*) for efficient global
  array access with non-constant indices.
proposer: Liqin Weng <wengliqin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch adds new relocation types to binutils for the RISC-V architecture,
  aimed at optimizing accesses to global arrays where the index is not a compile-time
  constant. This involves modifications to BFD (Binary File Descriptor) and GAS (GNU
  Assembler) to recognize and generate these new relocation types, referred to as
  R_RISCV_BASE_IDX_*. The goal is to improve performance by allowing the compiler
  to generate more specialized instructions for such memory accesses.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: relocation types
  definition: Information embedded in an object file that tells the linker how to
    adjust addresses in the code or data when combining different pieces of code or
    when creating position-independent code.
- term: R_RISCV_BASE_IDX_*
  definition: New relocation types specific to RISC-V, designed to handle base-relative
    indexed accesses to global arrays, particularly when the index is dynamic.
- term: PSABI
  definition: Processor Specific Application Binary Interface; defines calling conventions,
    data layout, and object file formats for a specific architecture and operating
    system.
- term: BFD
  definition: Binary File Descriptor library, a backend for GNU binutils that provides
    a common interface to various object file formats.
- term: GAS
  definition: GNU Assembler, the assembler used by the GNU toolchain.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260730010330.4124332-1-wengliqin@linux.spacemit.com
bugzilla_url: null
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This patch introduces support for new RISC-V relocation types, specifically R_RISCV_BASE_IDX_LO12, R_RISCV_BASE_IDX_LO12_S, and R_RISCV_BASE_IDX_ADD. These are designed to enable more efficient code generation for accessing global arrays when the array subscripts are not constant, aligning with the RISC-V PSABI specification.
