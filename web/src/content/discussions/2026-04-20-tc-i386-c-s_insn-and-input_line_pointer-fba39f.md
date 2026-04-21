---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- i386
- bugfix
discussion_id: aeV-SjBgD0pJeDjD@squeak.grove.modra.org
source_type: public_inbox
title: tc-i386.c s_insn and input_line_pointer
headline: tc-i386.c s_insn and input_line_pointer
tldr: Restores `input_line_pointer` in `s_insn` to prevent accessing a wild pointer
  in `ignore_rest_of_line()`.
stakes: Fixes a potential crash or incorrect behavior in the assembler when parsing
  i386 assembly code.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds one line of code to restore the `input_line_pointer`.
- Fixes a potential crash or incorrect behavior.
- No new features are added.
exchanges: []
primer_expert: The patch modifies `gas/config/tc-i386.c` to correctly restore `input_line_pointer`
  in the `s_insn` function. This function handles instruction parsing for the i386
  architecture. When an error occurs, the code jumps to the `bad` label. The `input_line_pointer`
  was not being correctly reset in this error path, leading to potential issues when
  `ignore_rest_of_line()` was called. The `input_line_pointer` points to the current
  position in the input assembly code being parsed.
primer_general: The GNU Assembler (GAS) translates assembly language into machine
  code.  Assembly language is a human-readable representation of machine instructions.  The
  `input_line_pointer` is a pointer that keeps track of the current position in the
  line of assembly code being processed. This patch fixes a bug in the i386-specific
  part of the assembler, where the `input_line_pointer` was not correctly reset when
  an error occurred, potentially causing the assembler to read from an invalid memory
  location. This can lead to crashes or incorrect assembly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeV-SjBgD0pJeDjD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

A comment in `tc-i386.c` claims that `input_line_pointer` is always restored by the caller of `s_insn`, but this is not always true. This patch fixes a case where `input_line_pointer` is not restored, leading to `ignore_rest_of_line()` accessing a wild pointer. The patch restores `input_line_pointer` in the `s_insn <bad>` code path.
