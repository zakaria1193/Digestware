---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- instruction
- architecture
- FEAT_RLCS
discussion_id: 20261102132956.53418-1-muhammad.kamran@arm.com
source_type: public_inbox
title: 'aarch64: Add FEAT_RLCS HINT aliases'
headline: 'aarch64: Add FEAT_RLCS HINT aliases'
tldr: Adds aliases for FEAT_RLCS system instructions SLBND and SRLS to the AArch64
  assembler.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the assembler's instruction parsing and disassembly logic to
  support new instruction variants and optional operands.
- Enables support for newer hardware features, potentially improving performance or
  enabling new capabilities for AArch64 users.
exchanges:
- author: Muhammad Kamran <muhammad.kamran@arm.com>
  role: proposer
  position: Adds new aliases and operand kinds for AArch64 FEAT_RLCS instructions
    SLBND and SRLS to the assembler.
  quote: 'Add the SLBND and SRLS system instruction aliases from FEAT_RLCS.


    SRLS has an optional STSHSTRM operand, so add a dedicated

    hint operand kind for the optional syntax and for disassembly.'
primer_expert: This change adds support for new AArch64 architectural extensions,
  specifically FEAT_RLCS (Release Consistency Extension). It introduces assembler
  aliases for the `SLBND` (Stash List Boundary) and `SRLS` (Stash Record List) instructions.
  Crucially, it handles the optional operand for `SRLS`, `STSHSTRM`, by defining new
  operand types to ensure correct parsing and disassembly of this specific instruction
  variant.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, used in many modern mobile devices and
    servers.
- term: FEAT_RLCS
  definition: A specific AArch64 architectural feature extension related to Release
    Consistency, likely improving memory ordering and synchronization primitives.
- term: SLBND
  definition: A system instruction related to Release Consistency, likely used to
    manage boundaries for stashed data or operations.
- term: SRLS
  definition: A system instruction related to Release Consistency, possibly used for
    stashing records in a list.
- term: STSHSTRM
  definition: An optional operand for the SRLS instruction, likely related to streaming
    or batching operations for stashed data.
- term: assembler
  definition: A program that converts human-readable assembly language code into machine
    code that a computer can execute.
- term: disassembly
  definition: The process of converting machine code back into assembly language,
    often used for reverse engineering or debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261102132956.53418-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This patch introduces aliases for the `SLBND` and `SRLS` system instructions, which are part of the FEAT_RLCS feature for AArch64. It also adds specific handling for the optional `STSHSTRM` operand of the `SRLS` instruction, including dedicated operand kinds for syntax and disassembly.
