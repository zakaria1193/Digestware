---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- loongarch
- relocation
- kernel
- binutils
discussion_id: 20260714155352.83544-1-xry111@xry111.site
source_type: public_inbox
title: 'LoongArch: only insert align section for ld -r if an input has R_LARCH_ALIGN
  or R_LARCH_RELAX'
headline: 'LoongArch: only insert align section for ld -r if an input has R_LARCH_ALIGN
  or R_LARCH_RELAX'
tldr: Fixes LoongArch linker behavior when using `ld -r` to avoid inserting align
  sections unnecessarily, preventing kernel module loading issues.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Conditionally inserting align sections reduces output bloat and resolves compatibility
  issues with environments expecting specific relocation behaviors.
- Balancing linker flexibility with strict requirements from environments like the
  Linux kernel module loader.
exchanges: []
primer_expert: This patch addresses a regression in LoongArch's `ld -r` (relocatable
  linking) behavior. Specifically, it corrects the creation of an align section that
  was previously inserted unconditionally. The issue reported is that this unconditional
  insertion breaks kernel modules built with `-mno-relax`, as they expect no R_LARCH_ALIGN
  relocations. The fix is to condition the align section's creation on the presence
  of R_LARCH_ALIGN or R_LARCH_RELAX relocations in the input object files.
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA (Instruction Set Architecture) developed in China.
- term: ld -r
  definition: A linker option that performs a partial link, combining multiple object
    files into a single relocatable object file.
- term: R_LARCH_ALIGN
  definition: A LoongArch-specific relocation type that indicates byte alignment.
- term: R_LARCH_RELAX
  definition: A LoongArch-specific relocation type used for relaxation, potentially
    allowing for code or data removal.
- term: -mno-relax
  definition: A compiler flag that disables instruction relaxation, which can affect
    code size and performance but might be required by certain linkers or environments.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260714155352.83544-1-xry111@xry111.site
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Xi Ruoyao proposes a fix to the LoongArch linker's behavior with `ld -r`. A previous change inadvertently caused issues with Debian kernel modules because the linker was inserting align sections even when not explicitly required by R_LARCH_ALIGN or R_LARCH_RELAX relocations. This patch ensures the align section is only inserted when such relocations are present, resolving the kernel module loading problem and preventing unnecessary bloat from NOPs and align sections.
