---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- ELF
- relocations
- security
discussion_id: 20261116184333.3297411-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[RFC PATCH 00/17] bfd: check that ELF relocation fields lie inside their section'
headline: 'bfd: check that ELF relocation fields lie inside their section'
tldr: RFC proposes a unified check in BFD to ensure ELF relocation fields fit within
  their sections, with per-target patches to handle backend-specific nuances.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Ready to Land
outcome: ready
impact_score: 7
sentiment_score: 7
technical_tradeoffs:
- Adds complexity to BFD by introducing new backend data structures and a centralized
  check.
- Requires per-target patches to correctly define relocation characteristics, increasing
  maintenance effort.
- Potentially rejects previously valid objects if backend descriptions are inaccurate
  or incomplete.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes a series of patches to add a unified check in BFD for ELF relocation
    field bounds, requiring per-backend adjustments.
  quote: Before sending more per-backend patches, I'd like your view on doing the
    check once, for every ELF backend.
- author: Harshit Kumar
  role: proposer
  position: Adds two members to `elf_backend_data` to allow backends to describe their
    relocation field sizes and composition rules.
  quote: 'Add two elf_backend_data members for the relocation offset check that a
    later patch adds to the linker, so that backends can describe their relocations
    before the check is turned on:


    - elf_backend_reloc_field_size gives the number of octets that a relocation type
    may read or write at r_offset, where the howto does not give it, or 0 for a type
    with no field.

    - relocs_compose_at_offset says that r…'
- author: Harshit Kumar
  role: proposer
  position: Explains how NDS32 relaxation relocations should be handled, as they mark
    positions rather than fields and have specific size requirements.
  quote: R_NDS32_RELAX_ENTRY, R_NDS32_LABEL and R_NDS32_RELAX_REGION_BEGIN and _END
    mark a position for relaxation, not a field, but have a 4-octet howto with a dst_mask.
    The assembler puts RELAX_ENTRY at offset 0 of a section of any size, and LABEL
    may be at its end, so a relocation offset check that took their howto size would
    reject valid objects. Give them a field size of 0 through elf_backend_reloc_f…
- author: Harshit Kumar
  role: proposer
  position: Describes MIPS's composed relocations and the need to handle them correctly
    to avoid rejecting valid objects.
  quote: 'MIPS relocate_section composes consecutive relocations at the same offset:
    each one but the last passes its result to the next as the addend, and only the
    last one writes the field. The intermediate ones may have a wider howto than the
    field, as R_MIPS_SUB (8 octets) in %hi(%neg(%gp_rel(x))), whose final R_MIPS_HI16
    writes 4, so a relocation offset check that took every howto size would reject
    su…'
- author: Harshit Kumar
  role: proposer
  position: Explains how RX relocations for symbol differences require special handling
    due to their composition and write behavior.
  quote: RX describes a symbol difference as several relocations at one offset. R_RX_SYM
    and the R_RX_OP* relocations push or combine values on the relocation stack and
    write nothing; only the relocation that pops the stack writes the field, which
    may be 1 or 2 octets. Their howto size is 4, so a relocation offset check that
    took it would reject a difference such as ".byte foo - bar" in the last octets
    of…
- author: Harshit Kumar
  role: proposer
  position: Details how MSP430 symbol difference relocations need to be treated as
    having a field size of 0 to avoid false rejections.
  quote: MSP430 describes a symbol difference as R_MSP430_SYM_DIFF (or R_MSP430X_SYM_DIFF),
    which only computes a value, followed at the same offset by the relocation that
    writes the field, which may be 1 or 2 octets. The SYM_DIFF howto size is 4, so
    a relocation offset check that took it would reject a difference such as ".byte
    foo - bar" in the last octets of a section. Give SYM_DIFF a field size of 0.…
primer_expert: This series of patches introduces a safety check into BFD's ELF relocation
  handling to prevent relocations from writing outside the bounds of their assigned
  section. Currently, several ELF backends do not verify that `r_offset + field_size`
  is within the section's limits. The core patch in `elf_link_read_relocs_from_section`
  adds this check, requiring new `elf_backend_data` members (`elf_backend_reloc_field_size`
  and `relocs_compose_at_offset`) to describe target-specific relocation characteristics.
  Subsequent patches provide these descriptions for various architectures (NDS32,
  MIPS, RX, MSP4…
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to read and write various executable file formats.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: relocation
  definition: Information in an object file that describes how to modify code or data
    pointers to refer to symbols in other modules or at different memory addresses.
- term: r_offset
  definition: The offset within a section where a relocation needs to be applied.
- term: howto
  definition: A data structure within BFD that describes the relocation types and
    their properties for a specific target architecture.
- term: composed relocations
  definition: A scenario where multiple relocations at the same offset are treated
    as a single operation, often involving intermediate results being passed between
    them.
- term: AddressSanitizer
  definition: A fast memory error detector for C/C++ that finds issues like buffer
    overflows and use-after-free.
series_id: 'binutils:bfd: check that elf relocation fields lie inside their section'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116184333.3297411-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This RFC proposes a centralized check within the BFD library to ensure that ELF relocation fields reside entirely within their respective sections. Currently, many ELF backends lack this check, leading to potential issues when relocations access memory beyond section boundaries. The proposal includes a core patch to implement this check in `elf_link_read_relocs_from_section`, along with several per-target patches to accommodate variations in how different architectures define relocation field sizes and handle composed relocations.
