---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- i386
- input_line_pointer
- crash fix
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: 'Gas/i386: Restore input_line_pointer in s_insn'
tldr: Restores `input_line_pointer` in `s_insn` in `tc-i386.c` to prevent `ignore_rest_of_line()`
  from accessing a wild pointer.
stakes: Fixes a potential crash in the i386 assembler due to incorrect handling of
  the input line pointer, improving stability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Minimal performance impact.
- Improved code correctness.
primer_expert: The patch corrects an error in `gas/config/tc-i386.c`'s `s_insn` function,
  which is part of the i386 target's opcode parsing logic. The `input_line_pointer`
  was not always restored to its original value before calling `ignore_rest_of_line()`,
  leading to potential memory corruption. The fix ensures that after a parsing error,
  the input stream is correctly positioned for subsequent processing, essential for
  robust assembly.
primer_general: The GNU Assembler (gas) translates assembly language into machine
  code. When assembling code for the Intel x86 architecture, the `tc-i386.c` file
  contains target-specific code for parsing and processing x86 instructions. The `input_line_pointer`
  variable keeps track of the current position in the input assembly source code line.
  This patch ensures that this pointer is correctly managed, so that error handling
  routines can safely process the remainder of the line, preventing crashes due to
  memory corruption.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a case in the i386 assembler (`gas/config/tc-i386.c`) where the `input_line_pointer` is not properly restored in the `s_insn` function. This can lead to `ignore_rest_of_line()` accessing an invalid memory location, resulting in a crash.  The patch restores the `input_line_pointer` to its saved value before calling `ignore_rest_of_line()`. The original code comment incorrectly claimed that the caller always handled the restore.
