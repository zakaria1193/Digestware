---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- buffer overrun
- MRI mode
- expression parser
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'Gas: Don''t allow single quote to go past EOL'
tldr: Fixes a buffer overrun in the assembler's expression parser and an MRI mode
  parsing error.
stakes: Improves assembler stability and security by preventing buffer overruns and
  misparsing in specific edge cases.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Minimal performance impact.
- Improved code correctness and security.
primer_expert: This patch resolves two issues in the assembler's expression handling.
  An overrun could occur in `expr.c` if a single quote reached the end of the input
  buffer. The patch also fixes incorrect `input_line_pointer` handling when parsing
  MRI-style hex floats. MRI mode is an older assembly syntax.
primer_general: The GNU Assembler (`gas`) translates assembly code into machine code.
  The expression parser within the assembler evaluates expressions and converts them
  into numerical values.  This patch fixes two potential errors in the expression
  parser. The first prevents a buffer overrun, where the parser attempts to read past
  the end of the input line. The second fixes an error in how the assembler parses
  floating-point numbers in a specific, older assembly syntax called MRI mode.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch addresses two issues in the GNU assembler (`gas`). First, it fixes a buffer overrun in the `operand` function in `expr.c` that occurs when a single quote character reaches the end of the input line. Second, it corrects a parsing error in MRI mode related to hexadecimal floating-point constants. The patch prevents `input_line_pointer` from incrementing past the end of the line when a single quote is encountered and adjusts pointer increment for MRI mode hex floats.
