---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- qualifier
- robustness
discussion_id: 26909d61-82f2-24f3-e29f-75850ff733b5@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 18/23] aarch64: Add QLF_ERR to aarch64_opnd_qualifiers'
headline: 'Aarch64: Add QLF_ERR to aarch64_opnd_qualifiers'
tldr: Add an explicit entry for `AARCH64_OPND_QLF_ERR` in `aarch64_opnd_qualifiers`
  for completeness and robustness.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Increases the size of the `aarch64_opnd_qualifiers` array.
- Adds a defensive measure against potential out-of-bounds accesses, which are unlikely
  to occur in practice.
exchanges: []
primer_expert: The `aarch64_opnd_qualifiers` array in `opcodes/aarch64-opc.c` maps
  operand qualifiers to their properties. This patch adds an entry for `AARCH64_OPND_QLF_ERR`
  to ensure that the array length matches the enum length, preventing potential out-of-bounds
  accesses.  While the `ERR` qualifier should not be used during normal operation,
  explicitly defining it improves robustness.
primer_general: The assembler uses tables to look up information about instructions
  and their operands. This patch adds an entry to one of these tables for an "error"
  qualifier. This "error" entry should never actually be used, but adding it makes
  the table more complete and prevents potential crashes if the assembler tries to
  access it.
series_id: 'binutils:aarch64: add qlf_err to aarch64_opnd_qualifiers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/26909d61-82f2-24f3-e29f-75850ff733b5@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch adds an entry for `AARCH64_OPND_QLF_ERR` to the `aarch64_opnd_qualifiers` array. Although this entry should ideally never be used, its presence ensures that the array length matches the enum length, improving code robustness and preventing potential out-of-bounds memory accesses, though such accesses would have been detected previously.
