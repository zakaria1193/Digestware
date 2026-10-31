---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- binutils
- x86
- optimization
- assembly
discussion_id: 7d7225a0-7df6-41be-bda9-8b83c8e7f99a@suse.com
source_type: public_inbox
title: '[PATCH 0/5] x86/APX: more {nf} optimizations'
headline: 'x86/APX: more {nf} optimizations'
tldr: A series of patches to optimize various x86 {nf} instruction forms for better
  code density.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves code size by using more efficient instruction encodings.
- Slightly increases complexity of the assembler's instruction selection logic.
exchanges: []
primer_expert: This is the cover letter for a series of patches that enhance the x86
  assembler's instruction selection heuristics. The focus is on 'nf' instruction forms,
  aiming to replace sequences that can be more compactly represented by single instructions
  (e.g., XOR with all-ones immediate becomes NOT, IMUL with all-ones immediate becomes
  NEG) or by narrower forms of the same instruction (e.g., 64-bit AND with small immediate
  becomes 8-bit AND).
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
- term: immediate value
  definition: A constant value embedded directly within an instruction.
- term: assembly
  definition: A low-level programming language that uses mnemonics to represent machine
    code instructions.
series_id: 'binutils:x86/apx: more {nf} optimizations'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/7d7225a0-7df6-41be-bda9-8b83c8e7f99a@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This is a cover letter for a series of five patches aimed at optimizing various 'nf' (no-fused) instruction forms in the x86 architecture. The optimizations target XOR, IMUL, AND, and OR instructions with specific immediate values, seeking to replace them with more efficient or shorter equivalents like NOT or NEG, and improve code density.
