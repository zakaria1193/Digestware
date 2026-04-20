---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- DWARF
- debugging
- security
discussion_id: aeXD6PoTmHjtu1iC@squeak.grove.modra.org
source_type: public_inbox
title: 'gas: segfault in out_debug_str'
headline: 'gas: segfault in out_debug_str'
tldr: This patch prevents a segfault in the assembler (gas) when processing DWARF
  debug information with a NULL filename.
stakes: Fixes a crash in the assembler, improving reliability and preventing denial-of-service
  scenarios when processing potentially malicious or malformed input files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: Addresses a crash reported by a fuzzer; the fix is straightforward.
technical_tradeoffs:
- Adds a NULL check that may slightly increase assembly time.
- No diagnostic is emitted for a missing filename.
primer: The GNU Assembler (gas) is a tool used to translate assembly language source
  code into object code.  DWARF is a debugging data format used to describe the structure
  and contents of compiled programs, enabling debuggers to map machine code back to
  source code. This patch avoids a crash when gas is generating debugging information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXD6PoTmHjtu1iC@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a NULL pointer dereference in the `out_debug_str` function in the assembler (gas). The function now checks if the filename is NULL before attempting to use it, preventing a segfault.  This was discovered by fuzzing.
