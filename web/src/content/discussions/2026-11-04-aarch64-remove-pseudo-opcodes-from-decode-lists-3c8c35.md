---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- opcode
discussion_id: f79953bf-5d7e-2f35-db9d-3abd9e9785c3@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 11/28] aarch64: Remove pseudo opcodes from decode lists'
headline: 'aarch64: Remove pseudo opcodes from decode lists'
tldr: Removes pseudo opcodes from decode lists as they are never disassembled.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves the correctness of the disassembler by not returning pseudo-instructions.
- Simplifies the alias lookup logic.
exchanges: []
primer_expert: This change in `aarch64-dis-2.c` removes pseudo-instruction mappings
  from the `aarch64_find_next_alias_opcode` function. The rationale is that the disassembler's
  role is to translate machine code into human-readable assembly, and pseudo-instructions
  (like directives) are not part of the machine code itself. Therefore, they should
  not appear in the output of a function designed to find the 'next' opcode in a sequence,
  especially when that sequence is part of an alias chain.
primer_glossary:
- term: pseudo instruction
  definition: An instruction that is not a true machine code instruction but rather
    a directive or command for the assembler or compiler, often used for source-level
    control or metadata.
series_id: 'binutils:aarch64: remove pseudo opcodes from decode lists'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f79953bf-5d7e-2f35-db9d-3abd9e9785c3@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch removes pseudo opcodes from the decode lists within `aarch64_find_next_alias_opcode` in `aarch64-dis-2.c`. Since pseudo instructions are never the target of disassembly, they should not be returned by this function, thus cleaning up the decoding logic.
