---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- segfault
- dwarf
- fuzzing
discussion_id: aeXD6PoTmHjtu1iC@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: segfault in out_debug_str'
headline: 'gas: segfault in out_debug_str'
tldr: A patch prevents a segfault in the assembler when handling NULL filenames in
  debug information.
stakes: Fixes a crash in the assembler, improving reliability when processing potentially
  malformed input.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check for NULL filenames, which may slightly increase processing time.
- Prevents a crash, improving the robustness of the assembler.
- Does not emit a diagnostic message for the invalid input.
exchanges: []
primer_expert: This patch addresses a NULL pointer dereference in `gas/dwarf2dbg.c`.
  The `out_debug_str` function, responsible for outputting debug strings in DWARF
  format, was not checking for NULL filenames, leading to a crash. The fix adds a
  NULL check to prevent the dereference.
primer_general: The GNU Assembler (`gas`) translates assembly code into machine code.
  During this process, it can also generate debugging information (e.g., DWARF) to
  help debuggers understand the generated code. This patch fixes a bug in the assembler
  that occurs when processing debug information, specifically when a source file name
  is missing. The fix prevents the assembler from crashing when encountering this
  situation, making it more robust.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

Alan Modra provides a patch that fixes a segfault in the assembler (`gas`) within the `out_debug_str` function. This issue was discovered through fuzzing and occurs when the filename associated with debug information is NULL. The patch adds a check for a NULL filename before attempting to use it, preventing the segfault.
