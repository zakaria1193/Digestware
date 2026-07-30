---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- relocation
- compiler
- optimization
discussion_id: 20260729075955.799091-1-wengliqin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v3] RISC-V: Add new relocation types for global array accesses with
  non-constant indices'
headline: 'RISC-V: Add new relocation types for global array accesses with non-constant
  indices'
tldr: Adds RISC-V relocation types R_RISCV_BASE_IDX_* for efficient non-constant global
  array access, includes relaxation for absolute int12, and renames internal ty…
proposer: Liqin Weng <wengliqin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch set introduces and refines new relocation types for the
  RISC-V architecture within binutils. The core purpose is to optimize accesses to
  global arrays when the index is not a constant, by introducing specific relocation
  types (R_RISCV_BASE_IDX_*). This version v3 updates the support by including a relaxation
  mechanism for absolute int12 values and renames internal relocation types for clarity.
  Modifications are made across BFD and GAS, accompanied by new test cases.
primer_glossary:
- term: RISC-V
  definition: An open standard Instruction Set Architecture (ISA) based on RISC principles.
- term: relocation types
  definition: Information in an object file that guides the linker in resolving addresses
    and creating position-independent code.
- term: R_RISCV_BASE_IDX_*
  definition: New relocation types for RISC-V designed to optimize global array access
    with non-constant indices.
- term: relaxation
  definition: A process in assembly and linking where an instruction that initially
    used a relative or absolute address can be later adjusted to use a more efficient
    form, such as a PC-relative address, if the final location is known.
- term: BFD
  definition: The Binary File Descriptor library, part of GNU binutils, that provides
    a common API for object file manipulation.
- term: GAS
  definition: The GNU Assembler, which translates assembly language code into machine
    code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260729075955.799091-1-wengliqin@linux.spacemit.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This third version of the patch introduces new RISC-V relocation types (R_RISCV_BASE_IDX_*) to streamline global array accesses with dynamic indices. It clarifies that 'absolute int12 relaxation' is now supported for these types and renames internal relocation identifiers like INTERNAL_R_RISCV_BASE_IDX_* to R_RISCV_BASE_IDX_GPREL*. The changes span BFD and GAS, including new test cases.
