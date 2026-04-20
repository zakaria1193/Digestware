---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- security
- buffer overrun
- MRI mode
discussion_id: aeVZgev2g-i7gtDy@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: don''t allow single quote to go past eol'
headline: 'gas: don''t allow single quote to go past eol'
tldr: This patch fixes a buffer overrun in the assembler (gas) when a single quote
  appears at the end of a line, and corrects MRI mode hex float parsing.
stakes: Addresses a potential security vulnerability due to a buffer overrun in the
  assembler, and corrects a parsing error.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: The patch fixes a security vulnerability and a parsing error,
  and the proposed changes seem reasonable.
technical_tradeoffs:
- Adds a check that might slightly slow down assembly.
- Potentially breaks existing code that relies on the buggy behavior (unlikely).
primer: The GNU Assembler (gas) translates assembly language into machine code. A
  buffer overrun is an anomaly where a program writes data beyond the allocated boundary
  of a buffer. MRI mode refers to a specific input format or mode of operation for
  the assembler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVZgev2g-i7gtDy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch prevents a buffer overrun in the `operand` function in `expr.c` when a single quote is at the end of a line, which could lead to reading past the end of a buffer. It also fixes a parsing error in MRI mode when handling hexadecimal floating-point numbers.  These issues were found by fuzzing.
