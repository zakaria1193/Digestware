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
discussion_id: 1688058d-d6a1-9c20-6e8c-4ce70247a5ad@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 26/28] aarch64: Add non-F_CONV aliases to the decode tree'
headline: 'aarch64: Add non-F_CONV aliases to the decode tree'
tldr: Patch integrates non-F_CONV instruction aliases into the aarch64 disassembler's
  decode tree for efficiency.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improved disassembly efficiency by integrating aliases into the main decode tree.
- Enabled support for overlapping opcodes and complex alias relationships.
exchanges: []
primer_expert: This patch reorganizes the aarch64 disassembler's opcode lookup mechanism.
  Previously, some aliased instructions required a separate step (`determine_disassembling_preference`)
  after an initial lookup. This change integrates all non-`F_CONV` (Format Convert)
  aliases directly into the main opcode decision tree. This streamlines the lookup
  process, potentially improving performance and simplifying the handling of instructions
  with overlapping encodings and alias relationships, paving the way for more complex
  alias support.
primer_glossary:
- term: decode tree
  definition: An internal data structure used by disassemblers to efficiently map
    instruction bit patterns to their corresponding symbolic names and properties.
- term: alias
  definition: In this context, an instruction that is a variation or shorthand for
    another, often differing in a few bits that control its specific behavior or target.
- term: F_CONV
  definition: Likely a flag indicating a format conversion instruction or an instruction
    that requires special handling related to data format conversion.
- term: F_HAS_ALIAS
  definition: A flag indicating that an opcode has one or more aliases.
- term: HINTE
  definition: Possibly a type of hint instruction in the ARM architecture.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set.
series_id: 'binutils:aarch64: add non-f_conv aliases to the decode tree'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/1688058d-d6a1-9c20-6e8c-4ce70247a5ad@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch integrates non-F_CONV instruction aliases into the aarch64 disassembler's binary decision tree. This change aims to improve efficiency by allowing more opcode lookups to be resolved directly within the tree, rather than relying on a separate alias conversion step. It also enables handling of overlapping opcodes marked `F_HAS_ALIAS` by removing dependencies on table order, which is necessary for future support of HINTE aliases.
