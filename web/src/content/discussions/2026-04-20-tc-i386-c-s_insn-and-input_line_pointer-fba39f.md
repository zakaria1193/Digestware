---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- i386
- input_line_pointer
- crash
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: tc-i386.c s_insn and input_line_pointer
tldr: Restores `input_line_pointer` in `s_insn` to prevent accessing a wild pointer
  after an error, fixing a potential crash in the assembler.
stakes: This patch improves the stability of the assembler by preventing it from accessing
  invalid memory locations, which could lead to crashes or incorrect assembly.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a line of code to restore `input_line_pointer`, which has minimal performance
  impact.
- Prevents a potential crash, improving the stability of the assembler.
exchanges: []
primer_expert: The patch modifies `gas/config/tc-i386.c`, specifically the `s_insn`
  function which is used to parse Intel instruction syntax. The `input_line_pointer`
  variable points to the current position in the input line being processed.  When
  an error occurs, the code jumps to the `bad` label.  The patch ensures that `input_line_pointer`
  is restored to its saved value before calling `ignore_rest_of_line()`, which consumes
  the remainder of the line.
primer_general: The GNU Assembler (GAS) translates assembly language into machine
  code.  During this process, the assembler keeps track of its current position in
  the input file using a pointer. This patch fixes a bug in the assembler's handling
  of Intel assembly code where, after encountering an error in an instruction, the
  pointer to the current position in the line was not correctly reset. This could
  cause the assembler to read from an invalid memory location, potentially leading
  to a crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch corrects an issue in the i386-specific code of the GNU Assembler (GAS).  A comment indicated that `input_line_pointer` was always restored by the caller, but this was not always the case. After a syntax error in a .insn directive, `input_line_pointer` was not properly reset, leading to `ignore_rest_of_line()` accessing a wild pointer. This patch restores `input_line_pointer` to its correct value in the `s_insn <bad>` error handling path.
