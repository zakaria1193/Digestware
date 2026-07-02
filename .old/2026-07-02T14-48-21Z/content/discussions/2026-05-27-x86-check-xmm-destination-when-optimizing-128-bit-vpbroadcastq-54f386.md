---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- optimization
- VPBROADCASTQ
- AVX2
discussion_id: CAMe9rOqa0uyxS_U2eQYQxZYsDx+_srnsLrZ7f72Y4hxkCjpVvA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] x86: Check XMM destination when optimizing 128-bit VPBROADCASTQ'
headline: 'x86: Check XMM destination when optimizing 128-bit VPBROADCASTQ'
tldr: Fixes a bug where 256-bit VPBROADCASTQ instructions were incorrectly optimized
  to 128-bit VPUNPCKLQDQ instructions by checking for XMM destination.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The fix adds a check for XMM destination, which may slightly increase the overhead
  of the optimization process, but it prevents incorrect code generation.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Fixes a bug where 256-bit VPBROADCASTQ instructions were incorrectly optimized
    to 128-bit VPUNPCKLQDQ instructions by checking for XMM destination.
  quote: 'But it didn''t check if the destination operand is XMM.  As the result,
    it

    turned:


    vpbroadcastq %xmmN, %ymmM


    into


    vpunpcklqdq %xmmN, %xmmN, %xmmM'
primer_expert: This patch fixes an incorrect optimization in the x86 assembler (`gas`)
  related to the `VPBROADCASTQ` instruction. The optimization attempts to replace
  a `VPBROADCASTQ` instruction with a `VPUNPCKLQDQ` instruction under certain conditions.
  The bug occurs because the optimization doesn't properly check the destination operand
  size, leading to incorrect code generation when a YMM register is used as the destination.
primer_general: The GNU Assembler (`gas`) is responsible for translating assembly
  code into machine code. During this process, the assembler may perform optimizations
  to improve the efficiency of the generated code. This patch addresses a bug in one
  such optimization for the `VPBROADCASTQ` instruction on x86 processors.  The `VPBROADCASTQ`
  instruction is part of the AVX2 instruction set, which is used to perform operations
  on vectors of data. A bug in the assembler caused it to incorrectly optimize this
  instruction in some cases, leading to incorrect program behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqa0uyxS_U2eQYQxZYsDx+_srnsLrZ7f72Y4hxkCjpVvA@mail.gmail.com
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

H.J. Lu fixed a bug in the x86 assembler where the optimization of 128-bit `VPBROADCASTQ` instructions could lead to incorrect code generation when the destination operand was a YMM register. The original optimization, intended to replace `vpbroadcastq %xmmN, %xmmM` with `vpunpcklqdq %xmmN, %xmmN, %xmmM` (N < 8), failed to check if the destination operand was an XMM register. This resulted in 256-bit `vpbroadcastq %xmmN, %ymmM` being incorrectly transformed into `vpunpcklqdq %xmmN, %xmmN, %xmmM`. The fix adds a check for XMM destination to prevent this incorrect optimization.
