---
project: binutils
subsystem: opcodes/aarch64
patch_id: null
tags:
- aarch64
- opcodes
- disassembler
- structure
commit_hash: 4fec2e2e720e3b377a086797ac577b7744d307fe
source_type: public_inbox
author: Alice Carlotti <acarlotti@sourceware.org>
headline: 'aarch64: Simplify operand field specification'
tldr: Replaces enum-based field kind tracking with direct struct usage for clearer
  AArch64 opcode definitions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch tackles the complexity in AArch64 instruction decoding by
  moving away from an enum-based `aarch64_field_kind` to direct usage of `aarch64_field`
  structs. It introduces compatibility macros to ease the transition. The core issue
  addressed is the increasing difficulty in mapping field names to their specific
  bit positions within opcodes, a problem exacerbated by architectural additions.
  By using structs directly, the code becomes more self-contained and easier to understand,
  reducing reliance on external lookup tables.
primer_glossary:
- term: aarch64_field_kind
  definition: An enumeration that previously represented the type or kind of a field
    within an AArch64 instruction's operand. This commit replaces it with a more direct
    structure-based approach.
- term: aarch64_field struct
  definition: A structure that defines the properties and bit positions of a field
    within an AArch64 instruction operand. This replaces the previous enum-based system
    for better clarity and directness.
- term: opcode
  definition: The part of a machine language instruction that specifies the operation
    to be performed. Opcode parsing involves breaking down instructions into their
    constituent parts, including operands and fields.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260710151734.44FE04BA2E11@sourceware.org
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This commit removes the indirection of `aarch64_field_kind` by directly using `aarch64_field` structs for AArch64 instruction operands. It introduces macro defines to map old enum names to the new struct values, facilitating a smoother transition. This change simplifies code readability by eliminating the need to cross-reference separate tables to determine opcode bit usage, addressing a long-standing issue with architecture complexity.
