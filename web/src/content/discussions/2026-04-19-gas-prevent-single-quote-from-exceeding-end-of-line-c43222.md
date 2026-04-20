---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- security
- fuzzing
- buffer overflow
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'Gas: Prevent single quote from exceeding end-of-line.'
tldr: The assembler now prevents single quotes from running past the end of a line,
  fixing a fuzzer-discovered buffer overrun.
stakes: Fixes a security vulnerability in the GNU Assembler (gas) that could lead
  to crashes or potentially arbitrary code execution.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check to prevent `input_line_pointer` from exceeding the line boundary.
- Corrects parsing of hexadecimal floating-point numbers in MRI mode.
- May slightly impact performance due to the added check (likely negligible).
primer_expert: The `operand` function in `gas/expr.c` incorrectly increments `input_line_pointer`
  when handling single quotes at the end of a line/statement, leading to a buffer
  overrun in `check_Scc_OszcOperations` within `tc-i386.c`. MRI mode hex float parsing
  also had an issue.  The fix ensures `input_line_pointer` stays within bounds.
primer_general: The GNU Assembler (gas) translates assembly language source code into
  object code. This involves lexical analysis, parsing, and code generation. During
  parsing, the assembler evaluates expressions, and this patch fixes a vulnerability
  where a malformed expression with a single quote can cause the assembler to read
  beyond the end of a buffer. This is a security concern, as it can lead to crashes
  or potentially arbitrary code execution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch addresses a buffer overrun vulnerability found by fuzzers in the GNU Assembler (gas).  The issue occurs when a single quote character extends beyond the end of a line during expression parsing.  The patch also corrects a separate parsing error related to hexadecimal floating-point numbers in MRI mode.
