---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- binutils
- macros
- encoding
discussion_id: 93a453e3-789a-5792-7e73-c6abc97df283@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 5/5] aarch64: Replace FLD_* macros in do_misc_{en|de}coding'
headline: 'aarch64: Replace FLD_* macros in do_misc_{en|de}coding'
tldr: This patch replaces FLD_* macros with explicit AARCH64_FIELD calls in do_misc_{en|de}coding
  for aarch64.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the aarch64 assembler (`opcodes/aarch64-asm.c`)
  to replace the `FLD_*` macros with `AARCH64_FIELD` calls in the `do_misc_encoding`
  function. These macros are used to extract and insert fields within AArch64 instructions.
  The `do_misc_encoding` function handles encoding for various miscellaneous instructions,
  including some SVE aliases.
primer_general: This patch modifies the binutils assembler for the AArch64 architecture.  It
  replaces some macros (`FLD_*`) with more explicit function calls (`AARCH64_FIELD`)
  when encoding instructions. This change makes the code easier to understand and
  maintain.
series_id: 'binutils:aarch64: replace fld_* macros in do_misc_{en|de}coding'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/93a453e3-789a-5792-7e73-c6abc97df283@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

This patch replaces the `FLD_*` macros with explicit `AARCH64_FIELD` calls in the `do_misc_encoding` function within the aarch64 assembler.  It also extends the comments to clarify which aliased instructions are involved.  This is part of a series to improve the clarity and maintainability of the aarch64 opcode definitions.
