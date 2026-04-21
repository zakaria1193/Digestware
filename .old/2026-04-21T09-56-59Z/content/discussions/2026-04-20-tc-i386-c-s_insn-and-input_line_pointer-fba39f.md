---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- x86
- instruction
- pointer
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: Tc-i386.c s_insn and input_line_pointer
tldr: Restores `input_line_pointer` in `s_insn` to prevent accessing a wild pointer
  when handling invalid instructions.
stakes: This fix prevents a potential crash or undefined behavior in the assembler
  when processing invalid x86 instructions.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a line of code to restore `input_line_pointer`, which may have a negligible
  impact on performance.
- Prevents a potential crash or undefined behavior, improving the robustness of the
  assembler.
- The fix is specific to the x86 architecture.
exchanges: []
primer_expert: The `tc-i386.c` file contains target-specific code for the x86 architecture
  in the GNU assembler. The `s_insn` function parses x86 instructions. The `input_line_pointer`
  variable points to the current location in the input line being processed. This
  patch ensures that `input_line_pointer` is properly restored even when the code
  jumps to a `bad:` label, preventing potential out-of-bounds reads in `ignore_rest_of_line()`.
primer_general: The GNU assembler (gas) translates assembly language source code into
  machine code. When an error occurs during assembly, the assembler needs to be able
  to recover and continue processing the input file. This patch fixes a bug in the
  x86-specific code that could cause the assembler to crash or behave unpredictably
  when encountering an invalid instruction.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch corrects an issue in the x86-specific code of the GNU assembler (`gas/config/tc-i386.c`) where the `input_line_pointer` was not always restored after an error in the `s_insn` function. This could lead to `ignore_rest_of_line()` accessing an invalid memory location. The patch restores `input_line_pointer` to its saved value to prevent this issue.
