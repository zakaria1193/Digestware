---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- optimization
- gas
commit_hash: 90a7bfab3c335c208392dfee449cca48d25e0d50
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Optimize alignment before linker-relaxable frags'
tldr: LoongArch GAS optimizes alignment of early fragments to avoid R_LARCH_ALIGN
  relocations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit modifies GAS for LoongArch to optimize alignment fragments
  that appear before the first linker-relaxable fragment. It converts rs_machine_dependent
  alignment frags to rs_align_code frags, enabling GAS to emit precise NOP padding
  and avoid R_LARCH_ALIGN relocations. The optimization is guarded by checks for R_LARCH_RELAX
  relocations and ensures correct handling of linker relaxation.
primer_glossary:
- term: linker-relaxable frag
  definition: A fragment of code or data within an object file that the linker can
    modify or adjust its position after the initial linking pass, typically to optimize
    alignment or instruction encoding.
- term: R_LARCH_ALIGN
  definition: A relocation type specific to LoongArch that indicates an alignment
    adjustment is needed at a particular address.
- term: NOP padding
  definition: The insertion of No-Operation (NOP) instructions to fill space, often
    used for alignment purposes or to ensure predictable instruction timing.
- term: size_seg
  definition: A phase in the linker or assembler process where the final sizes and
    addresses of code and data segments are determined.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260927090901.77A364BA79BF@sourceware.org
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

LoongArch GAS now converts initial alignment fragments into ordinary align-code fragments, allowing GAS to compute exact NOP padding. This avoids unnecessary R_LARCH_ALIGN relocations for these early alignments. The optimization is skipped if any .reloc *, R_LARCH_RELAX is present, as the exact linker-relaxable fragment cannot be determined prior to size_seg. The sec_flg1 flag is refreshed after this optimization.
