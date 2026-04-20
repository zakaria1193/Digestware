---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- assembler
- security
- fuzzing
- buffer overrun
commit_hash: 2ac845df73237ba29cef128fbee5dafe1e74a72e
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Gas now prevents single quotes from running past end-of-line.
tldr: The assembler now prevents single quotes from continuing past the end of a line,
  fixing potential buffer overruns.
why_it_matters: This prevents a potential buffer overrun when handling single quotes
  at the end of a line, improving robustness against malformed assembly code.
impact_score: 7
impact_rationale: Fixes a potential buffer overrun vulnerability.
performance_win: false
breaking_change: false
outcome: committed
primer: The assembler (gas) translates assembly language source code into object code.
  The `input_line_pointer` is a pointer that keeps track of the current position within
  the line of assembly code being processed.  A buffer overrun occurs when a program
  writes data beyond the allocated boundary of a buffer.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260419230946.1FF154BA23D0@sourceware.org
date: '2026-04-19'
---

The gas assembler's `operand` function in `expr.c` now checks for single quotes at the end of a line and avoids incrementing the `input_line_pointer` past the end of the line or statement. This fixes a potential buffer overrun vulnerability. Also, it fixes a parsing error related to MRI mode hexadecimal floats.
