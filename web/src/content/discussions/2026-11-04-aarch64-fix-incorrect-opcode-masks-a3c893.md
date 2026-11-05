---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- opcode
discussion_id: 3f1a862a-9991-8cdc-7642-ced8bfa4132f@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 06/28] aarch64: Fix incorrect opcode masks'
headline: 'aarch64: Fix incorrect opcode masks'
tldr: Corrects overly permissive masks for `ldp`/`stp` and `stllrh` opcodes.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves the accuracy of opcode definitions.
- Maintains existing decode behavior due to table ordering.
exchanges: []
primer_expert: The patch addresses inaccuracies in opcode masks within `aarch64-dis-2.c`.
  Specifically, the masks for `ldp`/`stp` (offset variants) and `stllrh` were too
  broad. While the fixes don't change the current disassembly output because of the
  opcode table's priority ordering (meaning more specific entries are matched first),
  they correct the underlying definitions of these instructions' bit patterns.
primer_glossary:
- term: opcode mask
  definition: A bitmask used to selectively extract or check specific bits within
    an instruction's binary representation (opcode) to identify the instruction or
    its variant.
- term: ldp/stp
  definition: Load-Pair and Store-Pair instructions in ARM architecture, used to load
    or store two registers with a single instruction.
- term: stllrh
  definition: Store-Linked-Register-Half, likely an AArch64 instruction for atomic
    operations on half-words.
series_id: 'binutils:aarch64: fix incorrect opcode masks'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/3f1a862a-9991-8cdc-7642-ced8bfa4132f@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch corrects the opcode masks for `ldp`/`stp` (offset) and `stllrh` in `aarch64-dis-2.c`. The previous masks were too lax, but fixing them does not alter decode behavior due to the priority of earlier opcode table entries. These corrections ensure that the masks accurately reflect the intended instruction encodings, preventing potential ambiguities.
