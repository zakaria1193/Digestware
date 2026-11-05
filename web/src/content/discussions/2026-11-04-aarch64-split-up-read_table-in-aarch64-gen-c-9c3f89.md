---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- opcode
discussion_id: 62eae559-16e2-b063-5236-5c74f445101e@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 14/28] aarch64: Split up read_table() in aarch64-gen.c'
headline: 'aarch64: Split up read_table() in aarch64-gen.c'
tldr: Refactors opcode table validation by extracting it into a new function.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improved code organization and maintainability.
- Ensured comprehensive validation of opcode table entries.
exchanges: []
primer_expert: This patch modifies `aarch64-gen.c` to improve the organization of
  opcode table parsing and validation. By separating validation into `validate_table()`,
  the code becomes more modular and readable. It also corrects the handling of aliases
  during validation, ensuring all opcodes are checked.
primer_glossary: []
series_id: 'binutils:aarch64: split up read_table() in aarch64-gen.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/62eae559-16e2-b063-5236-5c74f445101e@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refactors the `read_table()` function in `aarch64-gen.c` by splitting out the validation logic into a new `validate_table()` function. It also ensures that validation is not skipped for aliases. The results of `initialize_decoder_tree()` are moved and inlined into the correct `if` block as they are only used when emitting `aarch64-dis-2.c`.
