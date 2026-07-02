---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- binutils
- opcodes
- instruction encoding
discussion_id: e346e4a5-fb4c-a76a-fd00-9a5eefd177f4@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 2/5] aarch64: Write AARCH64_FIELD calls to aarch64-opc-2.c'
headline: 'aarch64: Write AARCH64_FIELD calls to aarch64-opc-2.c'
tldr: This patch writes AARCH64_FIELD calls to aarch64-opc-2.c by parsing the operand
  field lists in aarch64-gen.c.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the aarch64 opcode definitions (`opcodes/aarch64-gen.c`
  and `opcodes/aarch64-opc-2.c`). It changes how operand fields are defined, using
  `AARCH64_FIELD` calls in `aarch64-opc-2.c`.  These fields describe the layout of
  instructions for the aarch64 architecture.
primer_general: This patch modifies the binutils assembler for the AArch64 architecture.  It
  changes how the layout of instruction fields are defined, using more explicit function
  calls. This change makes the code easier to understand and maintain, and sets the
  stage for further improvements.
series_id: 'binutils:aarch64: write aarch64_field calls to aarch64-opc-2.c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e346e4a5-fb4c-a76a-fd00-9a5eefd177f4@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

This patch parses the operand field lists in `aarch64-gen.c`, and rewrites the content to `aarch64-opc-2.c` using `AARCH64_FIELD` calls. This allows `aarch64-tbl.h` to use shorthand macros without exporting them elsewhere. This is part of a series to improve the clarity and maintainability of the aarch64 opcode definitions.
