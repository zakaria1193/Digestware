---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- fuzzing
- security
- MRI mode
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'gas: Don''t allow single quote to go past eol'
tldr: This patch fixes vulnerabilities in the assembler related to single quotes and
  MRI mode float parsing, preventing crashes and misassembly.
stakes: Improves the security and reliability of the assembler by preventing buffer
  overruns and ensuring correct parsing of floating-point constants.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check to prevent reading past the end of the line, which may slightly impact
  performance.
- Corrects parsing of MRI-style floating-point constants.
- Improves security and reliability of the assembler.
exchanges: []
primer_expert: This patch fixes two issues in `gas/expr.c`. The first prevents `operand()`
  from reading past the end of the input line when a single quote is the last character.
  The second fixes incorrect handling of MRI-style hexadecimal floating-point constants,
  where the `input_line_pointer` was incorrectly incremented *before* parsing the
  constant.
primer_general: The GNU Assembler (`gas`) translates assembly code into machine code.
  The `expr.c` file handles parsing expressions within the assembly code. This patch
  fixes two bugs in the expression parsing logic. One bug involves how the assembler
  handles single quotes, preventing it from reading past the end of a line. The other
  bug corrects how floating-point numbers are parsed in a specific mode (MRI mode),
  ensuring they are interpreted correctly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

Alan Modra submits a patch that addresses two issues in the GNU Assembler (`gas`). The first fix prevents a buffer overrun when a single quote character reaches the end of a line. The second fix corrects a parsing error in MRI mode when handling hexadecimal floating-point constants. These issues were discovered through fuzzing.
