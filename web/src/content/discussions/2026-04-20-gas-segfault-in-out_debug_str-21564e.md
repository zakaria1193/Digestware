---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- dwarf
- debugging
- segfault
discussion_id: aeXD6PoTmHjtu1iC@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: segfault in out_debug_str'
headline: 'Gas: Segfault in out_debug_str'
tldr: Fixes a segfault in the assembler when processing DWARF debug information with
  a NULL filename.
stakes: This patch resolves a crash in the assembler, improving its robustness when
  handling potentially malformed input files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check for a NULL filename, which may slightly impact performance.
- Prevents a segfault, improving the robustness of the assembler.
- No diagnostic message is emitted for the invalid input.
exchanges: []
primer_expert: The `out_debug_str` function in `gas/dwarf2dbg.c` handles the output
  of strings related to DWARF debugging information. This patch addresses a null pointer
  dereference that occurs when `files[first_file].filename` is NULL. The fix adds
  a check for this condition before calling `strlen` and `memcpy`, preventing a segfault.
primer_general: The GNU assembler (gas) is a tool that translates assembly language
  source code into machine code. DWARF is a debugging data format used to provide
  information about the source code location of machine code instructions. This patch
  fixes a bug in the assembler that occurs when processing DWARF debugging information
  that contains a missing filename, preventing the assembler from crashing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault vulnerability in the GNU assembler (gas) that occurs in the `out_debug_str` function within `dwarf2dbg.c`.  The segfault is triggered when processing DWARF debug information and encountering a NULL filename. The patch adds a check for a NULL filename before attempting to access its length, preventing the crash.
