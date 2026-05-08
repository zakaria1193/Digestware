---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- enum
- type error
discussion_id: f54b2753-a787-9e85-0df8-0c529830ff86@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 02/23] aarch64: Fix use of wrong zero enum value'
headline: 'Aarch64: Fix use of wrong zero enum value'
tldr: Corrects an enum comparison in `aarch64_get_expected_qualifier` by using `AARCH64_OPND_QLF_NIL`
  instead of `AARCH64_OPND_NIL`.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Corrects a type error, improving code correctness.
- No performance impact.
exchanges: []
primer_expert: This patch fixes a bug in `opcodes/aarch64-opc.c::aarch64_get_expected_qualifier`
  involving incorrect comparison of enum values. It replaces a cast to `(enum aarch64_opnd)`
  with a direct comparison to `AARCH64_OPND_QLF_NIL`.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch fixes a type error.'
series_id: 'binutils:aarch64: fix use of wrong zero enum value'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f54b2753-a787-9e85-0df8-0c529830ff86@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch corrects an error in `aarch64_get_expected_qualifier` where an `aarch64_opnd_qualifier_t` was incorrectly compared against `AARCH64_OPND_NIL` instead of `AARCH64_OPND_QLF_NIL`. The incorrect comparison was previously worked around by casting the qualifier to `(enum aarch64_opnd)`.  This patch removes the cast and uses the correct enum value for comparison, fixing the underlying type mismatch.
