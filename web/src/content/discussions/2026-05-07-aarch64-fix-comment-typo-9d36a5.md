---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- typo
discussion_id: c0cd30ff-4aa1-57fa-008a-6cbec389428b@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 01/23] aarch64: Fix comment typo'
headline: 'Aarch64: Fix comment typo'
tldr: Corrects a typo in a comment within the AArch64 disassembler.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improved code readability.
- No performance impact.
exchanges: []
primer_expert: Fixes a trivial typo in `opcodes/aarch64-dis.c`.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the disassembler for the AArch64 architecture.
  The disassembler translates machine code back into human-readable assembly code.
  This patch corrects a typo.'
series_id: 'binutils:aarch64: fix comment typo'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c0cd30ff-4aa1-57fa-008a-6cbec389428b@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch corrects a typo in a comment in `opcodes/aarch64-dis.c`.  The word "accommadate" is corrected to "accommodate". This improves code readability.
