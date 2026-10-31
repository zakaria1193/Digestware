---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- binutils
- x86
- optimization
- assembly
discussion_id: 534abb89-6af1-4986-a8f5-2051f077d08b@suse.com
source_type: public_inbox
title: '[PATCH 3/5] x86/APX: optimize {nf} forms of AND with small immediates'
headline: 'x86/APX: optimize {nf} forms of AND with small immediates'
tldr: Optimize AND instructions with small immediate values for better code density
  in x86 assembly.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces code size by using narrower instruction forms.
- May increase complexity of the assembler's internal logic for instruction selection.
exchanges: []
primer_expert: This patch modifies gas's instruction selection logic for x86. It targets
  the 'nf' (no-fused) forms of AND instructions, which are part of the APX extension.
  The optimization replaces certain AND operations with smaller immediate values (e.g.,
  8-bit or 16-bit) by utilizing EVEX encoding properties, aiming to reduce code size.
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
- term: AND
  definition: A bitwise logical operation that outputs 1 only when both inputs are
    1.
- term: immediate value
  definition: A constant value embedded directly within an instruction.
- term: EVEX.ND encoding
  definition: A specific encoding scheme used in x86 instruction sets (particularly
    AVX-512) that allows for implied zero-extension of operands.
series_id: 'binutils:x86/apx: optimize {nf} forms of and with small immediates'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/534abb89-6af1-4986-a8f5-2051f077d08b@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch introduces optimizations for AND instructions in x86 assembly, specifically targeting forms with small immediate values. It leverages implied zero-extension of EVEX.ND encodings to replace wider operations with narrower byte or word forms, improving code density.
