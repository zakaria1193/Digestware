---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- opcode
- assembler
- disassembler
discussion_id: 8848be0a-28cd-b6e1-d7c8-a7a720d27714@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 21/23] aarch64: Remove F_STRICT'
headline: 'aarch64: Remove F_STRICT'
tldr: Removes the F_STRICT flag from AArch64 opcode definitions, as it's no longer
  needed with AARCH64_OPND_QLF_UNKNOWN.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Requires ensuring that the new qualifier handling logic correctly handles cases
  previously covered by `F_STRICT`.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Proposes removing the F_STRICT flag, as it is no longer needed with the
    introduction of AARCH64_OPND_QLF_UNKNOWN.
  quote: 'With the introduction of AARCH64_OPND_QLF_UNKNOWN, the F_STRICT flag is

    no longer needed and can be deleted.'
primer_expert: This patch modifies the AArch64 opcode definitions in `include/opcode/aarch64.h`
  and `opcodes/aarch64-tbl.h`.  The `F_STRICT` flag controlled how strictly the assembler
  and disassembler matched qualifiers in opcode definitions.  With the introduction
  of  `AARCH64_OPND_QLF_UNUSED` (or `AARCH64_OPND_QLF_UNKNOWN` as stated), this flag
  is redundant.
primer_general: This patch simplifies the internal representation of AArch64 instructions
  within binutils.  Specifically, it removes a flag called `F_STRICT` that controlled
  how closely the assembler and disassembler matched instruction variations. By removing
  this flag, the instruction definitions become cleaner and easier to maintain, without
  affecting the functionality of the tools.
series_id: 'binutils:aarch64: remove f_strict'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8848be0a-28cd-b6e1-d7c8-a7a720d27714@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes the `F_STRICT` flag from AArch64 opcode definitions. With the introduction of `AARCH64_OPND_QLF_UNKNOWN` (likely a typo and should be AARCH64_OPND_QLF_UNUSED from the previous patch), the `F_STRICT` flag, which required an exact qualifier match even for NIL qualifiers, is no longer necessary.  Removing this flag simplifies the opcode definitions and reduces code complexity.
