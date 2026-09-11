---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- assembler
- GAS
- relocation
- alignment
discussion_id: 20260910092253.526336-4-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 3/3] LoongArch: Resolve alignment before first linker-relaxable frag'
headline: 'LoongArch: Optimize alignment before first relaxable frag'
tldr: Optimizes alignment handling in LoongArch by converting early alignment frags
  to non-relaxable ones.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reduces the number of R_LARCH_ALIGN relocations, potentially improving link times
  and code density.
- Adds complexity to the alignment handling logic, with a fallback for R_LARCH_RELAX.
- May affect custom linker scripts if they rely on the exact placement of R_LARCH_ALIGN.
exchanges: []
primer_expert: This patch modifies the LoongArch GAS backend to optimize alignment
  handling. Specifically, it targets `rs_machine_dependent` alignment frags that precede
  any linker-relaxable frags. These early alignment frags are converted to `rs_align_code`
  frags, allowing GAS to calculate precise NOP padding at assembly time. This eliminates
  the need for `R_LARCH_ALIGN` relocations for these initial alignments, as the final
  layout is fixed. If `R_LARCH_RELAX` relocations are present, this optimization is
  disabled because the true relaxable state isn't known until after `size_seg`. Section
  flags are refres…
primer_glossary:
- term: linker-relaxable
  definition: A code fragment or instruction whose size or position can be adjusted
    by the linker during the relaxation phase to optimize code density or performance.
- term: rs_machine_dependent
  definition: Represents a machine-dependent fragment type within the GAS assembler,
    often related to specific instruction or alignment semantics for a target architecture.
- term: rs_align_code
  definition: An assembler fragment type representing an alignment directive, which
    ensures that subsequent code or data is placed at a properly aligned address.
- term: R_LARCH_ALIGN
  definition: A LoongArch relocation type specifically used to indicate that an alignment
    adjustment is required.
- term: NOP padding
  definition: Insertion of No-Operation (NOP) instructions to fill space, often used
    for alignment purposes or to provide space for later patching.
series_id: 'binutils:loongarch: resolve alignment before first linker-relaxable frag'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910092253.526336-4-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch optimizes alignment handling for LoongArch by converting alignment fragments that appear before the first linker-relaxable instruction into ordinary, non-linker-relaxable alignment fragments. This allows the assembler (GAS) to compute the exact NOP padding, thus avoiding the emission of R_LARCH_ALIGN relocations. Alignments that appear later remain linker-relaxable. The optimization is skipped if any R_LARCH_RELAX relocations are present, as the exact relaxable fragment cannot be determined before final addresses are known. The patch also refreshes section flags after optimization.
