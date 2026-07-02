---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- opcode table
- qualifier
- conditional select
discussion_id: 65cd537e-a57a-4d40-6a24-07b495e49fc5@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 13/23] aarch64: Fix qualifier sequences for cinc/cinv/cneg'
headline: 'Aarch64: Fix qualifier sequences for cinc/cinv/cneg'
tldr: Correct the qualifier sequences for three-operand cinc/cinv/cneg instructions
  to prevent future breakage.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Corrects an existing error in the opcode table.
- Ensures future compatibility when `AARCH64_OPND_QLF_NIL` is no longer a wildcard.
exchanges: []
primer_expert: The AArch64 opcode table (`opcodes/aarch64-tbl.h`) defines the structure
  of AArch64 instructions.  The `cinc`, `cinv`, and `cneg` instructions are conditional
  select aliases.  This patch corrects the qualifier sequences for the three-operand
  variants to use `QL_R2NIL` instead of `QL_CSEL`. This ensures correct behavior when
  `AARCH64_OPND_QLF_NIL` no longer acts as a wildcard.
primer_general: The assembler translates human-readable instructions into machine
  code. This patch fixes an error in the assembler's internal tables that describe
  the exact format of certain instructions (`cinc`, `cinv`, `cneg`). This ensures
  that the assembler generates the correct machine code for these instructions, especially
  when an operand is optional.
series_id: 'binutils:aarch64: fix qualifier sequences for cinc/cinv/cneg'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/65cd537e-a57a-4d40-6a24-07b495e49fc5@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch corrects the qualifier sequences for the three-operand forms of the `cinc`, `cinv`, and `cneg` instructions in the AArch64 assembler. These instructions were incorrectly using the same qualifier sequences as their four-operand counterparts, leading to an incorrect qualifier being specified for the third operand. This patch replaces the incorrect `QL_CSEL` sequence with `QL_R2NIL`, which will become necessary when `AARCH64_OPND_QLF_NIL` is no longer treated as a wildcard.
