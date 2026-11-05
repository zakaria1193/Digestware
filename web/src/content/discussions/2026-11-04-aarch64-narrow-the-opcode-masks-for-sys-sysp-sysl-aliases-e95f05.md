---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- disassembler
- opcode
- performance
discussion_id: fe4c48de-1cd8-475b-9379-01324cb0c8ec@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 28/28] aarch64: Narrow the opcode masks for SYS/SYSP/SYSL aliases'
headline: 'aarch64: Narrow the opcode masks for SYS/SYSP/SYSL aliases'
tldr: Patch narrows opcode masks for aarch64 SYS/SYSP/SYSL aliases, improving disassembly
  efficiency.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Slight improvement in disassembly speed due to more efficient opcode matching.
exchanges: []
primer_expert: This patch modifies the opcode decoding logic for the aarch64 architecture
  within binutils. It targets a set of aliases for system instruction-related opcodes
  (`SYS`, `SYSP`, `SYSL`). By adjusting the bitmasks used to identify these opcodes,
  the disassembler's internal decision tree can prune more branches earlier, potentially
  leading to faster disassembly. This is a refinement of the opcode matching mechanism.
primer_glossary:
- term: opcode mask
  definition: A bitmask used to isolate specific bits within an instruction's binary
    representation to identify the instruction or its type.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set.
- term: alias
  definition: In this context, an instruction that is a variation or shorthand for
    another, often differing in a few bits that control its specific behavior or target.
- term: SYS/SYSP/SYSL
  definition: Instructions in the ARM architecture that interact with system registers
    or perform system-level operations. The 'L' suffix typically indicates 'long'
    or a specific operand variant.
- term: decode tree
  definition: An internal data structure used by disassemblers to efficiently map
    instruction bit patterns to their corresponding symbolic names and properties.
series_id: 'binutils:aarch64: narrow the opcode masks for sys/sysp/sysl aliases'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/fe4c48de-1cd8-475b-9379-01324cb0c8ec@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refines the opcode masks for aarch64 `SYS`, `SYSP`, and `SYSL` instruction aliases. By narrowing these masks, the disassembler's decode tree can more efficiently eliminate unnecessary opcode entries. While this change doesn't affect assembly or disassembly output because operand bits are also checked, it optimizes the internal lookup process. The patch notes that the `DC` instruction has an irregular encoding space, still resulting in a decode chain of 11 opcodes.
