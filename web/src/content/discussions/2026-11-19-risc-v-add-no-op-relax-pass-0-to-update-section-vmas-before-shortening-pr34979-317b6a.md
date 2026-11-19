---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relocations
- optimization
- elf
discussion_id: CA+yXCZCq9v-ORh4uS_mZeDbO+bKv_qBYsWKHDOb4O9b2VRgXyw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: Add no-op relax pass 0 to update section VMAs before
  shortening [PR34979]'
headline: 'RISC-V: Add no-op relax pass 0 to update section VMAs before shortening
  [PR34979]'
tldr: Introduces a no-op relax pass to consistently update section VMAs before shortening,
  fixing overflow errors in RISC-V code generation.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Ready to Land
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introduces a new relax pass, adding a small overhead to the linker's initialization
  phase for RISC-V targets.
- Solves a correctness issue (relocation overflow) by ensuring consistent VMA updates,
  which is critical for correct code generation.
exchanges:
- author: Zhuo Zhi
  role: proposer
  position: Proposes adding a no-op relax pass to address a VMA discrepancy during
    section relaxation in the RISC-V linker.
  quote: 'When ldelf_map_segments invokes lang_relax_sections (true) after either
    bfd_elf_discard_info edits .eh_frame or bfd_elf_map_sections_to_segments increases
    elf_program_header_size (growing SIZEOF_HEADERS), lang_size_sections_1 walks the
    linker script top-down and updates each output section''s VMA immediately before
    invoking bfd_relax_section on its input sections.


    As a result, when relaxing an ea…'
- author: Kito Cheng
  role: reviewer
  position: Approves the patch, noting that a simple dummy relax pass elegantly solves
    the issue, and has pushed the fix to trunk.
  quote: 'Thanks for the patch, v2 is LGTM,

    although I am little suppress that could be fixed by adding a dummy

    relax pass :P

    Verified on my local, pushed to trunk :)'
primer_expert: This addresses a specific issue in the RISC-V linker where changes
  to ELF program headers (specifically, `SIZEOF_HEADERS`) can shift output section
  VMAs inconsistently during relaxation passes. The core problem is that a later section's
  VMA might not be updated before an earlier section that references it is relaxed,
  leading to incorrect PC-relative offset calculations and relocation overflows. The
  fix introduces a new, no-op `riscv_relax_pass_layout` at pass 0 to ensure all VMAs
  are synchronized before any shortening or relocation occurs.
primer_glossary:
- term: VMA
  definition: Virtual Memory Address. The address where a section or symbol resides
    in the program's virtual address space.
- term: Section
  definition: A part of an object file or executable, typically containing code (.text),
    initialized data (.data), or uninitialized data (.bss).
- term: Relaxation
  definition: A linker optimization pass that adjusts instruction encodings or addresses
    after initial layout, often to optimize for size or to fix relocations that couldn't
    be resolved immediately.
- term: PC-relative offset
  definition: An offset from the current instruction's Program Counter to a target
    address. Used for efficient branching and data access.
- term: R_RISCV_JAL
  definition: A RISC-V relocation type for the JAL (Jump and Link) instruction, indicating
    that the target address needs to be resolved.
- term: SIZEOF_HEADERS
  definition: The total size of the ELF header and program headers in an executable
    or shared object. An increase in this value shifts subsequent sections.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZCq9v-ORh4uS_mZeDbO+bKv_qBYsWKHDOb4O9b2VRgXyw@mail.gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch introduces a no-op relax pass at pass 0 in the RISC-V linker relaxation initialization. This ensures that all output section VMAs are consistently updated before the shortening pass, preventing a discrepancy where earlier sections have new VMAs while later sections have stale ones. This resolves an issue where the relaxation pass could underestimate PC-relative offsets, leading to overflow errors like R_RISCV_JAL.
