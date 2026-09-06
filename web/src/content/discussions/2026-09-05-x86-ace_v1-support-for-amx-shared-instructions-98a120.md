---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- ace
- amx
- isa
discussion_id: 5b6c56cbfd1d14e67d31556d4c0de464aad4deaa.1788591257.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v2 1/2] x86: ACE_V1 support for AMX-shared instructions'
headline: 'x86: ACE_V1 support for AMX-shared instructions'
tldr: Enables ACE_V1 architecture support in binutils, reusing AMX instructions for
  tile management and operations.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Reusing AMX instructions for ACE_V1 may simplify implementation but requires careful
  validation to ensure correct behavior across both contexts.
- Adding EVEX.V' validation adds complexity but prevents incorrect instruction encodings.
exchanges: []
primer_expert: This is the first part of a series introducing ACE_V1 ISA support to
  binutils. It focuses on enabling the ACE_V1 architecture and reusing existing AMX
  (Advanced Matrix Extensions) instructions for tile management, row moves, and conversions.
  The changes include updating the configuration to recognize ACE_V1, modifying opcode
  tables and disassembler logic to handle these shared instructions with ACE_V1 context,
  and adding validation for the EVEX.V' encoding to prevent incorrect usage with specific
  register types.
primer_glossary:
- term: ACE_V1
  definition: AI Compute Extensions version 1, an instruction set architecture extension
    for AI workloads on x86 processors.
- term: AMX
  definition: Advanced Matrix Extensions, an x86 instruction set extension designed
    to accelerate matrix operations, particularly for AI and machine learning workloads.
- term: TMM registers
  definition: Tile Matrix Multiply registers, a set of registers introduced with AMX
    for holding matrix tiles.
- term: EVEX
  definition: An advanced instruction prefix used in x86 processors for SIMD operations,
    supporting features like extended registers, vector lengths, and masking.
series_id: 'binutils:x86: ace_v1 support for amx-shared instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/5b6c56cbfd1d14e67d31556d4c0de464aad4deaa.1788591257.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This patch introduces assembler and disassembler support for the ACE_V1 architecture in binutils, enabling its use alongside existing AMX-shared instructions. It allows TMM register usage and includes validation for EVEX.V' encoding to reject invalid combinations, ensuring correct interpretation of these AI-focused instructions.
