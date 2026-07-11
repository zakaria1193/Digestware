---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- gas
- relocations
- optimization
commit_hash: 4fec67921a8c11700dff6db1c8b6ad9255c59254
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Avoid relocation for addsy/subsy within the same fragment'
tldr: Optimizes LoongArch assembler by skipping relocations when addsy and subsy fall
  within the same fragment, reducing object file size.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The change in `gas/config/tc-loongarch.c` adds a `linker_relax` flag
  to the `loongarch_cl_insn` struct. The core logic update prevents the emission of
  a relocation if both `addsy` and `subsy` directives fall within the same fragment.
  This is achieved by checking that relaxed instructions and alignment nops are placed
  within the same fragment, thereby simplifying the relocation calculation for symbol
  arithmetic. This optimization aims to reduce the overhead associated with relocations
  when the calculation operands are locally contained.
primer_glossary:
- term: addsy
  definition: An assembler directive used in LoongArch GAS to indicate the start of
    a symbol arithmetic expression, often involving labels. It's part of calculating
    relocations.
- term: subsy
  definition: An assembler directive used in LoongArch GAS, typically paired with
    'addsy', to complete a symbol arithmetic expression. Together, they define the
    operands for a relocation.
- term: Fragment
  definition: A contiguous sequence of code or data within an object file that the
    assembler or linker treats as a unit. Relocations are often associated with fragments.
- term: Relocation
  definition: Information in an object file that tells the linker how to adjust addresses
    or symbols to their final locations in memory.
- term: Linker-relaxable instructions
  definition: Instructions whose final encoding might be determined or adjusted by
    the linker, often involving branch offsets or immediate values that depend on
    the final layout of the code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260710070142.E6BF94BA2E0B@sourceware.org
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This commit enhances the LoongArch assembler's efficiency by preventing unnecessary relocations when `addsy` and `subsy` directives appear within the same code fragment. It refines the handling of linker-relaxable instructions and alignment no-operation (nop) instructions, ensuring they coexist within a single fragment. By doing so, the assembler avoids generating a relocation when the operands for symbol arithmetic are contained entirely within one fragment, leading to cleaner object files.
