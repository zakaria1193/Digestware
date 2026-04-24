---
project: binutils
subsystem: asan
patch_id: null
tags:
- bfd
- elf
- z80
- relocation
- asan
discussion_id: aen3u_6aPVWoRrRP@squeak.grove.modra.org
source_type: public_inbox
title: 'asan: unknown write in z80_elf_16_be_reloc'
headline: 'asan: unknown write in z80_elf_16_be_reloc'
tldr: Fixes an address sanitizer (ASan) error in the Z80 ELF relocator by adding a
  range check on the relocation offset.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds a range check, which may slightly impact performance, although the impact should
  be minimal.
- Increases code size slightly.
exchanges: []
primer_expert: This patch addresses an ASan error in `bfd/elf32-z80.c` within the
  `z80_elf_16_be_reloc` function.  The fix adds a bounds check using `bfd_reloc_offset_in_range`
  to ensure that relocation offsets are valid before proceeding.  This prevents out-of-bounds
  writes when processing crafted or corrupted Z80 ELF object files.
primer_general: This patch fixes a bug in the binary file descriptor (BFD) library,
  which is used by binutils to handle various object file formats.  Specifically,
  it addresses a potential memory corruption issue when linking or processing Z80
  ELF object files. The fix ensures that relocation offsets are within the valid range,
  preventing writes to invalid memory locations. This improves the robustness of binutils
  when dealing with potentially malformed input files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aen3u_6aPVWoRrRP@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-23'
---

A bug fix addresses a potential out-of-bounds write during relocation of Z80 ELF objects. The patch adds a sanity check to ensure the relocation offset is within the valid range before proceeding with the relocation.  This prevents a crash reported by the address sanitizer when processing a malformed object file.
