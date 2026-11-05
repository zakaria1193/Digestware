---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- disassembler
- refactoring
discussion_id: f5cf86cf-2080-bc0f-1f58-b171439d3fb2@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 19/28] aarch64: Use has_alias_list in print_find_real_opcode'
headline: 'aarch64: Use has_alias_list in print_find_real_opcode'
tldr: Refactors AArch64 real opcode lookup to use alias lists, simplifying code.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaces a complex data structure (`alias_info`) with a simpler list-based approach.
- Simplifies generation logic at the cost of reordering generated code and a slight
  increase in code size.
exchanges: []
primer_expert: Modifies `opcodes/aarch64-asm-2.c` to use a new mechanism (`has_alias_list`)
  for handling aliases within `print_find_real_opcode`, replacing the previous `alias_info`
  structure. This change simplifies the generation of the assembly code by processing
  alias lists in a forward order. Consequently, the order of `case` statements in
  the generated output may change, and shared case bodies are removed for clarity,
  resulting in a minor increase in code size but improved maintainability.
primer_glossary:
- term: has_alias_list
  definition: A data structure or mechanism used in the AArch64 disassembler to manage
    lists of opcodes that have aliases.
- term: alias_info
  definition: A data structure previously used in the AArch64 disassembler to store
    information about instruction aliases.
series_id: 'binutils:aarch64: use has_alias_list in print_find_real_opcode'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f5cf86cf-2080-bc0f-1f58-b171439d3fb2@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refactors the `print_find_real_opcode` function in `opcodes/aarch64-asm-2.c`, replacing the use of the `alias_info` structure with `has_alias_list`. This change simplifies the code generation for opcode lookups and reorders some case statements due to processing alias lists in forward order. The removal of shared case bodies adds a small amount of code but improves clarity. The disassembler behavior remains unchanged.
