---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- performance
- decode tree
discussion_id: 0780a3b0-c80f-1e82-1c57-12eb52bea2a9@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 24/28] aarch64: Enable partial splits in the decode tree'
headline: 'aarch64: Enable partial splits in the decode tree'
tldr: Shortens AArch64 instruction decode chains by enabling partial splits.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases complexity of decode tree logic for a performance gain.
exchanges: []
primer_expert: This patch modifies `opcodes/aarch64-dis-2.c` to allow the AArch64
  disassembler's decode tree to use partial splits. Previously, the decode tree required
  full splits, leading to long chains for certain instruction groups. By enabling
  partial splits, the tree can branch on subsets of bits, significantly reducing the
  depth of the decode chain and thus speeding up disassembly for complex instructions.
primer_glossary: []
series_id: 'binutils:aarch64: enable partial splits in the decode tree'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0780a3b0-c80f-1e82-1c57-12eb52bea2a9@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch enables partial splits in the AArch64 instruction decode tree. This optimization reduces the longest decode chain from 26 opcodes to 5, improving disassembly performance for complex instructions involving SIMD modified immediate and shift by immediate encoding groups. The change refines the decode logic by examining specific bits to distinguish these encoding groups.
