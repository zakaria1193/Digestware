---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relaxation
- relocation
discussion_id: 20261110201522.2149977-6-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 5/5] RISC-V: check relocation fields during relaxation'
headline: 'RISC-V: check relocation fields during relaxation'
tldr: Enhances RISC-V relaxation by validating relocation field offsets against section
  bounds to prevent out-of-bounds reads/writes.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds more robust error checking during relaxation, preventing potential memory corruption
  at the cost of slightly increased complexity in the relocation handling code.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Introduces `riscv_relax_field_in_range` to validate relocation accesses
    during relaxation and replaces assertions with explicit checks for various relocation
    types, addressing PR ld/34987.
  quote: 'Relaxation runs before riscv_elf_relocate_section.  Relocation bounds

    checks in the final link loop do not protect relaxation passes.


    Relaxation helpers read and write fields at rel->r_offset.  Previously,

    these helpers relied on BFD_ASSERT.  The default assert handler logs an

    error and continues execution out of bounds.


    Replace assertions in relaxation helpers with riscv_relax_field_in_range.…'
primer_expert: This patch refactors RISC-V relocation handling during the relaxation
  phase. It introduces `riscv_relax_field_in_range` to replace generic `BFD_ASSERT`
  calls, ensuring that operations like writing to `rel->r_offset` or processing instruction
  spans stay within `sec->size`. This is crucial because the default assert handler
  in BFD allows execution to continue after an assertion failure, potentially leading
  to memory corruption. The patch specifically addresses issues with `R_RISCV_DELETE`
  and instruction alignment checks, augmenting the safety of the relaxation process.
primer_glossary:
- term: Relaxation
  definition: A linker optimization process where instructions or data are adjusted
    to occupy less space or to adapt to runtime conditions, often involving changes
    to instruction encoding or addresses.
- term: R_RISCV_DELETE
  definition: A RISC-V relocation type that indicates a sequence of bytes should be
    removed during linking.
- term: BFD_ASSERT
  definition: A macro used in the Binary File Descriptor library (BFD) for asserting
    conditions that should always be true. If the condition is false, it typically
    triggers an error message and program termination or, in some configurations,
    continues execution.
- term: psABI
  definition: The Application Binary Interface for the specific architecture and operating
    system. For RISC-V, it defines conventions for how software is compiled and linked.
series_id: 'binutils:risc-v: check relocation fields during relaxation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-6-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch series enhances RISC-V linker relaxation by introducing `riscv_relax_field_in_range` to validate relocation field accesses against section sizes. It replaces existing assertions with explicit range checks, particularly for `R_RISCV_DELETE` and instruction spans, to prevent out-of-bounds memory operations during relaxation. New test cases are added to cover these scenarios, addressing PR ld/34987.
