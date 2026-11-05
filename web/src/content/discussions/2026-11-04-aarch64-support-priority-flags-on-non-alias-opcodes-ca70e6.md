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
discussion_id: 8e9cd716-5c09-d3b3-2e68-2005974e3cb2@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 25/28] aarch64: Support priority flags on non-alias opcodes'
headline: 'aarch64: Support priority flags on non-alias opcodes'
tldr: Patch removes opcode table order dependencies in aarch64 disassembler by using
  explicit priority flags.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removes reliance on opcode table order for disassembly.
- Potentially reduces decode chain lengths.
- Increases complexity slightly by requiring explicit priority for all opcodes.
exchanges: []
primer_expert: This patch refactors the aarch64 opcode table processing within binutils.
  It introduces explicit priority handling for all opcodes, including non-aliased
  ones, moving away from implicit prioritization based on table order. The `opcode_priority`
  function is updated to always return a value based on the instruction's flags, rather
  than defaulting to 0 for non-aliases. This allows the disassembler to build a more
  robust decode tree, independent of the table's ordering, and potentially simplifies
  alias handling in future patches. The priorities of `msr` and `mrs` are also adjusted.
primer_glossary:
- term: opcode priority
  definition: A mechanism to resolve ambiguities when multiple opcodes match a given
    instruction word, by giving precedence to certain instructions over others.
- term: decode tree
  definition: An internal data structure used by disassemblers to efficiently map
    instruction bit patterns to their corresponding symbolic names and properties.
- term: alias
  definition: In this context, an instruction that is a variation or shorthand for
    another, often differing in a few bits that control its specific behavior or target.
- term: msr/mrs
  definition: 'Instructions in the ARM architecture used to move data between general-purpose
    registers and system registers (MSR: Move to System Register, MRS: Move from System
    Register).'
- term: P0
  definition: Indicates the highest priority level (Priority 0) in a system with multiple
    priority levels.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set.
series_id: 'binutils:aarch64: support priority flags on non-alias opcodes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8e9cd716-5c09-d3b3-2e68-2005974e3cb2@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch modifies the aarch64 disassembler to support priority flags on non-alias opcodes. This change removes dependencies on the opcode table's order, allowing for more consistent disassembly regardless of table arrangement. It also reduces the length of decode chains by moving more logic into the decode tree. The priorities for `msr` and `mrs` instructions have been reduced to P0. This ensures all opcode prioritizations are explicitly defined.
