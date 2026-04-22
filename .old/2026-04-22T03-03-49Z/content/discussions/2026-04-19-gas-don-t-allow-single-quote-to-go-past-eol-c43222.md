---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- fuzzing
- buffer overrun
- parsing
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'gas: Don''t allow single quote to go past eol'
tldr: 'This patch fixes two parsing errors in the assembler: preventing a buffer overrun
  with single quotes and correcting hex float handling in MRI mode.'
stakes: This patch improves the robustness and security of the assembler by preventing
  buffer overruns and correcting parsing errors.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds checks to prevent the `input_line_pointer` from going past the end of the line,
  which may have a small performance impact.
- Corrects a parsing error in MRI mode, potentially affecting the accuracy of assembled
  code in that mode.
- Improves the robustness and security of the assembler by preventing buffer overruns.
exchanges: []
primer_expert: The patch modifies `gas/expr.c`. It ensures that the `input_line_pointer`
  is not incremented past the end of the line or statement when a single quote is
  encountered. It also corrects how the `input_line_pointer` is incremented when parsing
  hexadecimal floating-point numbers in MRI mode. The `is_end_of_stmt` function is
  used to check for the end of the line or statement.
primer_general: The GNU Assembler (GAS) converts assembly language into machine code.
  During this process, the assembler parses the input file, interpreting the various
  instructions and data. This patch fixes two bugs in the assembler's parsing logic.
  One bug could cause the assembler to read beyond the end of a line when processing
  a single quote, potentially leading to a crash. The other bug affected how the assembler
  handled certain types of numbers in a specific mode (MRI mode), potentially leading
  to incorrect assembly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch addresses two issues in the GNU Assembler (GAS). First, it prevents a buffer overrun in the `expr()` function when a single quote character appears at the end of a line. Second, it corrects a parsing error in MRI mode when handling hexadecimal floating-point numbers. These issues were discovered through fuzzing.
