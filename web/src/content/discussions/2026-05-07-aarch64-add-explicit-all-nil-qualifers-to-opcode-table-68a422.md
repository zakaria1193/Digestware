---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- opcode table
- qualifier
- NIL
discussion_id: 9fcc68b2-d261-6eaa-3631-9cf1b5cca568@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 17/23] aarch64: Add explicit all-nil qualifers to opcode table'
headline: 'Aarch64: Add explicit all-nil qualifers to opcode table'
tldr: Make the `NIL` qualifier value explicit in qualifier sequences to avoid relying
  on its implicit zero value.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increases the size of the opcode table.
- Improves code clarity and maintainability by avoiding implicit assumptions about
  the value of `AARCH64_OPND_QLF_NIL`.
exchanges: []
primer_expert: In the AArch64 backend, the opcode table (`opcodes/aarch64-tbl.h`)
  defines the structure of AArch64 instructions. This patch introduces `QL_0`, `QL_NIL1`,
  `QL_NIL2`, and `QL_NIL3` macros for explicitly defining qualifier sequences containing
  `AARCH64_OPND_QLF_NIL`. This ensures correct behavior when `AARCH64_OPND_QLF_NIL`
  is no longer implicitly zero.
primer_general: The assembler uses opcode tables to understand the structure of instructions.  This
  patch makes the table more explicit about what happens when an instruction doesn't
  have a qualifier.  Instead of assuming a default value of zero, it explicitly sets
  the qualifier to `NIL`. This ensures that the assembler continues to work correctly
  even if the internal value of `NIL` changes in the future.
series_id: 'binutils:aarch64: add explicit all-nil qualifers to opcode table'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9fcc68b2-d261-6eaa-3631-9cf1b5cca568@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch updates the opcode table to explicitly define all-NIL qualifier sequences. The `AARCH64_OPND_QLF_NIL` qualifier will soon have a nonzero enum value. This change ensures that qualifier sequences that are intended to be all-NIL are explicitly defined as such, rather than relying on the implicit zero value of uninitialized memory.  This prevents unexpected behavior when `AARCH64_OPND_QLF_NIL` changes.
