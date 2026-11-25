---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- bug fix
discussion_id: 20261125080658.1445826-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: Adds checks in the LoongArch ELF relocation process to detect and reject relocations
  that extend beyond their section boundaries.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submits a revised patch to implement relocation range checking for LoongArch
    ELF files, placing the check within `relocate_section` as suggested.
  quote: 'Use bfd_reloc_offset_in_range in loongarch_elf_relocate_section to reject
    input relocations whose fields extend outside their section. ... v1 -> v2: - Check
    in relocate_section as Alan suggested.'
primer_expert: This patch modifies `bfd/elfnn-loongarch.c` to use `bfd_reloc_offset_in_range`
  within `loongarch_elf_relocate_section`. The goal is to validate that input relocations,
  when their size is considered, do not extend beyond the end of the input section
  they are associated with. This prevents potential issues in later linking stages
  caused by invalid relocation offsets. The patch also adds new test cases in `ld/testsuite/ld-loongarch-elf/`
  to cover this scenario.
primer_glossary:
- term: Relocation
  definition: A process performed by the linker to adjust symbolic addresses in object
    code after it has been combined. Relocations indicate where in the code addresses
    need to be updated.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object code,
    executables, and shared libraries on many Unix-like systems.
- term: R_LARCH_NONE
  definition: A LoongArch relocation type that indicates no operation is needed; it's
    a placeholder or might be used in specific contexts.
- term: R_LARCH_RELAX
  definition: A LoongArch relocation type used for instruction relaxation, where the
    linker might adjust instruction encodings for performance or size.
- term: bfd_reloc_offset_in_range
  definition: A BFD library function that checks if a given relocation offset, considering
    its size, falls within the bounds of a specified section.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125080658.1445826-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch introduces a check within the LoongArch ELF relocation processing to identify and reject relocations whose fields extend outside the bounds of their respective input sections. It utilizes `bfd_reloc_offset_in_range` for this validation and skips certain relocation types like `R_LARCH_NONE` and `R_LARCH_RELAX`. New test cases are included to verify this functionality.
