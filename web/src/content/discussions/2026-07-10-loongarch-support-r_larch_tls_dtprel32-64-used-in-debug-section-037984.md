---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- tls
- relocation
- loongarch
- debugging
- binutils
discussion_id: 20260710033401.522212-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v3] LoongArch: Support R_LARCH_TLS_DTPREL32/64 used in debug section'
headline: 'LoongArch: Support R_LARCH_TLS_DTPREL32/64 used in debug section'
tldr: Simplify LoongArch TLS relocations in debug sections for better compatibility.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies relocation processing logic for improved maintainability.
- Ensures compatibility with LoongArch's RELA relocation model.
exchanges: []
primer_expert: This patch modifies `bfd/elfnn-loongarch.c` and related test files
  to correctly handle Thread-Local Storage (TLS) relocations, specifically `R_LARCH_TLS_DTPREL32/64`,
  when they appear within debug sections. The change simplifies the relocation processing
  logic and ensures the correct offset to the TLS block is returned. By setting `partial_inplace`
  to false, it aligns with LoongArch's use of RELA relocations, avoiding potential
  incompatibilities seen in previous compiler outputs where redundant addends were
  generated.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260710033401.522212-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This patch simplifies the processing of R_LARCH_TLS_DTPREL32/64 relocations within the debug sections on LoongArch systems. It aims to return the correct offset to the TLS block for symbols and sets partial_inplace to false, acknowledging that LoongArch uses RELA relocations. The changes are an iteration from previous versions, with adjustments to the `dtprel.d` file to remove addend values and improve clarity.
