---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bugfix
- bfd
- relocation
- nds32
discussion_id: ahVrCSmtOp-QIIkU@squeak.grove.modra.org
source_type: public_inbox
title: buffer overflow in nds32_elf_lo12_reloc
headline: Fixes buffer overflow in nds32_elf_lo12_reloc
tldr: Adds a sanity check to nds32_elf_lo12_reloc to prevent reading beyond the allocated
  buffer, and replaces a function call with a constant.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds a runtime check, which may introduce a small performance overhead.
- Replaces a function call with a macro, which may improve performance slightly.
exchanges: []
primer_expert: The patch addresses a potential buffer overflow vulnerability in `bfd/elf32-nds32.c`,
  specifically within the `nds32_elf_lo12_reloc` function. It adds a size check using
  `bfd_reloc_offset_in_range` before accessing relocation data. The patch also replaces
  calls to `bfd_octets_per_byte` with the `OCTETS_PER_BYTE` macro, which is likely
  a performance optimization. The vulnerability could be triggered by malformed ELF
  files with crafted relocation entries.
primer_general: The Binary File Descriptor (BFD) library is part of binutils and provides
  a generic interface for working with different object file formats like ELF. Relocations
  are adjustments the linker makes to code and data when combining object files. This
  patch adds a check to prevent the tool from reading beyond the allocated buffer
  when processing a specific type of relocation for the NDS32 architecture. Without
  this check, a malformed or malicious ELF file could cause the program to crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahVrCSmtOp-QIIkU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

This patch adds a sanity check to the `nds32_elf_lo12_reloc` function to ensure that the relocation offset is within the valid range, preventing potential buffer overflows when processing stashed hi relocs. It also replaces `bfd_octets_per_byte` calls with the `OCTETS_PER_BYTE` macro throughout the `elf32-nds32.c` file for consistency and potential performance gains. This prevents out-of-bounds reads and possible crashes when processing crafted or malformed binaries.
