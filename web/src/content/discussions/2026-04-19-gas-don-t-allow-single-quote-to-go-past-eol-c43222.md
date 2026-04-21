---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- expression
- buffer overrun
- fuzzing
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'gas: Don''t allow single quote to go past eol'
tldr: Fixes a buffer overrun and parsing error in the assembler's expression handling
  related to single quotes.
stakes: Prevents potential crashes or incorrect code generation due to malformed assembly
  code, enhancing security and reliability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check to prevent incrementing the input_line_pointer past the end of line,
  which has a neglible performance impact.
- Fixes a buffer overrun and a parsing error, increasing robustness and correctness.
- Does not introduce any new features.
exchanges: []
primer_expert: The patch modifies `gas/expr.c` to fix a buffer overrun and parsing
  error. The overrun occurred in `operand()` when a single quote was the last character
  on a line, causing `input_line_pointer` to increment past the end of the input buffer.
  The parsing error relates to MRI mode hexadecimal floating-point constants. The
  line `++input_line_pointer;` was removed before integer_constant call. MRI mode
  is a specific assembly syntax.
primer_general: The GNU Assembler (GAS) converts assembly code into machine code.  When
  parsing assembly code, the assembler needs to interpret expressions and operands
  correctly. This patch fixes two bugs in the assembler's expression handling logic.
  One bug involves a single quote character potentially causing the assembler to read
  beyond the end of a buffer. The second bug relates to how hexadecimal floating-point
  constants are parsed. The fixes prevent crashes and ensure that the assembler correctly
  translates assembly code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch addresses two issues found by fuzzing the GNU Assembler (GAS). First, it prevents a buffer overrun in `expr()` when a single quote character appears at the end of a line. Second, it corrects a parsing error in MRI mode related to hexadecimal floating-point constants. The overrun could lead to reading beyond the end of allocated memory, while the parsing error could result in incorrect code generation.
