---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- expression parser
- buffer overrun
- mri mode
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'Gas: Don''t allow single quote to go past eol'
tldr: Fixes a buffer overrun in the assembler's expression parser and corrects an
  MRI mode parsing error.
stakes: This patch improves the security and stability of the assembler by preventing
  buffer overruns and ensuring correct parsing of floating-point constants in MRI
  mode.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check to prevent incrementing `input_line_pointer` past the end of the line,
  which may have a negligible impact on performance.
- Corrects the parsing of floating-point numbers in MRI mode, ensuring correct assembly
  of code that uses this feature.
- Improves the security and stability of the assembler by preventing buffer overruns.
exchanges: []
primer_expert: The patch modifies `gas/expr.c` to fix two issues. The first prevents
  `operand()` from incrementing `input_line_pointer` past the end of the line when
  a single quote is encountered. The second corrects the handling of hex floating
  point constants in MRI mode, ensuring that `input_line_pointer` is not incremented
  prematurely. The `check_Scc_OszcOperations` function in `gas/config/tc-i386.c` is
  relevant to the first issue.
primer_general: 'The GNU assembler (gas) translates assembly language source code
  into machine code. The expression parser is responsible for evaluating expressions
  used in assembly code. This patch fixes two bugs in the expression parser: one that
  could cause a buffer overrun when a single quote character appears at the end of
  a line, and another that caused incorrect parsing of floating-point numbers in MRI
  mode (a specific assembly language dialect).'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch addresses two issues in the GNU assembler's (`gas`) expression parser (`expr.c`). It prevents a buffer overrun that occurs when a single quote character appears at the end of a line, and corrects an existing parsing error in MRI mode when handling hexadecimal floating-point constants. The buffer overrun fix prevents the assembler from reading past the end of a string, while the MRI mode fix ensures correct parsing of floating-point numbers.
