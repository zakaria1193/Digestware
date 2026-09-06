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
discussion_id: cde123df6ce754214c7482a3bc3ba109f807f63a.1788591257.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v2 2/2] x86: ACE_V1 support for ACE-specific instructions'
headline: 'x86: ACE_V1 support for ACE-specific instructions'
tldr: Adds assembler and disassembler support for new ACE_V1 specific instructions,
  including block scale register operations and tile outer products.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This is the second part of a series adding support for the ACE_V1 ISA
  to binutils. It focuses on the instructions unique to ACE, differentiating from
  the AMX-shared instructions covered in the first part. This includes instructions
  like BSRINIT, BSRMOVF/H/L for block scale registers, TILEMOVCOL/ROW for tile data
  movement, and several TOP variants for outer products. The implementation details
  in `gas/` and `opcodes/` are updated to recognize and correctly disassemble these
  new instructions based on the ACE v1.16.2 specification.
primer_glossary:
- term: ACE_V1
  definition: AI Compute Extensions version 1, an instruction set architecture extension
    for AI workloads on x86 processors.
- term: EVEX
  definition: An advanced instruction prefix used in x86 processors for SIMD operations,
    supporting features like extended registers, vector lengths, and masking.
- term: TMM
  definition: Tile Matrix Multiply registers, used by AMX and other AI acceleration
    features on x86 processors.
- term: block scale register
  definition: A register used in certain x86 instruction set extensions to control
    the scaling of blocks for operations like outer products.
- term: tile move write
  definition: Instructions that move data into tile registers, often used in matrix
    operations.
- term: outer product instructions
  definition: Instructions that compute the outer product of two vectors, a fundamental
    operation in linear algebra and machine learning.
series_id: 'binutils:x86: ace_v1 support for ace-specific instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/cde123df6ce754214c7482a3bc3ba109f807f63a.1788591257.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This patch series extends binutils support for the ACE_V1 (AI Compute Extensions) ISA by adding assembler and disassembler logic for ACE-specific instructions. This includes operations involving the block scale register, tile move writes, and various outer product instructions, referencing the ACE v1.16.2 specification.
