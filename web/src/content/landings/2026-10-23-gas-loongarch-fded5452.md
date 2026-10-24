---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocation
- relaxation
commit_hash: fded5452c53ed187bad8295aca3310b1376199b6
source_type: public_inbox
author: mengqinggang <mengqinggang@loongson.cn>
headline: Emit LoongArch relocations after .option norelax
tldr: LoongArch assembler now emits relocations for relaxed fragments even when relaxation
  is disabled.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes an issue in `gas/config/tc-loongarch.c` where `_loongarch_force_relocation_sub_same`
  incorrectly returned `false` when `LARCH_opts.relax` was disabled, preventing the
  emission of necessary relocations for fragments that would have been relaxed. The
  check on `LARCH_opts.relax` is removed, and the decision to emit a relocation now
  correctly depends on whether the section contains relaxable fragments (`sec->sec_flg1`).
  New tests for relax-local-branch are added.
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed by Loongson Technology.
- term: relocation
  definition: Information in an object file that tells the linker how to modify certain
    instructions or data when combining multiple object files or loading a program.
    It specifies addresses, symbols, and types of fixups needed.
- term: assembler
  definition: A program that converts assembly language source code into machine code
    that a computer can execute.
- term: gas
  definition: The GNU Assembler, part of the binutils package, responsible for converting
    assembly code into machine code.
- term: .option norelax
  definition: An assembler directive that disables instruction relaxation, a process
    where the assembler may adjust instruction lengths or offsets for optimization.
- term: fragment
  definition: A piece of code or data within an assembly file that the assembler processes.
    Relaxable fragments are those that the assembler might modify (e.g., in length
    or offset) during relaxation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261023071145.0DBAB4BA23D6@sourceware.org
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

This patch corrects the LoongArch assembler's behavior regarding relocations when the `.option norelax` directive is active. Previously, the assembler incorrectly omitted relocations that spanned a relaxed fragment if relaxation was disabled. The fix ensures these relocations are emitted by removing an overly strict check in `_loongarch_force_relocation_sub_same` and instead basing the decision on the relocation's coverage of a relaxable fragment.
