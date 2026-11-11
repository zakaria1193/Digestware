---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- relocation
- bounds checking
- security
discussion_id: 20261110201522.2149977-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 3/5] RISC-V: check ULEB128 relocation field bounds'
headline: 'RISC-V: check ULEB128 relocation field bounds'
tldr: Adds bounds checking for RISC-V ULEB128 relocation fields to prevent buffer
  overflows and ensure termination within section limits.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Improves robustness and security by preventing buffer overflows related to ULEB128
  encoding, at the expense of slightly more complex relocation validation logic.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Enhances RISC-V relocation handling by adding checks for ULEB128 sequences
    to ensure they are within section bounds and properly terminated, preventing buffer
    overflows and incorrect linking.
  quote: 'R_RISCV_SET_ULEB128 and R_RISCV_SUB_ULEB128 have a HOWTO size of zero

    because their encoded length varies, so the range check added by the

    previous patch accepts an offset equal to the section size.  For

    R_RISCV_SUB_ULEB128 at that offset, perform_relocation decodes zero

    bytes, computes len - 1 with len == 0 and passes (size_t) -1 to memset.


    Before applying either relocation, check that at least…'
primer_expert: This patch refines the handling of RISC-V ULEB128 relocations (`R_RISCV_SET_ULEB128`,
  `R_RISCV_SUB_ULEB128`) within `elfnn-riscv.c`. It corrects a flaw where a zero-size
  HOWTO for these relocations bypassed previous bounds checks, leading to potential
  buffer overflows in `perform_relocation` when decoding or writing. The fix ensures
  that ULEB128 sequences are fully contained within the target section and properly
  terminated, preventing silent truncation or corruption. It also introduces a specific
  error return for zero-length decodes and associated test cases.
primer_glossary:
- term: R_RISCV_SET_ULEB128
  definition: A RISC-V relocation type used in conjunction with R_RISCV_SUB_ULEB128
    to encode variable-length unsigned integers.
- term: R_RISCV_SUB_ULEB128
  definition: A RISC-V relocation type used in conjunction with R_RISCV_SET_ULEB128
    to encode variable-length unsigned integers.
- term: ULEB128
  definition: Unsigned LEB128 (Little-Endian Base 128) is a variable-length encoding
    format for integers, commonly used in DWARF debugging information and some ABIs.
- term: HOWTO size
  definition: In the context of BFD relocations, this refers to the size of the field
    being modified by the relocation, as defined in the relocation type's HOWTO structure.
- term: bfd_reloc_outofrange
  definition: An error code returned by BFD functions indicating that a relocation
    operation attempted to access memory outside the defined bounds of a section.
series_id: 'binutils:risc-v: check uleb128 relocation field bounds'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch addresses issues with RISC-V `R_RISCV_SET_ULEB128` and `R_RISCV_SUB_ULEB128` relocations that previously allowed out-of-bounds access due to their variable length encoding. It introduces checks to ensure that at least one byte is available at the relocation offset and that the ULEB128 sequence terminates within the section's size. The patch also modifies `perform_relocation` to return `bfd_reloc_outofrange` for zero-length decodes and adds new test cases to verify these boundary conditions.
