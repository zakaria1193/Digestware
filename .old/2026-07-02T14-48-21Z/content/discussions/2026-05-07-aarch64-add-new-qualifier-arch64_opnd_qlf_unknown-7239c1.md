---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- qualifier
- SVE
- consistency
discussion_id: c01d3d39-9184-9d50-77cf-5d3310eab11d@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 20/23] aarch64: Add new qualifier ARCH64_OPND_QLF_UNKNOWN'
headline: 'Aarch64: Add new qualifier ARCH64_OPND_QLF_UNKNOWN'
tldr: Introduce AARCH64_OPND_QLF_UNKNOWN to represent unknown operand qualifiers,
  improving code consistency.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces a new qualifier type, increasing the complexity of the qualifier enum.
- May require updates to existing code that relies on the previous behavior of `AARCH64_OPND_QLF_NIL`.
- Adds an extra check during development by setting the default qualifier to `AARCH64_OPND_QLF_ERR`.
exchanges: []
primer_expert: In the aarch64 backend, operand qualifiers specify additional constraints
  on register operands. The patch adds `AARCH64_OPND_QLF_UNKNOWN` to represent cases
  where the qualifier is not immediately known during parsing but can be deduced later.
  This change aims to improve consistency in how operand qualifiers are handled, especially
  in the context of SVE and the `F_STRICT` flag within `gas/config/tc-aarch64.c`.
primer_general: When assembling code, the assembler needs to know the exact type and
  size of data that instructions will operate on.  Operand qualifiers are extra bits
  of information attached to registers or memory locations that specify these constraints.
  This patch adds a new type of qualifier, `UNKNOWN`, for situations where the assembler
  doesn't yet know the data type but can figure it out later.  This helps the assembler
  handle instructions more consistently, especially for newer CPU features.
series_id: 'binutils:aarch64: add new qualifier arch64_opnd_qlf_unknown'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c01d3d39-9184-9d50-77cf-5d3310eab11d@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch introduces a new qualifier, `AARCH64_OPND_QLF_UNKNOWN`, to represent cases where the operand qualifier is unknown. It replaces some uses of `AARCH64_OPND_QLF_NIL` and aims to improve code consistency, especially concerning the `F_STRICT` flag for SVE instructions. For development, the default qualifier value during parsing is changed to `AARCH64_OPND_QLF_ERR` to catch errors early and ensure explicit qualifier assignments, which could prevent unexpected behavior with future changes.
