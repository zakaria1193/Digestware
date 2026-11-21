---
project: binutils
subsystem: binutils
patch_id: null
tags:
- RISC-V
- Zibi
- extension
- binutils
- compiler
discussion_id: 23bdc12b-7130-470a-b527-c7b2c14c0dd1@gmail.com
source_type: public_inbox
title: Zibi Extension for RISC-V
headline: Zibi Extension for RISC-V
tldr: Binutils is preparing to include the Zibi extension for RISC-V, which adds new
  compare-and-branch instructions.
proposer: Jeff Law <jeffreyalaw@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds new functionality for RISC-V development.
- Requires careful testing to ensure correct instruction encoding and decoding.
exchanges:
- author: Jeff Law <jeffreyalaw@gmail.com>
  role: proposer
  position: Submits a patch for the Zibi RISC-V extension for review and inclusion
    in binutils, noting that he is functioning as a reviewer for Kito's work.
  quote: "Given it's Kito's patch I'm really functioning as the reviewer here, but\
    \ \nit's also the case that I don't think he's officially submitted for \ninclusion\
    \ into binutils."
primer_expert: The Zibi extension for RISC-V adds instructions for comparing a register
  against a small immediate constant and conditionally branching. This patch integrates
  support for these instructions into binutils, extending its RISC-V toolchain capabilities.
primer_glossary:
- term: Zibi extension
  definition: A proposed extension for the RISC-V ISA that introduces compare-and-branch
    instructions.
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/23bdc12b-7130-470a-b527-c7b2c14c0dd1@gmail.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch introduces the Zibi extension for RISC-V to binutils. The Zibi extension adds two new instructions that compare a small constant against a register and branch based on the result. The submission is a review of a patch originally from Kito, with Jeff Law acting as the reviewer and preparing to commit it.
