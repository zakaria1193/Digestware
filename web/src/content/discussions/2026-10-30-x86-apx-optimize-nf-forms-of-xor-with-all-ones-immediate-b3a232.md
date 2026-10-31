---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- binutils
- x86
- optimization
- assembly
discussion_id: f0c60ae6-16ec-4c85-b060-b5a8e373c154@suse.com
source_type: public_inbox
title: '[PATCH 1/5] x86/APX: optimize {nf} forms of XOR with all-ones immediate'
headline: 'x86/APX: optimize {nf} forms of XOR with all-ones immediate'
tldr: Replaces XOR instructions with an all-ones immediate with NOT, simplifying the
  instruction.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces code size by replacing a generic XOR with a specific NOT instruction.
- Ensures compatibility with legacy x86 encodings where applicable.
exchanges: []
primer_expert: This patch modifies gas's instruction selection for x86 APX. It identifies
  XOR instructions with an immediate operand of -1 (all ones) or 0xFF and rewrites
  them as NOT instructions. This applies to various operand sizes and forms, aiming
  for code size reduction by using the more specific NOT instruction.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures (ISAs) for CPUs, commonly
    used in personal computers and servers.
- term: APX
  definition: Advanced Performance Extensions, a set of new instructions and features
    for x86 processors.
- term: '{nf}'
  definition: Refers to instruction forms that do not utilize fused operations, often
    implying more explicit or less optimized instruction sequences.
- term: XOR
  definition: Exclusive OR, a bitwise logical operation.
- term: immediate value
  definition: A constant value embedded directly within an instruction.
- term: NOT
  definition: Bitwise NOT (complement) instruction in x86 architecture.
series_id: 'binutils:x86/apx: optimize {nf} forms of xor with all-ones immediate'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f0c60ae6-16ec-4c85-b060-b5a8e373c154@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch optimizes x86 XOR instructions when the immediate value is all ones (-1) or 0xFF. It replaces these operations with the NOT (bitwise NOT) instruction, which achieves the same result with potentially fewer bytes or a simpler instruction encoding.
