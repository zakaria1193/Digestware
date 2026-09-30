---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- ACE
- assembler
- disassembler
discussion_id: ae54cf1f99aee4fc8b1ea144f14408dec7595716.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 5/7] x86: add ACE V1 block scale register instructions'
headline: 'x86: add ACE V1 block scale register instructions'
tldr: Adds assembler and disassembler support for ACE V1 block scale register instructions
  and the bsr0 register.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds new instructions and a register, increasing the complexity of the assembler
  and disassembler.
- Ensures compatibility with the ACE V1 specification.
exchanges: []
primer_expert: This patch adds support for new x86 instructions related to the ACE
  V1 specification, specifically focusing on block scale registers (bsr0). It modifies
  gas/config/tc-i386.c to recognize the bsr0 register and updates opcodes/i386-dis-*.h
  and opcodes/i386-opc.tbl to handle the new instructions within the gas and opcodes
  components of binutils.
primer_glossary:
- term: ACE V1
  definition: AI Compute Extensions version 1, a set of x86 instructions designed
    to accelerate AI and machine learning workloads.
- term: assembler
  definition: A program that converts assembly language source code into machine code.
- term: disassembler
  definition: A program that converts machine code into assembly language source code.
- term: bsr0
  definition: A register introduced with ACE V1, used in conjunction with block scale
    register instructions.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: opcodes
  definition: The part of an instruction that specifies the operation to be performed.
    In binutils, 'opcodes' refers to the component responsible for instruction decoding
    and encoding.
series_id: 'binutils:x86: add ace v1 block scale register instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ae54cf1f99aee4fc8b1ea144f14408dec7595716.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch introduces assembler and disassembler support for the BSRINIT, BSRMOVF, BSRMOVH, and BSRMOVL instructions, along with the bsr0 register. This is part of a larger series enabling the AI Compute Extensions (ACE) V1 ISA in binutils.
