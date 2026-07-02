---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- opcode table
- qualifier
- consistency
discussion_id: 4de2501e-da46-1465-0c98-20e29b2b706e@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 14/23] aarch64: Make FPIMM0 qualifiers consistent'
headline: 'Aarch64: Make FPIMM0 qualifiers consistent'
tldr: Standardize the FPIMM0 operand qualifier to `QLF_NIL` for consistency across
  the opcode table.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Minor change with no functional impact.
- Improves code maintainability by enforcing consistency.
exchanges: []
primer_expert: The AArch64 opcode table (`opcodes/aarch64-tbl.h`) defines instruction
  formats.  The `FPIMM0` operand represents a floating-point immediate value of zero.  This
  patch changes the qualifier used for `FPIMM0` in two table entries from `QLF_S_H`
  to `QLF_NIL` to match other entries, improving internal consistency.
primer_general: When an assembler translates a program, it relies on tables that describe
  the valid structure of each instruction. This patch fixes a small inconsistency
  in one of these tables, ensuring that a particular type of operand (a floating-point
  zero) is handled the same way across all instructions.  This makes the assembler's
  internal code more consistent and easier to maintain.
series_id: 'binutils:aarch64: make fpimm0 qualifiers consistent'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4de2501e-da46-1465-0c98-20e29b2b706e@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch addresses an inconsistency in the opcode table where two entries used `QLF_S_H` for the `FPIMM0` operand, while the rest used `QLF_NIL`.  By changing these two entries to also use `QLF_NIL`, the patch promotes consistency within the table, simplifying maintenance and reducing the risk of unexpected behavior due to the inconsistent qualifier. This change is purely for internal consistency and has no functional impact.
