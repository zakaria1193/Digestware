---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- dwarf
- segfault
- fuzzing
discussion_id: aeXD6PoTmHjtu1iC@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: segfault in out_debug_str'
headline: 'gas: Segfault in out_debug_str'
tldr: Fixes a segfault in the assembler (gas) when processing DWARF debug information
  with a NULL file name.
stakes: Prevents a crash in the assembler, improving its reliability and security
  when handling potentially malformed input.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check for a NULL file name, potentially increasing the runtime slightly.
- Improves robustness by preventing a crash due to malformed input.
- Does not add any new features.
exchanges: []
primer_expert: The patch modifies `gas/dwarf2dbg.c` to prevent a segmentation fault
  in `out_debug_str` when processing DWARF debug information. The function now checks
  for a NULL filename before attempting to use it. This prevents a crash when the
  assembler encounters malformed DWARF information. DWARF is used for representing
  debugging information.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.  DWARF
  is a standard format for storing debugging information, which maps machine code
  instructions back to the original source code. This information is crucial for debuggers
  to function correctly.  This patch fixes a bug in the assembler that could cause
  it to crash when processing DWARF debug information, specifically when a file name
  is missing. By adding a check for a NULL file name, the patch prevents the assembler
  from attempting to access invalid memory, thus avoiding the crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault in the `out_debug_str` function within the assembler's DWARF debugging information processing logic. The segfault occurred when the file name was NULL. The patch adds a check to prevent dereferencing the NULL file name, avoiding the crash.
