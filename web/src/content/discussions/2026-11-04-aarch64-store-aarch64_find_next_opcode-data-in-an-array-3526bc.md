---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- performance
- refactoring
discussion_id: 50d27f4c-2736-c98e-2111-4d54e1e595cb@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 21/28] aarch64: Store aarch64_find_next_opcode data in an array'
headline: 'aarch64: Store aarch64_find_next_opcode data in an array'
tldr: Replaces a switch statement with an array lookup for AArch64 instruction decoding.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Replaces a switch statement with an array lookup for potentially faster instruction
  decoding.
- Simplifies code structure, paving the way for further refactoring.
exchanges: []
primer_expert: Replaces the `switch` statement in `aarch64_find_next_opcode` within
  `opcodes/aarch64-dis-2.c` with an array-based lookup. This is a preparatory step
  to removing the decode tree entirely, simplifying the instruction lookup mechanism.
  The array stores the mapping from instruction keys to their corresponding opcode
  indices, offering a more direct and potentially faster lookup compared to a deeply
  nested switch.
primer_glossary:
- term: aarch64_find_next_opcode
  definition: A function in the AArch64 disassembler responsible for determining the
    next opcode in a decoding sequence, likely used to resolve instruction variants
    or aliases.
series_id: 'binutils:aarch64: store aarch64_find_next_opcode data in an array'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/50d27f4c-2736-c98e-2111-4d54e1e595cb@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch updates `opcodes/aarch64-dis-2.c` to store the data for `aarch64_find_next_opcode` in an array instead of using a large switch statement. This simplifies the lookup process for instruction decoding and sets the stage for removing the decode tree data structure in a subsequent commit. The change is presented as a simplification and preparation for further refactoring.
