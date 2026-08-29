---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- assembler
- disassembler
discussion_id: 20260827151014.9719-5-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH 4/7] aarch64: add PAuth_LR instructions with no or one-register operand'
headline: 'aarch64: add PAuth_LR instructions with no or one-register operand'
tldr: Adds support for AArch64 PAuth_LR instructions that take no operands or a single
  register operand, including new register types and tests.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introduces a new register type 'R' to enforce correct instruction usage, potentially
  adding complexity to the parser but improving correctness.
exchanges: []
primer_expert: This patch extends the AArch64 assembler and disassembler support for
  the Pointer Authentication (PAuth) extension, specifically the PAuth_LR feature.
  It adds support for instructions that authenticate the Link Register (LR) using
  SP or XZR registers as diversifiers. The patch defines new instruction mnemonics
  and their encodings, a new register type `R` to constrain operand usage (preventing
  SP/XZR with certain instructions), and includes relevant test cases in `gas/testsuite`.
  The `CI-tag:skip` indicates this patch is part of a series where intermediate commits
  might not be independently bu…
primer_glossary:
- term: FEAT_PAuth_LR
  definition: A specific AArch64 hardware feature extension related to Pointer Authentication,
    which enhances security by signing or authenticating the Link Register (LR).
- term: PAuth_LR
  definition: Pointer Authentication for the Link Register. This feature uses special
    instructions to protect the LR register from being tampered with, typically used
    in security-sensitive code.
- term: SP
  definition: Stack Pointer. A special-purpose register in ARM architectures that
    holds the address of the current top of the stack.
- term: XZR
  definition: Zero Register in AArch64. This register always returns 0 when read and
    has no effect when written to. It's often used as a null operand.
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language code into machine code.
series_id: 'binutils:aarch64: add pauth_lr instructions with no or one-register operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827151014.9719-5-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch introduces support for AArch64 FEAT_PAuth_LR instructions that operate with zero or one register operand. It adds new instruction mnemonics like `paci<k>sppc`, `pacnbi<k>sppc`, `auti<k>171615`, and their register variants (`autisppcr`, `retisppcr`). A new register type `R` is defined to prevent misuse of SP or XZR registers. The changes include corresponding gas assembler configurations and test cases.
