---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- i386
- input_line_pointer
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: tc-i386.c s_insn and input_line_pointer
tldr: This patch fixes a bug in the i386 assembler backend where the input line pointer
  is not correctly restored, potentially leading to a crash.
stakes: Fixes a potential crash in the assembler, improving reliability and preventing
  misassembly of code.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a line of code to restore the `input_line_pointer`.
- Prevents a potential crash and improves the reliability of the assembler.
exchanges: []
primer_expert: The `input_line_pointer` in `gas` tracks the current position within
  the assembly source code being processed. This patch fixes a case in `gas/config/tc-i386.c`
  where the `input_line_pointer` was not correctly restored on error within the `s_insn`
  function. Specifically the `bad:` label.
primer_general: The GNU Assembler (`gas`) translates assembly code into machine code.
  It reads the assembly source code line by line, keeping track of the current position
  with a pointer. This patch fixes a bug within the i386-specific part of the assembler.
  The bug occurs when the assembler encounters an error and has to discard the rest
  of the current line. The patch ensures that the pointer to the current position
  in the line is correctly reset, preventing it from pointing to an invalid memory
  location and causing a crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

Alan Modra addresses a bug in the i386-specific code within the GNU Assembler (`gas`). The patch corrects an issue where the `input_line_pointer` is not always restored correctly in the `s_insn` function, which can lead to a wild pointer access when `ignore_rest_of_line()` is called. The patch restores the `input_line_pointer` to its saved value, preventing the crash.
