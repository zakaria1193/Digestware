---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- binutils
- x86
- optimization
- assembly
discussion_id: 57aec33f-cc0e-421f-9a35-5fff703a5c2c@suse.com
source_type: public_inbox
title: '[PATCH 2/5] x86/APX: optimize {nf} forms of IMUL with all-ones immediate'
headline: 'x86/APX: optimize {nf} forms of IMUL with all-ones immediate'
tldr: Replaces IMUL instructions with an all-ones immediate with NEG, simplifying
  the instruction and potentially improving performance.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaces a potentially multi-byte IMUL instruction with a shorter NEG instruction.
- Simplifies instruction sequences.
exchanges: []
primer_expert: This change targets gas's x86 instruction selection for APX. It identifies
  `imul` instructions where the immediate operand is -1 (all ones) and rewrites them
  as `neg`. This is applicable to various operand sizes and forms, including `imulzu`
  (unsigned multiply immediate to extended register).
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
- term: IMUL
  definition: Integer Multiply instruction in x86 architecture.
- term: immediate value
  definition: A constant value embedded directly within an instruction.
- term: NEG
  definition: Negate instruction in x86 architecture, which performs two's complement
    negation.
series_id: 'binutils:x86/apx: optimize {nf} forms of imul with all-ones immediate'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/57aec33f-cc0e-421f-9a35-5fff703a5c2c@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch optimizes specific forms of the x86 IMUL instruction when the immediate value is all ones (-1). It replaces these IMUL operations with the equivalent NEG (negate) instruction, which can lead to simpler instruction sequences and potential performance benefits.
