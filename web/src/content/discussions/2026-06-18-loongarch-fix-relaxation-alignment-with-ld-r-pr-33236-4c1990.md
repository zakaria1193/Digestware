---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- alignment
- relaxation
- ld -r
discussion_id: 20260618070155.1339292-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Fix relaxation alignment with ld -r (PR 33236)'
headline: 'LoongArch: Fix relaxation alignment with ld -r (PR 33236)'
tldr: This patch fixes section misalignment issues in LoongArch when using `ld -r`
  due to linker relaxation, by adding alignment sections and relocations and adjusti…
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds new alignment sections and relocations, potentially increasing object file
  size slightly.
- Changes basic linker behavior for `ld -r` on LoongArch, requiring careful testing
  to avoid regressions in other scenarios.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes a fix for LoongArch relaxation alignment issues when using `ld
    -r` by adding alignment sections and relocations, and adjusting section alignment.
    The updated patch removes changes in `ldlang.c` and prevents `ldlang.c:size_input_section`
    padding by modifying the input section's alignment power.
  quote: To fix this, add an align section and an align relocation before each section
    when ld -r. And change the section alignment to 4 to disable the default section
    start address calculation.
primer_expert: The `ld -r` option creates a relocatable output file that can be used
  as input for another `ld` run. On LoongArch, during this intermediate linking step,
  instruction relaxation can alter section sizes. The problem arises when `ld` does
  not account for these size changes when calculating section offsets, leading to
  misaligned sections. This patch extends `bfd/elfnn-loongarch.c` and `ld/emultempl/loongarchelf.em`
  to explicitly manage alignment during relaxation, similar to practices in `ld.lld`,
  by inserting NOPs and adjusting the `alignment_power` to ensure correct section
  placement and preven…
primer_general: This patch addresses an issue in the linker, `ld`, specifically for
  the LoongArch processor architecture. The linker is a program that combines different
  pieces of compiled code (object files) into a single executable or library. When
  `ld` is used with the `-r` option, it performs an intermediate link, producing another
  object file. During this process, the linker sometimes optimizes code instructions,
  a process called "relaxation," which can change the size of code segments. If the
  linker doesn't properly account for these size changes, subsequent code segments
  might start at incorrect memory addresses, leading to performance issues or program
  crashes. This fix ensures that even after these optimizations, all code segments
  maintain their correct alignment, which is crucial for the processor to efficiently
  access data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260618070155.1339292-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-06-18'
is_stub: false
---

This proposal addresses a known issue in the LoongArch linker where section alignment is not correctly maintained during relaxation when linking with `ld -r`. The current behavior can lead to subsequent sections being misaligned if preceding sections undergo relaxation. The proposed fix introduces alignment sections and relocations before each section, and modifies the section alignment to explicitly disable default start address calculations, mirroring fixes implemented in `ld.lld`.
