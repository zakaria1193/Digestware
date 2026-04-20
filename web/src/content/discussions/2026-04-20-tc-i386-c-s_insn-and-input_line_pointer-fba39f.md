---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- i386
- parsing
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: tc-i386.c s_insn and input_line_pointer
tldr: This patch fixes a wild pointer access in the i386 assembler by ensuring `input_line_pointer`
  is properly restored after an error.
stakes: Prevents potential crashes or undefined behavior in the assembler when processing
  invalid i386 assembly code.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch fixes a potential memory safety issue, and the proposed
  solution is simple and direct.
technical_tradeoffs:
- Adds a line of code to restore a pointer, which might slightly increase assembly
  time in error cases.
primer: The GNU Assembler (gas) translates assembly language into machine code. The
  `input_line_pointer` variable keeps track of the current position in the input assembly
  source code being processed. The `ignore_rest_of_line()` function skips the remaining
  characters on the current line after an error.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch corrects an issue in the i386 assembler where the `input_line_pointer` was not always restored correctly after an error in the `s_insn` function. This could lead to `ignore_rest_of_line()` accessing an invalid memory location. The patch restores `input_line_pointer` to the saved value.
