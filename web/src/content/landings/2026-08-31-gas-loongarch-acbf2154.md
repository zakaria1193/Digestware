---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- optimization
- assembler
- relocations
commit_hash: acbf21547ecc21e2cab7e9fc56633deefb207fe4
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Optimize TC_FORCE_RELOCATION_SUB_LOCAL'
tldr: LoongArch assembler optimizes relocation generation to avoid ADD/SUB relocations
  when possible.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit modifies `gas/config/tc-loongarch.c` to optimize the generation
  of `BFD_RELOC_32` and `BFD_RELOC_64` relocations for LoongArch. It refactors the
  `loongarch_force_relocation_sub_local` logic by removing it and instead directly
  optimizing fixups within `loongarch_force_relocation`. The goal is to emit PC-relative
  relocations when possible, avoiding ADD/SUB relocations when the distance to the
  symbol is small and no relaxable instructions are present, thereby improving code
  density and linker performance.
primer_glossary:
- term: relocation
  definition: A directive in object code that tells the linker how to modify certain
    instructions or data before the executable code can be run. This typically involves
    adjusting addresses or offsets to be correct in the final program image.
- term: PC-relative
  definition: An addressing mode where an address or offset is calculated relative
    to the current value of the program counter (PC). This is common for position-independent
    code.
- term: linker-relaxable instructions
  definition: Instructions that the linker can modify or substitute, often to optimize
    code size or performance. The linker can 'relax' these instructions, for example,
    by changing a generic jump to a more specific, shorter one.
- term: ADD/SUB relocations
  definition: Specific types of relocations used to encode the result of an addition
    or subtraction at link time. This commit aims to replace these with more efficient
    PC-relative relocations when applicable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260831081129.EDACF4BA23E1@sourceware.org
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

The LoongArch assembler now optimizes relocation generation for subtraction symbols relative to the PC. If no linker-relaxable instructions exist between the subtraction symbol and the PC, it changes the fixup to be PC-relative. This change avoids emitting ADD/SUB relocations, leading to more efficient code generation.
