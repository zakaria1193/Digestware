---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- disassembler
- architecture extension
- testing
discussion_id: 20261016141228.388135-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH] aarch64: Add FEAT_LSC64B assembly support'
headline: 'aarch64: Add FEAT_LSC64B assembly support'
tldr: Adds support for the new aarch64 FEAT_LSC64B architecture extension and its
  associated instructions (LDA64B, STL64B, etc.) to the assembler and disassembler.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds support for new hardware features, enabling developers to utilize them.
- Increases the complexity of the assembler and disassembler by adding new instructions
  and feature checks.
- Includes new tests to ensure correctness, requiring maintenance as the architecture
  evolves.
exchanges: []
primer_expert: This patch adds support for the FEAT_LSC64B architecture extension
  to the aarch64 assembler and disassembler. This extension introduces load-store
  exclusive cache (LSC) instructions with 64-byte atomicity. The implementation correctly
  models that FEAT_LSC64B implies FEAT_LSCP and requires FEAT_LS64, and it reuses
  the Rt operand definition from FEAT_LS64. New tests cover instruction encoding,
  decoding, and feature dependencies.
primer_glossary:
- term: aarch64
  definition: The 64-bit instruction set architecture for ARM processors.
- term: FEAT_LSC64B
  definition: A specific ARM architecture feature extension related to Load-Store
    Cache (LSC) operations with 64-byte granularity.
- term: LDA64B, STL64B, STL64BV, STL64BV0
  definition: New assembly instructions associated with the FEAT_LSC64B extension,
    likely for atomic load, store, and store-conditional operations involving 64-byte
    cache lines.
- term: FEAT_LSCP
  definition: An ARM architecture feature extension that likely relates to Load-Store
    Cache operations, possibly a prerequisite or component of FEAT_LSC64B.
- term: FEAT_LS64
  definition: An ARM architecture feature extension related to 64-byte Load-Store
    operations, required for the new LSC64B instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016141228.388135-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Muhammad Kamran introduces support for the FEAT_LSC64B architecture extension in the ARM 64-bit assembler and disassembler. This includes adding the new instructions LDA64B, STL64B, STL64BV, and STL64BV0. The patch also models the dependencies of FEAT_LSC64B on FEAT_LSCP and FEAT_LS64, reuses existing operand constraints, and adds comprehensive tests for the new features.
