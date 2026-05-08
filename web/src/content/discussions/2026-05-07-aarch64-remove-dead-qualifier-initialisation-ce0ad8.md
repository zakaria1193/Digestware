---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- dead code
- initialization
discussion_id: c2c88417-cc02-38c5-babf-130377813534@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 08/23] aarch64: Remove dead qualifier initialisation'
headline: 'Aarch64: Remove dead qualifier initialisation'
tldr: Removes an unused variable initialization in `encode_asimd_fcvt` function within
  the AArch64 assembler.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improved code clarity by removing redundant initialization.
- No performance impact.
exchanges: []
primer_expert: The patch removes the dead initialization of `qualifier` in `opcodes/aarch64-asm.c::encode_asimd_fcvt`.
  The variable is assigned `AARCH64_OPND_QLF_NIL` but is then always overwritten by
  a switch statement. Removing the initialization avoids a potentially misleading
  assignment.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler for the AArch64 architecture. The
  assembler translates human-readable assembly code into machine code that a computer
  can execute. The patch removes a variable initialization that''s immediately overwritten,
  cleaning up the code.'
series_id: 'binutils:aarch64: remove dead qualifier initialisation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c2c88417-cc02-38c5-babf-130377813534@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes an unused variable initialization in the `encode_asimd_fcvt` function in `opcodes/aarch64-asm.c`.  The variable `qualifier` is initialized but its value is overwritten before it is used. Removing the dead initialization simplifies the code.
