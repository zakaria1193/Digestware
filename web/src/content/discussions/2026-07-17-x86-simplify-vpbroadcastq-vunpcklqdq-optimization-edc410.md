---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- AVX
- optimization
- instruction selection
discussion_id: ac3b0417-f5b7-4297-9cfa-46e1b951c324@suse.com
source_type: public_inbox
title: '[PATCH 1/3] x86: slightly simplify VPBROADCASTQ -> VUNPCKLQDQ optimization
  again'
headline: 'x86: Simplify VPBROADCASTQ -> VUNPCKLQDQ optimization.'
tldr: Fixes an overzealous check in the x86 assembler's VPBROADCASTQ optimization.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Corrects a functional bug in instruction optimization.
- Improves the accuracy of instruction selection for AVX instructions.
exchanges: []
primer_expert: Refines the x86 assembler's optimization for transforming `VPBROADCASTQ`
  to `VUNPCKLQDQ`. A previous commit incorrectly added a check for the `xmmword` property
  on the first operand (`i.op[0]`). This patch removes that redundant check, as it
  was only necessary to ensure the second operand is an `xmmword`, thereby allowing
  more correct transformations.
primer_glossary:
- term: VPBROADCASTQ
  definition: An x86 AVX instruction that broadcasts a 64-bit integer value to all
    elements of a 128-bit XMM register.
- term: VUNPCKLQDQ
  definition: An x86 AVX instruction that unpacks packed low quadwords from two XMM
    registers.
- term: optimization
  definition: The process of modifying code to improve its efficiency, such as speed
    or size.
- term: x86 assembler
  definition: The part of binutils that processes x86 assembly language code, translating
    it into machine code.
series_id: 'binutils:x86: slightly simplify vpbroadcastq -> vunpcklqdq optimization
  again'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ac3b0417-f5b7-4297-9cfa-46e1b951c324@suse.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch corrects an optimization in the x86 assembler related to the `VPBROADCASTQ` instruction. It removes an unnecessary check for the `xmmword` property on the source operand, which was overly strict and incorrectly disabled valid transformations. The fix ensures that the optimization correctly identifies when `VPBROADCASTQ` can be transformed into `VUNPCKLQDQ`.
