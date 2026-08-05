---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- RISC-V
- relocations
- optimization
- ABI
discussion_id: 20260804075202.2369022-1-wengliqin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v5] RISC-V: Add new relocation types for global array accesses with
  non-constant indices'
headline: 'RISC-V: Add new relocation types for global array accesses with non-constant
  indices'
tldr: Introduces new RISC-V relocation types for efficient global array access with
  dynamic indices.
proposer: Liqin Weng <wengliqin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Introduces new relocation types, potentially increasing complexity in the linker
  and assembler.
- Enables more efficient code for a specific access pattern, leading to performance
  improvements.
- Requires updates across multiple binutils components (BFD, GAS, ld) and toolchain
  support.
exchanges:
- author: Liqin Weng <wengliqin@linux.spacemit.com>
  role: proposer
  position: Introduces new RISC-V relocation types to optimize global array accesses
    with non-constant indices.
  quote: 'This patch introduces support for new RISC-V relocation types

    (R_RISCV_BASE_IDX_*) to enable more efficient code generation for

    global array accesses with non-constant array subscripts.'
primer_expert: This patch introduces new relocation types (R_RISCV_BASE_IDX_*) to
  the RISC-V toolchain, specifically within binutils (BFD, GAS, ld). These relocations
  are designed to optimize accesses to global arrays when the index is not a constant.
  This involves defining new ELF relocation types, handling their relaxation and emission,
  and updating associated tools and tests to support this new capability as per the
  RISC-V PSABI specification.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles.
- term: relocation types
  definition: Information in an object file that tells the linker how to modify memory
    addresses and other data when combining multiple object files into an executable
    or shared library.
- term: global array accesses
  definition: Operations (read or write) performed on elements of an array that is
    allocated in the global data segment of a program.
- term: non-constant indices
  definition: Array subscripts that are determined at runtime, rather than being fixed
    values known at compile time.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite, which translates
    assembly language code into object files.
- term: BFD
  definition: Binary File Descriptor library, part of GNU Binutils, which provides
    a common interface to various object file formats.
- term: PSABI
  definition: Platform-Specific Application Binary Interface. Defines conventions
    for how software components interact at the binary level for a specific platform
    or architecture.
- term: relaxation
  definition: A process during linking where initially generated, potentially less
    optimal, instructions or addresses are replaced with more efficient ones, often
    utilizing specialized relocation types.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260804075202.2369022-1-wengliqin@linux.spacemit.com
bugzilla_url: null
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

Liqin Weng proposes adding new RISC-V relocation types (R_RISCV_BASE_IDX_*) to improve code generation efficiency for global array accesses where the array subscript is not a compile-time constant. This patch updates BFD, GAS, and includes new test cases to support these relocation types, aligning with the RISC-V PSABI specification. The changes involve defining new relocation types, mapping internal relaxed relocations to public ELF equivalents, and documenting the new types.
