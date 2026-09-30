---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- ACE
- assembler
- disassembler
- instruction set
discussion_id: cover.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 0/7] x86: add ACE V1 ISA support'
headline: 'x86: add ACE V1 ISA support'
tldr: Adds assembler and disassembler support for the x86 ACE V1 (AI Compute Extensions)
  instructions.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds a significant new instruction set extension to binutils.
- Requires multiple patches to introduce dependencies and the final support.
- Balances code reuse (AMX) with new feature implementation.
exchanges: []
primer_expert: This is the cover letter for a series of patches adding support for
  the ACE V1 instruction set to binutils. It outlines the changes, which include establishing
  a shared 'TILE' feature, fixing EVEX decoding for new instructions, and integrating
  the ACE V1 ISA itself, including new registers and instructions for tile management
  and block scaling. The series is structured with prerequisites first, followed by
  the core ACE V1 enablement.
primer_glossary:
- term: ACE V1
  definition: AI Compute Extensions version 1, a new set of x86 instructions designed
    to accelerate AI and machine learning workloads.
- term: assembler
  definition: A program that converts assembly language source code into machine code.
- term: disassembler
  definition: A program that converts machine code into assembly language source code.
- term: EVEX
  definition: A 4-byte instruction prefix used in AVX-512 and later x86 instruction
    sets to encode features like vector length, rounding, and masking.
- term: ISA
  definition: Instruction Set Architecture. The set of commands a processor can execute.
series_id: 'binutils:x86: add ace v1 isa support'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/cover.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch series introduces assembler and disassembler support for the new x86 ACE V1 (AI Compute Extensions) instructions. The series first adds prerequisite patches for internal features like 'TILE' and EVEX decoding, then enables ACE V1 and adds support for its specific instructions, including block scale registers and tile operations.
