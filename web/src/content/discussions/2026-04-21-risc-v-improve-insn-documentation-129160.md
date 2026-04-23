---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- documentation
- insn directive
- mapping symbols
discussion_id: d7fff964-1b92-4e78-9801-b9dbb139f4b3@suse.com
source_type: public_inbox
title: '[PATCH 01/19] RISC-V: improve .insn documentation'
headline: 'RISC-V: improve .insn documentation'
tldr: The `.insn` directive in RISC-V assembly does not permit a comma after the type,
  and the documentation is updated to reflect the use of mapping symbols.
stakes: Ensures accurate documentation of the `.insn` directive, which is crucial
  for developers using this feature to represent instructions numerically.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved accuracy of the `.insn` directive documentation.
- Clarification of syntax rules.
- Updated information on mapping symbols.
exchanges: []
primer_expert: This patch modifies `gas/doc/c-riscv.texi` to improve the documentation
  of the `.insn` directive. It clarifies the syntax of the "type" form and updates
  the text related to `.word` and mapping symbols, reflecting the current state of
  the RISC-V assembler.
primer_general: The `.insn` directive in assembly languages like RISC-V allows representing
  instructions numerically. This patch updates the documentation for this directive,
  clarifying its syntax and reflecting current practices in the RISC-V assembler.
  Accurate documentation is important for developers to correctly use the `.insn`
  directive and understand how instructions are encoded.
series_id: 'binutils:risc-v: improve .insn documentation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d7fff964-1b92-4e78-9801-b9dbb139f4b3@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves the documentation for the `.insn` directive in the RISC-V assembly language. It clarifies that the "type" form of `.insn` does not permit a comma after the type. The patch also updates the documentation related to `.word` and mapping symbols.
