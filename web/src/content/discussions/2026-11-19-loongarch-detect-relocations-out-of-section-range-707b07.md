---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- relocation
- linker
- security
discussion_id: 20261119124742.1434928-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: Adds checks to detect and reject relocations outside the section range during
  final linking for LoongArch.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- The reviewer questions the placement of the check, suggesting `relocate_section`
  might be more appropriate than `check_relocs` for comprehensive coverage.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Adds checks to reject relocations whose fields are out of the input section
    range by using `bfd_reloc_offset_in_range`.
  quote: 'Use bfd_reloc_offset_in_range in check_relocs to reject relocations

    whose fields are out of the input section range during final linking.'
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Suggests that the relocation checks might be better placed in `relocate_section`
    instead of `check_relocs`, as `check_relocs` is not called for all sections.
  quote: 'This is better done in relocate_section, unless loongarch reads

    section contents in check_relocs.  check_relocs is not called for some

    sections (see _bfd_elf_link_iterate_on_relocs), so for instance, debug

    sections won''t have their relocations sanity checked.'
primer_expert: This patch enhances the LoongArch ELF backend by adding validation
  for relocation offsets. It prevents relocations from referencing addresses outside
  their designated section by using `bfd_reloc_offset_in_range` within `elfnn-loongarch.c`.
  The reviewer suggests moving this check to `relocate_section` for more comprehensive
  coverage, as `check_relocs` has limitations.
primer_glossary:
- term: LoongArch
  definition: A RISC-V based instruction set architecture.
- term: relocation
  definition: A modification to an instruction or data in an object file that is required
    to resolve external references or to adapt code for execution in a specific memory
    address.
- term: ELF
  definition: Executable and Linkable Format, a common standard for object file formats
    on Unix-like systems.
- term: bfd_reloc_offset_in_range
  definition: A BFD library function that checks if a relocation's offset falls within
    the boundaries of a given section.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261119124742.1434928-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch introduces checks in the LoongArch ELF backend to ensure that relocations are within the bounds of their input section. It utilizes `bfd_reloc_offset_in_range` in `check_relocs` to reject invalid relocations during the final linking phase. New test cases are also added to verify this functionality.
