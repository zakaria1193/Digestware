---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- optimization
- VPBROADCASTQ
- VPUNPCKLQDQ
discussion_id: CAMe9rOqfwneN-54vwwLez0_YGTBn88NuzCzL9=N4h5kio2mVJQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH] x86: Check XMM destination when optimizing 128-bit VPBROADCASTQ'
headline: 'x86: Fix VPBROADCASTQ optimization in assembler'
tldr: The assembler incorrectly optimizes `vpbroadcastq` with a YMM destination; this
  patch fixes it by checking for an XMM destination.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses an issue in the x86 assembler's instruction optimization
  logic.  The assembler attempts to replace `vpbroadcastq` with `vpunpcklqdq` for
  128-bit operations. The bug occurs because the code doesn't validate the destination
  register size, leading to AVX instruction corruption when a YMM register is used
  as the destination.
primer_general: The assembler is a tool that translates assembly language (human-readable
  instructions) into machine code. This patch fixes an error in the assembler that
  caused it to generate incorrect machine code for a specific x86 instruction (`vpbroadcastq`)
  when used with certain types of registers (YMM).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqfwneN-54vwwLez0_YGTBn88NuzCzL9=N4h5kio2mVJQ@mail.gmail.com
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

H.J. Lu provides a patch that fixes an incorrect optimization in the x86 assembler. The original optimization of `vpbroadcastq %xmmN, %xmmM`  to `vpunpcklqdq %xmmN, %xmmN, %xmmM` didn't check if the destination was an XMM register, leading to incorrect code generation when the destination was a YMM register.  The patch adds this check.
