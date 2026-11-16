---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- AVX10.3
- x86
- ISA
- assembly
discussion_id: 20261116081322.1851772-1-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH 0/3] Support AVX10.3 instructions'
headline: Support AVX10.3 instructions
tldr: Add support for new AVX10.3 instructions to binutils, extending current AVX10.2
  capabilities.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in the assembler/disassembler to support new instructions.
- Ensures forward compatibility for future hardware implementations.
exchanges:
- author: Haochen Jiang <haochen.jiang@intel.com>
  role: proposer
  position: Submits a patch series to add support for the AVX10.3 instruction set
    to binutils, noting that AVX10V2AUX is already in the trunk.
  quote: 'In this patch series, we are going to support AVX10.3 instructions.


    Based on AVX10.2, AVX10.3 includes four part of insts, where AVX10V2AUX is already
    on trunk.'
primer_expert: This patch series adds support for the AVX10.3 instruction set extensions
  to the binutils assembler and disassembler. Binutils processes assembly language
  and produces object code, and this change ensures it can correctly parse and represent
  new AVX10.3 mnemonics and their encoding. The primary impact is on developers targeting
  microarchitectures that will implement AVX10.3, allowing them to utilize these new
  instructions.
primer_glossary:
- term: AVX10.3
  definition: A new instruction set extension for x86 processors, building upon AVX10.2.
    It introduces new capabilities for advanced vector operations.
- term: ISA
  definition: Instruction Set Architecture. Defines the set of commands a processor
    can execute.
- term: x86 AG
  definition: Refers to the x86 Architecture Group, likely responsible for defining
    new instruction set extensions for Intel and AMD processors.
- term: mnemonics
  definition: Symbolic names given to machine language instructions, used in assembly
    language (e.g., MOV, ADD).
series_id: binutils:support avx10.3 instructions
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081322.1851772-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

Haochen Jiang proposes adding support for the new AVX10.3 instructions to binutils. This update builds upon the existing AVX10.2 support and introduces four new instruction parts, one of which (AVX10V2AUX) is already present in the trunk. The changes are based on recently disclosed ISA specifications.
