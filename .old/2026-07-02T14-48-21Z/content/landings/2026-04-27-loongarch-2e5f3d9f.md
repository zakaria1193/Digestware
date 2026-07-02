---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- alignment
- assembler
commit_hash: 2e5f3d9f0596e60031d7c56cf943cf00e81fe53d
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Enforce 4-byte alignment for machine instructions.'
tldr: The LoongArch backend in GNU assembler now enforces 4-byte alignment for machine
  instructions to prevent instruction fetch errors.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GNU assembler's LoongArch backend (`gas/config/tc-loongarch.c`)
  now calls `record_alignment (now_seg, 2)` when emitting instructions to enforce
  4-byte alignment. This prevents instruction fetch errors that can occur when linking
  object files where alignment wasn't explicitly specified. A new test case (`gas/testsuite/gas/loongarch/insn_align_4.s`)
  validates this.
primer_general: The GNU assembler (gas) translates assembly code into machine code.  LoongArch
  is a RISC instruction set architecture (ISA).  This change ensures that LoongArch
  instructions are aligned on 4-byte boundaries in the assembled output.  Unaligned
  instructions can cause crashes or performance problems on some architectures, as
  the CPU may only fetch instructions from aligned addresses. The assembler must take
  care to insert padding bytes when necessary to maintain alignment.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260427092631.F286E4B99F58@sourceware.org
date: '2026-04-27'
---

The LoongArch backend in GNU assembler now enforces 4-byte alignment for machine instructions. This ensures that instructions are properly aligned when linked into executables or shared objects, even when no explicit alignment is specified in the assembly source.  Without this, instruction fetch errors may occur, especially when generating shared objects with the `-nostdlib` option.
