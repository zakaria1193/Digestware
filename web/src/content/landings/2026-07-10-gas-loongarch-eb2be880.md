---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- gas
- relocations
- optimization
commit_hash: eb2be880c89506ddc619af484121df1c9538e8e8
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Reduce relocations for label subtraction with no relaxed instructions'
tldr: Optimizes LoongArch assembly by avoiding unnecessary relocations for label subtractions
  when no relaxed instructions are involved.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The commit updates `gas/config/tc-loongarch.c` and related files to
  add flags (`linker_relax` in `loongarch_cl_insn`, and a flag for sections) that
  track whether a fragment or section contains linker-relaxable instructions. The
  core change is in how `addsy` and `subsy` handle relocations: if `addsy` and `subsy`
  are within the same fragment, and that fragment does not contain any relaxed instructions,
  a relocation is no longer emitted. This reduces the number of relocations generated
  for simple label arithmetic when relaxation is not a factor.'
primer_glossary:
- term: Label Subtraction
  definition: An operation in assembly language where the addresses of two labels
    are subtracted from each other. This is often used to calculate the size or distance
    between two points in the code or data.
- term: Relocations
  definition: Information in an object file that tells the linker how to modify certain
    instructions or data references to point to the correct final memory addresses
    after linking.
- term: Relaxed Instructions
  definition: Instructions whose final machine code encoding (e.g., branch offsets,
    immediates) is not known at assembly time and may change during linking. The linker
    'relaxes' these instructions by patching them to their final form.
- term: addsy
  definition: An assembly directive or pseudo-instruction used in some assemblers
    (like GAS for LoongArch) to indicate the start of a section involved in symbol
    arithmetic, potentially related to relocations.
- term: subsy
  definition: Similar to 'addsy', this directive likely marks the end or a component
    of symbol arithmetic, working in conjunction with 'addsy' to define the operands
    for a relocation calculation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260710070148.108EF4BA2E09@sourceware.org
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This change introduces optimizations for LoongArch assembly by intelligently managing relocations related to label subtraction. It marks fragments and sections to indicate the presence of relaxed instructions. Consequently, if no relaxed instructions exist between `addsy` and `subsy` operations, the assembler now avoids emitting unnecessary relocations, leading to smaller object files and potentially faster linking times.
