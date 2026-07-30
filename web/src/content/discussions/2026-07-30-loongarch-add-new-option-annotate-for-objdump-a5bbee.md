---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- objdump
- loongarch
- disassembly
discussion_id: 20260730021453.50476-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Add new option annotate for objdump'
headline: 'LoongArch: Add new option annotate for objdump'
tldr: Adds 'objdump -dM annotate' to display disassembly with annotations for LoongArch
  dbar instructions.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch adds a new disassembly annotation option to objdump for
  the LoongArch architecture. The 'annotate' mode specifically targets 'dbar' instructions,
  providing meta-information about their operands or behavior during disassembly.
primer_glossary:
- term: objdump
  definition: A utility that displays information from object files, including disassembly
    of machine code.
- term: LoongArch
  definition: A RISC-ISA instruction set architecture developed in China.
- term: dbar
  definition: Likely refers to a specific instruction in the LoongArch architecture,
    possibly related to data buffering or synchronization.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260730021453.50476-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This patch introduces a new 'annotate' option for the LoongArch objdump tool. When used with '-dM annotate', it will display disassembly along with specific annotations for 'dbar' instructions, providing more detailed insight into their usage and behavior.
