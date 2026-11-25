---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- binutils
- linker
- assembler
commit_hash: 7b17b2c03057d5c5eb425fecc890e3f88cc3a64b
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Treat RISC-V R_RISCV_ALIGN as relaxable
tldr: Binutils now treats R_RISCV_ALIGN relocations as relaxable for RISC-V, improving
  linker behavior.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the RISC-V backend in Binutils (`gas`) to mark
  `R_RISCV_ALIGN` relocations as relaxable. In `gas/config/tc-riscv.c`, the `riscv_frag_align_code`
  function now sets `info->last_relax = true;` after emitting an `R_RISCV_ALIGN` relocation.
  This is crucial because an `R_RISCV_ALIGN` can alter the size of a section. Even
  in contexts where preceding instructions are not relaxable, the linker might need
  to adjust section boundaries. By marking the alignment as relaxable, the linker
  is informed that subsequent relaxations might depend on this alignment, ensuring
  correct behavior f…
primer_glossary:
- term: R_RISCV_ALIGN
  definition: A relocation type specific to RISC-V that indicates a required alignment
    for a section or symbol. The linker uses this information to adjust code placement.
- term: relaxable
  definition: In the context of linkers and assemblers, 'relaxable' refers to instructions
    or relocations whose size or position can be adjusted by the linker after initial
    assembly. This allows for optimizations like instruction compression or better
    code positioning.
- term: relocation
  definition: Information in an object file that tells the linker how to modify addresses
    in the code or data sections to correctly reference symbols defined elsewhere.
    Relocation entries specify the type of fix-up needed and the location to apply
    it.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261125100031.94E344716437@sourceware.org
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit updates the RISC-V assembler in Binutils to treat `R_RISCV_ALIGN` relocations as relaxable. This change ensures that the linker can correctly handle alignment changes, even in non-relaxable code sections, by allowing the `R_RISCV_ALIGN` to influence section size adjustments. Previously, the assembler might not have marked these as relaxable, potentially leading to alignment issues when the linker needed to modify section sizes after instructions that were not themselves relaxable.
