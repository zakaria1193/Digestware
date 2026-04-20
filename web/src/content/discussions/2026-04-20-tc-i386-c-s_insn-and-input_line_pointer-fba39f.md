---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- i386
- wild pointer
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: Tc-i386.c s_insn and input_line_pointer
tldr: Fixes a potential wild pointer access in the i386 assembler by restoring `input_line_pointer`
  in `s_insn`.
stakes: Improves the stability of the assembler and prevents crashes when processing
  malformed or invalid assembly code.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a line of code to restore `input_line_pointer`, slightly increasing code complexity.
- Improves stability by preventing a potential crash.
- Addresses a potential security vulnerability.
primer_expert: This patch focuses on the i386 target code in the assembler (`gas/config/tc-i386.c`).
  It corrects an issue with `input_line_pointer` not being properly restored in an
  error handling path within the `s_insn` function. This prevents `ignore_rest_of_line()`
  from accessing an invalid memory location.
primer_general: The GNU Assembler (`gas`) translates assembly language code into object
  code. The `input_line_pointer` variable tracks the current position in the input
  line being processed. This patch ensures that the `input_line_pointer` is correctly
  restored after an error, preventing potential crashes due to the assembler trying
  to read from an invalid memory location.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a potential issue in the i386 assembler (`gas`) where the `input_line_pointer` is not always restored, leading to a wild pointer access in `ignore_rest_of_line()`. The patch restores `input_line_pointer` in the `s_insn <bad>` error handling case in `tc-i386.c`.
