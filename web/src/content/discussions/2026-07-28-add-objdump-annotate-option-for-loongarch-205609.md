---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- objdump
- loongarch
- disassembly
- annotations
discussion_id: 20260728104343.23106-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Add new option annotate for objdump'
headline: Add objdump annotate option for LoongArch
tldr: Introduces `objdump -dM annotate` for LoongArch to display disassembly with
  `dbar` instruction annotations.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch introduces a new display mode, `annotate`, to `objdump`
  for the LoongArch architecture. This mode is designed to provide specific annotations
  alongside the disassembly of `dbar` instructions. The `dbar` instruction is likely
  related to data cache coherency or management on LoongArch systems, and the annotations
  aim to clarify its usage and parameters directly in the object code listing.
primer_glossary:
- term: objdump
  definition: A utility that displays information from object files, including disassembly.
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China, used in
    various processors.
- term: dbar instruction
  definition: A specific instruction in the LoongArch architecture, likely related
    to data cache barrier operations or management.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260728104343.23106-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

A patch adds a new `annotate` option to `objdump` specifically for the LoongArch architecture. This enhancement allows users to view disassembly output that includes annotations for `dbar` instructions, providing more detailed information about their operands and behavior.
