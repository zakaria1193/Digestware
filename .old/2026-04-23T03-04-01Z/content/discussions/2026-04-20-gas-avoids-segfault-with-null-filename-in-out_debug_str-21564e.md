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
headline: GAS avoids segfault with NULL filename in out_debug_str
tldr: The assembler (GAS) now avoids a segfault when processing debug information
  with a NULL filename.
stakes: Preventing crashes in the assembler improves its reliability and robustness,
  especially when dealing with potentially malformed input files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The patch adds a check for a NULL filename, which introduces a small performance
  overhead.
- The check prevents the assembler from crashing, improving its reliability.
- No diagnostics are emitted for the invalid input, which might make debugging more
  difficult in some cases.
exchanges:
- author: Alan Modra
  role: proposer
  position: 'Proposes fix: GAS avoids segfault with NULL filename in out_debug_str.'
  quote: Another fuzzer fix.  I don't care to emit diagnostics for silly input, so
    haven't done so here.
primer_expert: This patch modifies `gas/dwarf2dbg.c`, which is responsible for generating
  DWARF debugging information within the GNU assembler (GAS). The `out_debug_str`
  function is used to output strings to the `.debug_str` section. The patch addresses
  a null pointer dereference that occurred when `files[first_file].filename` was NULL.
  The fix adds a check to prevent `strlen` from being called on a NULL pointer, thus
  avoiding the segfault.  Instead, the code now appends a single null character.
primer_general: The GNU Assembler (GAS) is a tool that translates assembly language
  code into machine code. DWARF is a standard format for storing debugging information,
  which helps debuggers understand the relationship between the machine code and the
  original source code. This patch fixes a bug in GAS that caused it to crash when
  processing certain types of debugging information. Specifically, the crash occurred
  when the assembler encountered a missing filename. The patch adds a check to prevent
  this crash and allows the assembler to continue processing the file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a segfault in the GNU assembler (GAS) that could occur when processing debug information. Specifically, the `out_debug_str` function in `dwarf2dbg.c` would crash if it encountered a NULL filename. The patch adds a check for a NULL filename and handles the case gracefully by appending a null character.
