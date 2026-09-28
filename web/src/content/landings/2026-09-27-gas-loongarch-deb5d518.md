---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- gas
- linker
- relocation
- dwarf
commit_hash: deb5d51883d7d6659e08a5b8e3a7d1ca769e0684
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Mark .reloc *, R_LARCH_RELAX target frags correctly'
tldr: LoongArch GAS now correctly marks fragments with R_LARCH_RELAX for linker relaxation.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit enhances LoongArch GAS to correctly handle fragments marked
  with `.reloc *, R_LARCH_RELAX`. Previously, GAS did not track this linker-relaxable
  state in the containing frag and section, leading to incorrect assumptions about
  fixed distances and the generation of invalid relocations (e.g., converting symbol
  subtraction to PC-relative) or DWARF line table entries. The fix introduces marking
  these frags as linker-relaxable via `tc_frob_file_before_fix` after `size_seg` and
  adjusts relocation and DWARF emission accordingly.
primer_glossary:
- term: .reloc *, R_LARCH_RELAX
  definition: An assembler directive and relocation type for LoongArch that marks
    a specific code or data fragment as subject to linker relaxation. The linker may
    adjust the fragment's size or position.
- term: linker relaxation
  definition: A linker optimization technique where the linker can adjust the size
    and position of certain code or data segments after an initial linking pass to
    improve code density or enable specific instruction encodings.
- term: PC-relative relocation
  definition: A type of relocation where an address is specified relative to the current
    Program Counter (PC), commonly used for position-independent code.
- term: DWARF line tables
  definition: A debugging data format that maps executable code addresses back to
    source code lines, enabling source-level debugging.
- term: DW_LNS_fixed_advance_pc
  definition: A specific DWARF line table instruction that advances the program counter
    by a fixed amount, used to represent code sequencing in the debugger.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260927090856.5BF9A4BA799D@sourceware.org
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

LoongArch GAS now properly identifies and marks fragments containing .reloc *, R_LARCH_RELAX, indicating they are linker-relaxable. This prevents GAS from incorrectly treating distances between symbols within these frags as fixed, which could lead to inappropriate PC-relative relocations or DWARF line table issues. The change ensures that same-frag symbol subtraction uses ADD/SUB relocs and forces DW_LNS_fixed_advance_pc in DWARF line tables when R_LARCH_RELAX is present.
