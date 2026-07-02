---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- qualifier
- error handling
discussion_id: 4742b057-d883-26cf-cd2d-957013b5e92c@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 19/23] aarch64: Return QLF_ERR for error conditions'
headline: 'Aarch64: Return QLF_ERR for error conditions'
tldr: Modify `vectype_to_qualifier` and `get_qualifier_from_partial_encoding` to return
  `AARCH64_OPND_QLF_ERR` instead of `AARCH64_OPND_QLF_NIL` on errors.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Changes the return value of `vectype_to_qualifier` and `get_qualifier_from_partial_encoding`
  in error cases, which might affect code relying on the previous behavior.
- Introduces a more explicit error signaling mechanism, potentially improving debugging
  and error handling.
exchanges: []
primer_expert: In the AArch64 backend, `vectype_to_qualifier` and `get_qualifier_from_partial_encoding`
  are responsible for determining the operand qualifier based on vector type information
  or partial encoding.  Returning `AARCH64_OPND_QLF_ERR` instead of `AARCH64_OPND_QLF_NIL`
  provides a clearer indication of error conditions during operand processing in `gas/config/tc-aarch64.c`.
primer_general: When the assembler encounters an instruction, it needs to determine
  the specific type of data the instruction will operate on. Operand qualifiers provide
  this information. This patch modifies functions that determine these qualifiers
  to return a specific `ERR` code when something goes wrong, rather than a generic
  `NIL` value. This makes it easier to identify and handle errors during the assembly
  process.
series_id: 'binutils:aarch64: return qlf_err for error conditions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4742b057-d883-26cf-cd2d-957013b5e92c@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch changes the functions `vectype_to_qualifier` and `get_qualifier_from_partial_encoding` to return `AARCH64_OPND_QLF_ERR` instead of `AARCH64_OPND_QLF_NIL` when an error condition is encountered.  This makes error handling more explicit and consistent within the AArch64 assembly code, which helps catch errors earlier and could simplify debugging.
