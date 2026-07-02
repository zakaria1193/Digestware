---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- stack pointer
- opcode flag
- code simplification
discussion_id: fe6df20a-c3bc-7e96-e130-f9e7497b1cf5@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 11/23] aarch64: Add F_REQUIRES_SP and eliminate QLF_SP and QLF_WSP'
headline: 'Aarch64: Add F_REQUIRES_SP and eliminate QLF_SP and QLF_WSP'
tldr: Enforce stack pointer requirements using opcode flags instead of operand qualifiers,
  simplifying the code.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removes `QLF_SP` and `QLF_WSP`, reducing the complexity of the operand qualifier
  system.
- Introduces `F_REQUIRES_SP`, adding a new flag to the opcode definition.
- Simplifies qualifier matching logic.
exchanges: []
primer_expert: This patch refactors the handling of stack pointer requirements in
  the AArch64 backend. By introducing `F_REQUIRES_SP` and removing `QLF_SP` and `QLF_WSP`
  in `include/opcode/aarch64.h` and `opcodes/aarch64-asm.c`, the code simplifies the
  qualifier matching process and makes the stack pointer requirement more explicit
  at the opcode level.
primer_general: When the assembler translates code, it needs to ensure that instructions
  are used correctly. This patch changes how the assembler enforces the rule that
  certain instructions must use the stack pointer. By using a special flag instead
  of extra qualifiers, the assembler's code becomes simpler and easier to understand,
  reducing the chance of errors.
series_id: 'binutils:aarch64: add f_requires_sp and eliminate qlf_sp and qlf_wsp'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/fe6df20a-c3bc-7e96-e130-f9e7497b1cf5@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch replaces the `QLF_SP` and `QLF_WSP` operand qualifiers with a new opcode flag, `F_REQUIRES_SP`. This flag enforces the requirement for at least one stack pointer operand in the `mov` (to/from SP) opcode. By using an opcode flag instead of operand qualifiers, the code for switching between SP and non-SP qualifiers is removed, resulting in a simpler and less confusing implementation.
