---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- relaxation
- alignment
- output_offset
discussion_id: 20260618062910.972814-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v1] LoongArch: Fix linker relaxation alignment'
headline: 'LoongArch: Fix linker relaxation alignment'
tldr: This patch fixes linker relaxation causing misalignment by updating section
  output_offset with correct alignment power.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Changes the calculation of `output_offset` during relaxation, which needs thorough
  testing to ensure it does not introduce new issues or regressions.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to fix alignment issues caused by linker relaxation on LoongArch
    by updating the `output_offset` to correctly use `align_power`.
  quote: Input section's output_offset is updated in relaxation without considering
    section alignment. Update section output_offset by align_opwer.
primer_expert: In the LoongArch `bfd` backend, specifically `bfd/elfnn-loongarch.c`,
  the `output_offset` for an input section within an output section is critical for
  correct linking. When linker relaxation occurs, the size of instructions can change,
  which in turn affects the `output_offset` of subsequent sections. The issue described
  is that the `sec->output_offset` update during relaxation currently neglects the
  `alignment_power` of the section, leading to incorrect placement. The proposed fix
  integrates the `alignment_power` into the `output_offset` calculation to ensure
  proper section alignment after r…
primer_general: This discussion is about a problem within the linker (`ld`) for computers
  using the LoongArch processor. The linker combines different pieces of compiled
  code into a single program. One of its jobs is "relaxation," where it optimizes
  machine instructions, sometimes making them shorter. When this happens, the size
  of a section of code can change. If the linker doesn't properly adjust the starting
  position (called `output_offset`) of the next section of code to account for this
  size change and also consider the required memory alignment (e.g., forcing a section
  to start at a memory address that's a multiple of 4 or 8), then the subsequent code
  might be placed at an incorrect memory address, which can lead to errors or slower
  performance. This patch aims to make sure the linker always places code sections
  at the correct, aligned memory addresses, even after relaxation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260618062910.972814-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-06-18'
is_stub: false
---

This proposal addresses an issue where linker relaxation on LoongArch can cause alignment problems when linking multiple object files. The current implementation updates an input section's `output_offset` during relaxation without properly considering section alignment, leading to potential misalignments. The patch aims to correct this by modifying how `output_offset` is calculated to factor in the `align_power` property.
