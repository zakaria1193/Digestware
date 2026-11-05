---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- decode tree
- code generation
discussion_id: a7a91a98-e12e-ca22-2dee-73d74369e248@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 23/28] aarch64: Support partial splits in the decode tree'
headline: 'aarch64: Support partial splits in the decode tree'
tldr: Adds support for partial splits in the AArch64 instruction decode tree generation.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the decode tree generation logic to enable more efficient instruction
  decoding.
- Partial splits are currently disabled to ensure no regressions.
exchanges: []
primer_expert: Modifies `opcodes/aarch64-gen.c` to introduce the concept of partial
  splits in the AArch64 instruction decode tree generation. This allows the tree construction
  algorithm to handle cases where a group of opcodes cannot be fully distinguished
  by a single bit. Instead, it can split off a subset of opcodes and continue processing
  the rest, enabling a more optimized decode tree. The change is a prerequisite for
  future optimizations.
primer_glossary: []
series_id: 'binutils:aarch64: support partial splits in the decode tree'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a7a91a98-e12e-ca22-2dee-73d74369e248@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch introduces support for partial splits in the AArch64 instruction decode tree generation. It allows the decode tree to split off a subset of opcodes and then chain the remainder, which is useful for instructions that cannot be fully partitioned by a single bit. The feature is temporarily disabled in this patch to ensure existing functionality remains unchanged. Future work will enable it for aliases.
