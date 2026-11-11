---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- relocation
- bounds checking
- security
- linker
discussion_id: 20261110201522.2149977-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/5] RISC-V: reject relocation offsets outside the section'
headline: 'RISC-V: reject relocation offsets outside the section'
tldr: Adds checks to reject RISC-V relocations targeting memory outside the section
  bounds, preventing memory corruption and crashes.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Significantly improves security and stability by preventing out-of-bounds memory
  accesses during relocation, which could otherwise lead to crashes or exploitable
  vulnerabilities.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Implements checks in `riscv_elf_relocate_section` to ensure all relocation
    fields, including those for `R_RISCV_TLSDESC_CALL`, are within the section bounds,
    using a new helper function `riscv_reloc_field_in_range`.
  quote: 'riscv_elf_relocate_section applies relocations without checking that

    the relocated field lies inside the section, so a relocation with a

    bad r_offset reads and writes past the section contents.


    Add riscv_reloc_field_in_range and check each relocation field against

    bfd_get_section_limit_octets before the relocation is applied.'
primer_expert: This patch addresses a critical safety issue in RISC-V relocation handling
  within `bfd/elfnn-riscv.c`. It introduces `riscv_reloc_field_in_range` to perform
  explicit bounds checking on relocation targets, preventing writes or reads beyond
  the section's boundaries. This is particularly important for relocations like `R_RISCV_TLSDESC_CALL`
  which, despite having a zero HOWTO size, involve instruction rewriting that can
  extend beyond the section end if not checked. The patch also correctly handles `R_RISCV_NONE`
  and ensures checks are applied even during relaxation, improving overall linker
  robus…
primer_glossary:
- term: relocation
  definition: The process of updating symbolic references in object code to their
    final memory addresses after linking.
- term: R_RISCV_TLSDESC_CALL
  definition: A RISC-V relocation type specifically for TLS (Thread-Local Storage)
    descriptor calls, which may involve instruction rewriting.
- term: bfd_putl32
  definition: A BFD library function to write a 32-bit value to memory, typically
    used for patching instruction fields.
- term: AddressSanitizer
  definition: A fast memory error detector for C/C++ that finds use-after-free, buffer
    overflows, and other memory bugs.
- term: HOWTO size
  definition: In the context of BFD relocations, this refers to the size of the field
    being modified by the relocation, as defined in the relocation type's HOWTO structure.
series_id: 'binutils:risc-v: reject relocation offsets outside the section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch introduces `riscv_reloc_field_in_range` to validate relocation field offsets against the section's limits before applying them in `riscv_elf_relocate_section`. This prevents operations like `bfd_putl32` from writing past the end of the section, which could lead to heap-buffer-overflows, as seen with `R_RISCV_TLSDESC_CALL`. It also correctly skips `R_RISCV_NONE` relocations and ensures that relocations used during relaxation are also checked.
