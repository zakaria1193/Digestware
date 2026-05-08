---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- unused operand
- code cleanup
discussion_id: cbc5fff6-7983-c2a6-7c2e-4aac23134934@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 03/23] aarch64: Remove unused operand ADDR_SIMM9_2'
headline: 'Aarch64: Remove unused operand ADDR_SIMM9_2'
tldr: Removes the unused `AARCH64_OPND_ADDR_SIMM9_2` operand from the AArch64 assembler.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improved code clarity by removing an unused operand.
- No performance impact.
exchanges: []
primer_expert: This patch removes `AARCH64_OPND_ADDR_SIMM9_2` from `include/opcode/aarch64.h`
  and related code in `gas/config/tc-aarch64.c`. This operand has been unused since
  commit c8f89a3423101b25.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch removes an unused operand, simplifying the code.'
series_id: 'binutils:aarch64: remove unused operand addr_simm9_2'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/cbc5fff6-7983-c2a6-7c2e-4aac23134934@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes the `AARCH64_OPND_ADDR_SIMM9_2` operand, which has been unused since commit c8f89a3423101b25.  This operand related to load/store register (unscaled) instructions. Removing the dead code simplifies the code base.
