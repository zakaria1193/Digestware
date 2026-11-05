---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- code generation
- refactoring
- globals
discussion_id: ef6eb523-6ad6-a8c6-22e7-d42228e1b134@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 16/28] aarch64: Eliminate global opcode_nodes_heads list'
headline: 'aarch64: Eliminate global opcode_nodes_heads list'
tldr: Removes global state from AArch64 opcode table processing.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces global state, improving modularity and testability.
- Requires passing list pointers as arguments, slightly increasing function signature
  complexity.
exchanges: []
primer_expert: Removes the global `opcode_nodes_head` from `opcodes/aarch64-gen.c`.
  The list of opcode nodes, previously managed by this global variable, is now passed
  as a parameter to functions like `read_table` and `divide_table`. This promotes
  a more functional style by reducing reliance on global mutable state, making the
  code more self-contained and easier to test or integrate.
primer_glossary: []
series_id: 'binutils:aarch64: eliminate global opcode_nodes_heads list'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ef6eb523-6ad6-a8c6-22e7-d42228e1b134@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refactors `opcodes/aarch64-gen.c` to eliminate the global `opcode_nodes_head` variable. The linked list of opcode nodes is now passed as a local variable throughout the relevant functions, such as `read_table` and `divide_table`. This change reduces reliance on global state, making the code more modular and easier to reason about. It also removes an unnecessary empty node at the head of the list.
