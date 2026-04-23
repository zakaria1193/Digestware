---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- .insn directive
- documentation
discussion_id: d7fff964-1b92-4e78-9801-b9dbb139f4b3@suse.com
source_type: public_inbox
title: '[PATCH 01/19] RISC-V: improve .insn documentation'
headline: 'RISC-V: Improve .insn documentation'
tldr: Corrects and updates the documentation for the .insn directive in the RISC-V
  assembler.
stakes: Ensures accurate and up-to-date documentation, reducing confusion and improving
  the usability of the .insn directive.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- No functional changes, purely documentation updates.
- Requires careful review to ensure accuracy and clarity.
exchanges: []
primer_expert: This patch modifies `gas/doc/c-riscv.texi`, which is the source file
  for the RISC-V assembler's documentation. The changes focus on clarifying the syntax
  and usage of the `.insn` directive, which allows embedding raw instruction encodings
  directly. The update addresses inaccuracies in the documentation regarding comma
  usage and the interaction with mapping symbols.
primer_general: The RISC-V assembler translates assembly code into machine code.  The
  `.insn` directive allows embedding raw instruction encodings directly into assembly.
  Mapping symbols associate addresses with code or data, letting debuggers correlate
  machine code with source code. This patch improves the documentation for the `.insn`
  directive, ensuring developers have correct information about its syntax and how
  it interacts with other assembler features, like mapping symbols. Accurate documentation
  is crucial for effective use of assembly language features.
series_id: 'binutils:risc-v: improve .insn documentation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d7fff964-1b92-4e78-9801-b9dbb139f4b3@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves the documentation for the `.insn` directive in the RISC-V assembler. It clarifies that a comma is not permitted after the type specifier in the `.insn` directive, and updates the text related to `.word` usage and mapping symbols in assembly code. The goal is to provide more accurate and helpful information to developers using the `.insn` directive.
