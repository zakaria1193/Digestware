---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- dwarf
- segfault
discussion_id: aeXD6PoTmHjtu1iC@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: segfault in out_debug_str'
headline: 'Gas: Segfault in out_debug_str'
tldr: Fixes a segfault in the assembler (gas) when handling NULL file names in debug
  information.
stakes: Improves the stability of the assembler and prevents crashes when processing
  malformed input files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check for NULL file names, slightly increasing code complexity.
- Improves stability by preventing a crash.
- Does not provide specific error messages for the invalid input.
primer_expert: This patch addresses a crash in the assembler's DWARF debugging information
  handling (`dwarf2dbg.c`). The `out_debug_str` function is responsible for outputting
  strings related to debugging information. The fix involves checking for a NULL filename
  before attempting to use it, preventing a dereference of a NULL pointer.
primer_general: The GNU Assembler (`gas`) translates assembly language code into object
  code. DWARF is a debugging data format used to store information about a program's
  source code and variables. This patch prevents a crash in the assembler when it
  encounters malformed debug information, ensuring that it can gracefully handle unexpected
  input.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault in the assembler (`gas`) that occurs in the `out_debug_str` function when processing debug information with a NULL file name. The patch adds a check for NULL file names in `dwarf2dbg.c` to prevent the segfault. The author notes that no diagnostics are emitted for this type of invalid input.
