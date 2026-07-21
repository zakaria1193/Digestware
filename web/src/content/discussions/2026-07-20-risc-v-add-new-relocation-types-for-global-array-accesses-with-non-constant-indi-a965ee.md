---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- relocation
- optimization
- compiler
discussion_id: 20260720083312.2953958-1-wengliqin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v2] RISC-V: Add new relocation types for global array accesses with
  non-constant indices'
headline: 'RISC-V: Add new relocation types for global array accesses with non-constant
  indices'
tldr: Adds new relocation types to RISC-V support for efficient global array access
  with non-constant subscripts.
proposer: Liqin Weng <wengliqin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased complexity in relocation handling.
exchanges: []
primer_expert: Adds new BFD relocation types (R_RISCV_BASE_IDX_*) and corresponding
  GAS support for RISC-V. This facilitates compiler optimization for global array
  accesses with non-constant indices by allowing the linker to better resolve addresses,
  potentially reducing runtime overhead. It aligns with the RISC-V PSABI specification.
primer_glossary:
- term: Relocation
  definition: The process of modifying code or data in an object file to allow it
    to be loaded at a different address in memory than it was originally compiled
    for. Relocations are typically handled by the linker.
- term: RISC-V
  definition: A free and open instruction set architecture (ISA) based on RISC principles.
- term: PSABI
  definition: Platform-Specific Application Binary Interface. Defines conventions
    for how software components interact at the binary level for a specific platform.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils for manipulating
    object files in various formats.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260720083312.2953958-1-wengliqin@linux.spacemit.com
bugzilla_url: null
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This patch introduces new RISC-V relocation types (R_RISCV_BASE_IDX_*) to the binutils project. These relocations are designed to enable more efficient code generation for global array accesses where the array subscript is not a compile-time constant. The changes affect BFD, GAS, and header files, and include new test cases.
