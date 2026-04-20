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
headline: 'Gas: Prevent segfault in out_debug_str'
tldr: Fixes a segfault in the assembler (gas) when handling NULL file names in debug
  string output, discovered via fuzzing.
stakes: Improves the robustness of the assembler by preventing crashes caused by malformed
  input, enhancing the developer experience.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Slight performance overhead due to additional checks.
- No diagnostics emitted for invalid input.
primer_expert: This patch fixes a NULL pointer dereference in `gas/dwarf2dbg.c`'s
  `out_debug_str` function. The function generates DWARF debugging information. Specifically,
  it now checks if `files[first_file].filename` is NULL before calling `strlen`, preventing
  a crash when processing malformed input. The fix is important because debug information
  is crucial for debugging optimized binaries.
primer_general: The GNU Assembler (gas) translates human-readable assembly code into
  machine code that computers can execute. During this process, it can also generate
  debugging information in the DWARF format, which helps debuggers map machine code
  back to the original source code. This patch prevents a crash in gas when processing
  malformed input that results in a NULL file name when generating debug information.
  The crash was found using a technique called fuzzing, where the program is fed with
  randomly generated inputs to uncover vulnerabilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault in the assembler (gas) within the `out_debug_str` function in `dwarf2dbg.c`. The segfault occurred when the function encountered a NULL file name. The patch adds a check for a NULL file name before attempting to access it, preventing the crash. This was found as a result of fuzzing the assembler.
