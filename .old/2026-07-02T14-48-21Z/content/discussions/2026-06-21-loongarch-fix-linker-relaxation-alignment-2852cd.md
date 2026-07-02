---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relaxation
- alignment
- binutils
discussion_id: 6f5dabdd8c73fd86d73c763f992b2add5485747d.camel@xry111.site
source_type: public_inbox
title: 'Re: [PATCH v1] LoongArch: Fix linker relaxation alignment'
headline: 'LoongArch: Fix linker relaxation alignment'
tldr: A patch for Binutils' LoongArch linker fixes issues where relaxation previously
  caused alignment problems when linking multiple objects, improving code generat…
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: ready
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Xi Ruoyao
  role: contributor
  position: Confirms that the proposed patch fixes insufficient alignment issues for
    `trampoline_code_table` in `libffi` on LoongArch.
  quote: I can confirm this fixes the insufficient alignment of trampoline_code_table
    in libffi.
primer_expert: This discussion pertains to the Binutils linker (`ld`) and the LoongArch
  architecture, specifically addressing linker relaxation in `bfd/elfnn-loongarch.c`.
  Linker relaxation optimizes code by shortening instructions or removing unnecessary
  padding within sections. The issue described is that `sec->output_offset` was updated
  in `loongarch_relax_pcala_addi` and `loongarch_relax_call36` without considering
  `align_power`, causing misalignment of sections when multiple objects are linked.
  The fix likely involves properly incorporating `align_power` into the `output_offset`
  calculation for relaxed…
primer_general: This is a technical discussion about a fix for a problem in the linker
  (a program that combines different parts of a compiled program) for computer systems
  using the LoongArch chip architecture. When the linker optimizes code (a process
  called 'relaxation'), it sometimes caused parts of the program, particularly those
  related to `libffi` (a library that helps programs call functions in different programming
  languages), to be misaligned. This misalignment could lead to incorrect program
  behavior. The confirmed patch ensures that the linker correctly aligns these program
  sections, making compiled programs for LoongArch more reliable and functional.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6f5dabdd8c73fd86d73c763f992b2add5485747d.camel@xry111.site
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This discussion confirms a patch that resolves linker relaxation alignment issues for the LoongArch architecture within Binutils. The original problem arose during the linking of multiple object files, where the linker's relaxation process failed to account for section alignment, leading to incorrect `output_offset` values. This fix specifically addresses insufficient alignment observed in `libffi`'s `trampoline_code_table`, ensuring that linker relaxation correctly maintains alignment. This improves the correctness and reliability of generated code for LoongArch systems.
