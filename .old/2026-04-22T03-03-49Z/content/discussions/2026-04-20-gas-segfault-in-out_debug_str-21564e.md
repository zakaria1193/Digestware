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
headline: 'gas: segfault in out_debug_str'
tldr: This patch prevents a segfault in the assembler due to a NULL filename when
  writing DWARF debug information.
stakes: This patch increases the robustness of the assembler, preventing crashes when
  processing potentially malformed or unusual input files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a check for a NULL filename, which may introduce a small performance overhead.
- Prevents a segfault, improving the stability of the assembler.
- Does not emit diagnostics for the error condition.
exchanges: []
primer_expert: The patch modifies `gas/dwarf2dbg.c` to handle cases where the filename
  associated with a debug entry is NULL.  Without this check, `strlen` would be called
  on a NULL pointer, resulting in a segfault.  The fix adds a check for a NULL `files[first_file].filename`
  and appends a null character to the output if it's NULL.
primer_general: The GNU Assembler (GAS) converts assembly code into object files.
  DWARF is a debugging format used to store information about the original source
  code, such as filenames and line numbers. This patch addresses a bug where the assembler
  would crash (segfault) if it encountered a missing filename while generating DWARF
  debugging information. The patch adds a check to handle this case gracefully, preventing
  the crash and making the assembler more robust.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault vulnerability in the GNU Assembler (GAS) found by fuzzing. The issue occurs in the `out_debug_str` function within `dwarf2dbg.c` when handling DWARF debug information. The patch prevents the segfault by checking for a NULL filename before attempting to access it, and if the filename is NULL, it appends a null character.
