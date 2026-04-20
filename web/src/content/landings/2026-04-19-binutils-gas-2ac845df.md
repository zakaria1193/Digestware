---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- assembler
- security
- fuzzing
- buffer-overrun
commit_hash: 2ac845df73237ba29cef128fbee5dafe1e74a72e
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'gas: Prevent Single Quote from Exceeding End-of-Line.'
tldr: The assembler now prevents a single quote from running past the end of a line,
  fixing a buffer overrun vulnerability.
why_it_matters: This change fixes a potential security vulnerability where a crafted
  input file could cause a buffer overrun during assembly, leading to a crash or arbitrary
  code execution.
impact_score: 8
impact_rationale: Fixes a buffer overrun vulnerability found via fuzzing.
performance_win: false
breaking_change: false
outcome: committed
primer: The GNU Assembler (gas) translates assembly code into machine code. MRI mode
  is a specific input mode. This commit focuses on preventing buffer overruns, which
  are a class of vulnerability where a program writes data beyond the allocated boundary
  of a buffer.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260419230946.1FF154BA23D0@sourceware.org
date: '2026-04-19'
---

The assembler's `operand` function was vulnerable to a buffer overrun when a single quote appeared at the end of a line. This commit prevents the `input_line_pointer` from incrementing past the end of the line/statement when a single quote is encountered. It also fixes another parsing error related to MRI mode.
