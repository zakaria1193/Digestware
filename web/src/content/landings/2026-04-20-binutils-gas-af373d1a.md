---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- assembler
- i386
- gas
commit_hash: af373d1a1a023a12b107230eb4ebd33ca3e7f57b
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'gas (i386): Restore input_line_pointer in s_insn.'
tldr: The i386 assembler now restores the `input_line_pointer` in the `s_insn` function,
  preventing potential crashes.
why_it_matters: Failure to restore `input_line_pointer` can lead to the assembler
  reading from invalid memory locations, causing crashes. This change ensures correct
  assembler behavior.
impact_score: 5
impact_rationale: Fixes a potential crash in the assembler.
performance_win: false
breaking_change: false
outcome: committed
primer: The GNU Assembler (gas) translates assembly code into machine code.  The `input_line_pointer`
  is a pointer to the current position in the input line being processed by the assembler.
  It is used to track the location of tokens and other elements in the assembly code.
  The `tc-i386.c` file contains code specific to the i386 architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260420011624.65FE54AADCF5@sourceware.org
date: '2026-04-20'
---

The `s_insn` function in `tc-i386.c` was not always restoring `input_line_pointer`, leading to potential issues with `ignore_rest_of_line()` accessing a wild pointer. This commit fixes this by restoring `input_line_pointer` in the `s_insn <bad>` block.
