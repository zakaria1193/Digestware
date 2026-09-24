---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- patch
- loongarch
- disassembler
- internationalization
discussion_id: 20260924022722.55003-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Fix non-ASCII string in disassemble_annotate_one function'
headline: 'LoongArch: Fix non-ASCII string in disassemble_annotate_one function'
tldr: Fixes non-ASCII characters in comments within the LoongArch disassembler.
proposer: zhaozhou
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies comments in `opcodes/loongarch-dis.c` to replace
  non-ASCII hyphens ('-') with standard ASCII hyphens. The affected comments are part
  of the annotation layout description for the `dbar` instruction. The change ensures
  that the source code is clean and compatible with ASCII-based parsing tools.
primer_glossary:
- term: LoongArch
  definition: An instruction set architecture (ISA) developed by Loongson Technology,
    primarily for use in China.
- term: disassembler
  definition: A program that translates machine code (binary instructions) back into
    a human-readable assembly language format.
- term: dbar
  definition: Likely refers to a specific instruction or a type of barrier in the
    LoongArch architecture, possibly related to memory ordering or synchronization.
- term: annotate
  definition: To add explanatory notes or comments to code or data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924022722.55003-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the LoongArch disassembler by fixing multiple non-ASCII '-' characters found in comments within the `disassemble_annotate_one` function. The changes involve replacing these characters to ensure correct display and avoid potential issues with tools that parse source code.
