---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- performance
discussion_id: 733b2101-300e-981f-767a-9120bb1dc01a@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 09/28] aarch64: Don''t decode aliased instructions twice'
headline: 'aarch64: Don''t decode aliased instructions twice'
tldr: Fixes redundant decoding of aliased instructions in the AArch64 disassembler.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Eliminates redundant decoding, improving disassembler efficiency.
- Simplifies the alias resolution logic.
exchanges: []
primer_expert: The patch corrects an inefficiency in `aarch64-dis-2.c`. When decoding
  an aliased instruction, the `aarch64_find_next_alias_opcode` function's chain might
  terminate by returning the base opcode itself. This can cause `determine_disassembling_preference`
  to perform a second, unnecessary decode of the base opcode. By removing the base
  opcode from the alias mappings, this redundant step is avoided.
primer_glossary: []
series_id: 'binutils:aarch64: don''t decode aliased instructions twice'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/733b2101-300e-981f-767a-9120bb1dc01a@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the AArch64 disassembler where aliased instructions could be decoded twice. The `aarch64_find_next_alias_opcode` function previously returned the base opcode at the end of an alias chain. This led to unnecessary second decodes when `determine_disassembling_preference` was called. The fix removes the aliased opcode from the alias list to prevent this redundant decoding.
