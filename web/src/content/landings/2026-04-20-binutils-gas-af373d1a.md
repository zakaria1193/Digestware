---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- assembler
- i386
- bugfix
commit_hash: af373d1a1a023a12b107230eb4ebd33ca3e7f57b
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Assembler now restores `input_line_pointer` in `s_insn`.
tldr: The assembler now restores `input_line_pointer` in the `s_insn` function, preventing
  potential memory access errors.
why_it_matters: Missing restoration of `input_line_pointer` could lead to the assembler
  reading from incorrect memory locations when processing assembly code, resulting
  in unpredictable behavior or crashes.
impact_score: 5
impact_rationale: Fix that prevents memory access errors in the assembler.
performance_win: false
breaking_change: false
outcome: committed
primer: The assembler (gas) translates assembly language source code into object code.
  The `input_line_pointer` is a pointer that keeps track of the current position within
  the line of assembly code being processed. The `ignore_rest_of_line()` function
  skips the remaining characters on the current line.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260420011624.65FE54AADCF5@sourceware.org
date: '2026-04-20'
---

The `s_insn` function in `tc-i386.c` was missing a restoration of the `input_line_pointer` after a certain error condition. This could lead to `ignore_rest_of_line()` accessing a wild pointer. This commit adds the missing restoration to ensure `input_line_pointer` is correctly reset, preventing potential memory access errors.
