---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- assembler
- opcode
discussion_id: 645db6b4-e603-79dc-6675-e5a3bfeb2006@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 05/28] aarch64: Fix incorrect F_ALIAS and F_HAS_ALIAS flags'
headline: 'aarch64: Fix incorrect F_ALIAS and F_HAS_ALIAS flags'
tldr: Corrects the `F_ALIAS` and `F_HAS_ALIAS` flags for various AArch64 instructions.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures accurate representation of instruction aliasing.
- Improves the correctness of opcode handling.
exchanges: []
primer_expert: The patch addresses flag assignments in `aarch64-asm-2.c`. It corrects
  the `F_HAS_ALIAS` and `F_ALIAS` flags for various opcodes. `F_HAS_ALIAS` is removed
  from instructions that do not have aliases and added to those that do, such as conditional
  branches (`b.c`), `msr` (immediate), and `sysl`. `F_ALIAS` is added to `smstart`,
  `smstop`, and GCS system instructions, accurately reflecting their aliasing behavior.
primer_glossary:
- term: F_ALIAS
  definition: A flag indicating that an opcode is an alias for another opcode.
- term: F_HAS_ALIAS
  definition: A flag indicating that an opcode has one or more aliases associated
    with it.
- term: b.c
  definition: A conditional branch instruction in AArch64.
- term: msr
  definition: Move to Special Register, an AArch64 instruction used to write to system
    registers.
- term: sysl
  definition: System instruction, likely for calling system service routines or managing
    system state in AArch64.
- term: smstart/smstop
  definition: Instructions related to Scalable Matrix Extension (SME) state management.
series_id: 'binutils:aarch64: fix incorrect f_alias and f_has_alias flags'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/645db6b4-e603-79dc-6675-e5a3bfeb2006@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch corrects the `F_ALIAS` and `F_HAS_ALIAS` flags for several AArch64 instructions in `aarch64-asm-2.c`. It removes `F_HAS_ALIAS` from instructions without aliases (like `dsb`, `wfet`, `wfit`), adds it to instructions that do have aliases (like `b.c`, `msr`, `sysl`), and adds `F_ALIAS` to instructions like `smstart`/`smstop` and GCS system instructions.
