---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- ace
- isa
- assembler
discussion_id: cover.1788591257.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v2 0/2] x86: add ACE_V1 ISA support'
headline: 'x86: add ACE_V1 ISA support'
tldr: Adds assembler and disassembler support for the ACE_V1 ISA, enabling AI-focused
  instructions on x86.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Balancing reuse of existing AMX logic with the need for ACE-specific validation
  and instructions.
- Ensuring correct and safe handling of the EVEX prefix, particularly the EVEX.V'
  bit, for ACE instructions.
exchanges: []
primer_expert: This is the cover letter for a two-part patch series introducing support
  for the AI Compute Extensions (ACE) V1 ISA in binutils. The series updates the assembler
  and disassembler to recognize and correctly handle new instructions designed for
  AI workloads. Part 1 focuses on enabling the ACE_V1 architecture and leveraging
  existing AMX instructions, while Part 2 adds support for instructions that are unique
  to ACE. The series has undergone revisions (V2) to address reviewer comments, including
  improvements to disassembly table lookups and stricter validation of EVEX prefix
  encodings, particular…
primer_glossary:
- term: ACE_V1
  definition: AI Compute Extensions version 1, an instruction set architecture extension
    for AI workloads on x86 processors.
- term: ISA
  definition: Instruction Set Architecture, the part of the processor visible to the
    programmer. It defines the set of instructions that a computer architecture supports.
- term: EVEX
  definition: An advanced instruction prefix used in x86 processors for SIMD operations,
    supporting features like extended registers, vector lengths, and masking.
- term: AMX
  definition: Advanced Matrix Extensions, an x86 instruction set extension designed
    to accelerate matrix operations, particularly for AI and machine learning workloads.
series_id: 'binutils:x86: add ace_v1 isa support'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/cover.1788591257.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This patch series introduces support for the ACE (AI Compute Extensions) V1 ISA in binutils, covering both assembler and disassembler functionalities. The series is divided into two parts: the first enables ACE_V1 and supports AMX-shared instructions, while the second adds ACE-specific instructions. Revisions in V2 address feedback, refine table lookups, and add crucial EVEX.V' validation for instruction encoding.
