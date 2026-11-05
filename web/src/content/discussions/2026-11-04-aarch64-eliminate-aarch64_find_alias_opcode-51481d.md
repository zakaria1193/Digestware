---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- refactoring
discussion_id: 550dfda0-a274-d896-cf52-0a1c973d39c7@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 10/28] aarch64: Eliminate aarch64_find_alias_opcode'
headline: 'aarch64: Eliminate aarch64_find_alias_opcode'
tldr: Merges `aarch64_find_alias_opcode` into `aarch64_find_next_alias_opcode` for
  simplification.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Reduces code duplication by merging similar functionalities.
- Simplifies the codebase.
exchanges: []
primer_expert: The patch consolidates alias lookup in `aarch64-dis-2.c` by merging
  `aarch64_find_alias_opcode` into `aarch64_find_next_alias_opcode`. This eliminates
  a separate function dedicated to initial alias mappings, streamlining the process
  of finding the next opcode in an alias chain.
primer_glossary: []
series_id: 'binutils:aarch64: eliminate aarch64_find_alias_opcode'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/550dfda0-a274-d896-cf52-0a1c973d39c7@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch eliminates the `aarch64_find_alias_opcode` function by merging its initial alias mappings into `aarch64_find_next_alias_opcode`. This change simplifies the AArch64 disassembler code by consolidating alias lookup logic into a single function, reducing redundancy.
