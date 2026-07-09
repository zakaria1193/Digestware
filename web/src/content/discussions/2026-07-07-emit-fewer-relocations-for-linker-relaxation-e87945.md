---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- LoongArch
- relaxation
- relocations
discussion_id: 20260707174719.1883721-1-mengqinggang@loongson.cn
source_type: public_inbox
title: Emit fewer relocations for linker relaxation
headline: Emit fewer relocations for linker relaxation
tldr: Series aims to reduce relocation emissions during linker relaxation on LoongArch.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential for increased code density by reducing relocation overhead.
- Ensuring correctness of relaxation behavior across various instruction and relocation
  types.
exchanges: []
primer_expert: This series targets the GNU linker's relaxation capabilities for the
  LoongArch architecture. It refactors gas/config/tc-loongarch.c and related files
  to emit fewer relocations by optimizing how symbolic addresses and alignment requirements
  are handled. Specifically, it addresses TLS descriptor relocations and conditions
  under which subtractions of labels are handled to avoid unnecessary relocation entries.
primer_glossary: []
series_id: binutils:emit fewer relocations for linker relaxation
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This series introduces changes to the LoongArch backend for the GNU linker, aiming to reduce the number of relocations generated during the linker relaxation process. By optimizing relocation handling for label subtraction and alignment, the changes seek to improve code density and potentially performance. The series contains four patches, with the first addressing TLS descriptor relocation sizes.
