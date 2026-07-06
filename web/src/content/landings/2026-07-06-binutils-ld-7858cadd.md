---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- binutils
- ld
- loongarch
- linker
- alignment
commit_hash: 7858cadd335b3ffbc8e0250c0c180253d9f09489
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Fix linker relaxation alignment'
tldr: LoongArch linker correctly updates section output offsets during relaxation
  to maintain alignment.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bfd/elfnn-loongarch.c` file is updated to fix how linker relaxation
  affects section alignment. The problematic lines that unconditionally updated `sec->output_offset`
  without accounting for alignment have been removed. Instead, the `align_power` function
  (or similar alignment logic) is implicitly or explicitly relied upon to manage the
  `output_offset` correctly, ensuring that sections remain properly aligned after
  relaxation, even when linking multiple objects.
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China.
- term: linker relaxation
  definition: A linker optimization technique where the linker adjusts instruction
    offsets for branches and calls after the initial pass, potentially improving code
    density or enabling features like Position-Independent Code (PIC).
- term: output_offset
  definition: The offset of a section within its output section in the final linked
    object or executable.
- term: align_power
  definition: A function or mechanism within the linker that ensures a memory address
    or section is aligned to a power of two boundary.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260706061304.155864BA2E0A@sourceware.org
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

This commit resolves alignment issues in the LoongArch linker related to relaxation. Previously, the `output_offset` of a section was updated during relaxation without considering alignment requirements. The fix ensures that the `output_offset` is correctly updated by the `align_power` function, thus preserving section alignment.
