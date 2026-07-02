---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- opcode
- qualifiers
- assembler
- disassembler
discussion_id: 23d4ba68-e7cf-ae93-b6bd-0c6ec5b176eb@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 22/23] aarch64: Add new qualifier AARCH64_OPND_QLF_UNUSED'
headline: 'aarch64: Add new qualifier AARCH64_OPND_QLF_UNUSED'
tldr: Replaces QLF_NIL with QLF_UNUSED for qualifier sequence list padding in AArch64
  opcode definitions.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Requires updating code that uses qualifier sequence lists to use the new `AARCH64_OPND_QLF_UNUSED`
  qualifier.
- Slightly increased code complexity due to the introduction of a new qualifier.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Proposes replacing QLF_NIL with QLF_UNUSED for padding qualifier sequence
    lists, to improve clarity and simplify detection of empty sequences.
  quote: 'Replace QLF_NIL with QLF_UNUSED for qualifier sequence list padding.

    This splits apart distinct qualifier meanings, and simplifies detection

    of empty qualifier sequences.'
primer_expert: This patch modifies the AArch64 opcode definitions in `include/opcode/aarch64.h`
  and related files.  Qualifiers are used to distinguish between different forms of
  AArch64 instructions.  The `AARCH64_OPND_QLF_UNUSED` qualifier is introduced to
  explicitly mark unused entries in the qualifier sequence lists, improving the clarity
  and maintainability of the opcode definitions.
primer_general: This patch refines how AArch64 instructions are defined within binutils.  AArch64
  instructions can have variations based on the types of operands they use.  These
  variations are described using "qualifiers." This patch introduces a specific marker
  to indicate unused qualifier entries, making the instruction definitions clearer
  and easier to understand, thus simplifying future maintenance and extensions.
series_id: 'binutils:aarch64: add new qualifier aarch64_opnd_qlf_unused'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/23d4ba68-e7cf-ae93-b6bd-0c6ec5b176eb@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch introduces a new qualifier, `AARCH64_OPND_QLF_UNUSED`, to replace `QLF_NIL` for padding qualifier sequence lists in AArch64 opcode definitions. This change clarifies the distinct meanings of qualifiers and simplifies the detection of empty qualifier sequences. By separating the concepts of "no further qualification" and "unused entry", the patch improves the clarity and maintainability of the AArch64 opcode definitions.
