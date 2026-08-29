---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- assembler
- disassembler
discussion_id: 20260827151014.9719-2-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH 1/7] aarch64: add PAuth_LR instructions belonging to NOP space'
headline: 'aarch64: add PAuth_LR instructions belonging to NOP space'
tldr: Adds the 'pacm' instruction, which is part of the PAuth_LR feature but resides
  in the NOP space, along with its test cases.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Allows `pacm` to be used without explicitly enabling the `+pauth-lr` feature, simplifying
  its adoption but potentially obscuring its security context.
exchanges: []
primer_expert: The patch adds support for the `pacm` instruction to binutils for the
  AArch64 architecture. `pacm` is an instruction related to the FEAT_PAuth_LR (Pointer
  Authentication for Link Register) feature. However, unlike other PAuth_LR instructions,
  `pacm` is defined to fall within the NOP (No Operation) instruction encoding space.
  This means it can be assembled and disassembled without explicitly enabling the
  `+pauth-lr` feature. The patch updates opcode tables and adds gas test suite entries
  for `pacm`. This is likely the first functional patch in the series, setting up
  a foundational instruction.
primer_glossary:
- term: PAuth_LR
  definition: Pointer Authentication for the Link Register. A security feature in
    ARM architectures that protects the Link Register (LR) from being tampered with.
- term: NOP space
  definition: A range of instruction encodings that are designated as 'No Operation'
    instructions. These instructions typically do nothing but consume CPU cycles.
    Instructions falling into this space can sometimes be added without breaking compatibility
    or requiring new feature flags.
- term: pacm
  definition: An AArch64 instruction related to Pointer Authentication, specifically
    within the PAuth_LR feature set. It resides in the NOP instruction space.
- term: FEAT_PAuth_LR
  definition: A specific AArch64 hardware feature extension for Pointer Authentication
    of the Link Register.
series_id: 'binutils:aarch64: add pauth_lr instructions belonging to nop space'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827151014.9719-2-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch introduces the `pacm` instruction to the AArch64 assembler and disassembler. Although `pacm` is part of the PAuth_LR feature set, it is located within the NOP (No Operation) instruction space and does not require explicit feature declaration. The change includes the addition of relevant test cases to ensure proper functionality.
