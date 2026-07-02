---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- relaxation
- alignment
discussion_id: 20260624061128.3917927-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v3] LoongArch: Fix relaxation alignment with ld -r (PR 33236)'
headline: LoongArch linker fix for `ld -r` relaxation alignment issues
tldr: This patch for Binutils fixes section misalignment on LoongArch when using `ld
  -r` and linker relaxation, a problem also seen on RISC-V.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Adding align sections and relocations might slightly increase the size of relocatable
  object files, but this is a necessary overhead to ensure correct alignment after
  relaxation.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to fix linker relaxation alignment issues for LoongArch in `ld
    -r` mode by adding align sections and relocations, similar to a fix implemented
    in ld.lld for RISC-V.
  quote: To fix this, add an align section and an align relocation before each section
    when ld -r. And change the section alignment to 4 to disable the default section
    start address calculation.
primer_expert: GNU `ld` (the linker in Binutils) for LoongArch, when performing relocatable
  linking (`ld -r`), faces an issue with section alignment, mirroring a problem previously
  encountered with RISC-V (PR 33236). This occurs because linker relaxation (a process
  where the linker re-optimizes code usually by shortening immediate operands or branches
  based on their final addresses) can change the size of sections. If a preceding
  relaxed section shrinks, and a subsequent section is not properly aligned, it can
  lead to misaligned code or data. The proposed fix involves inserting special 'align
  sections' and…
primer_general: When you compile a program, the compiler creates "object files," which
  are like building blocks. A tool called the "linker" (`ld`) then stitches these
  object files together to create a final executable. One of the linker's jobs is
  to arrange these blocks (called "sections") in memory and make sure they start at
  the correct memory addresses, a process called "alignment." This proposal fixes
  a problem in the linker for a new computer architecture called LoongArch. When the
  linker is asked to produce an intermediate linked file (`ld -r` mode), and it also
  tries to optimize the size of sections (called "relaxation"), it can sometimes miscalculate
  where the next section should begin. This results in parts of the program starting
  at the wrong memory address, which can cause the program to crash or behave unexpectedly.
  The solution involves telling the linker to always insert small padding sections
  and special markers to ensure everything stays perfectly aligned, even after optimizations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260624061128.3917927-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-06-24'
is_stub: false
---

This patch (v3) addresses a known issue (PR 33236) in Binutils' `ld -r` linker mode where section alignment can break on LoongArch. Similar to RISC-V, if previous sections are relaxed, a subsequent section might become misaligned. The proposed fix involves inserting an align section and a corresponding relocation before each section, and setting the section alignment to 4 in `ld -r` mode to disable default alignment calculations. This aims to prevent misaligned sections, especially when sections undergo size changes during relaxation.
