---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- binutils
- macros
- opcodes
discussion_id: 8a88091d-e001-e910-3960-4e65cabbb8eb@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 3/5] aarch64: Inline all FLD_* uses in aarch64-tbl.h'
headline: 'aarch64: Inline all FLD_* uses in aarch64-tbl.h'
tldr: This patch inlines FLD_* macro uses in aarch64-tbl.h and defines FLD as an alias
  for AARCH64_FLD in aarch64-gen.c.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the aarch64 opcode definitions (`opcodes/aarch64-gen.c`
  and `opcodes/aarch64-opc.h`). It inlines `FLD_*` macros into operand field lists
  in `aarch64-tbl.h`.  These macros are used to define fields within AArch64 instructions.
primer_general: This patch modifies the binutils assembler for the AArch64 architecture.  It
  replaces some macros (`FLD_*`) with more explicit definitions when describing the
  layout of instructions. This change makes the code easier to understand and maintain.
series_id: 'binutils:aarch64: inline all fld_* uses in aarch64-tbl.h'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8a88091d-e001-e910-3960-4e65cabbb8eb@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

This patch inlines all non-constant field definitions into operand field lists within `aarch64-tbl.h`, and removes the resulting unused `FLD_*` macros. For brevity, it defines `FLD` as an alias for `AARCH64_FLD` in `aarch64-gen.c`.  This is part of a series to improve the clarity and maintainability of the aarch64 opcode definitions.
