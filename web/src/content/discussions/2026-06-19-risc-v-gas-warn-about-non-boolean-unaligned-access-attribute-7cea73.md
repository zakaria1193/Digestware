---
project: binutils
subsystem: risc-v/gas
patch_id: null
tags:
- risc-v
- gas
- attributes
- unaligned access
- warnings
discussion_id: d26d357f-dbcb-4aa1-a193-2dd61bb9f40a@suse.com
source_type: public_inbox
title: '[PATCH v3 10/13] RISC-V/gas: warn about non-boolean unaligned-access attribute'
headline: 'RISC-V/gas: warn about non-boolean unaligned-access attribute'
tldr: The GNU Assembler for RISC-V will now warn about `unaligned-access` attributes
  that are not strictly boolean (0 or 1).
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces new warnings for developers using non-boolean `unaligned-access` attributes,
  which may require updates to existing build systems or assembly code.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to introduce warnings in the RISC-V GNU Assembler for `unaligned-access`
    attributes that are not strictly boolean (0 or 1).
  quote: The attribute being a boolean one, values should be solely 0 or 1.
primer_expert: In the RISC-V `gas` backend (`gas/config/tc-riscv.c`), the `s_riscv_attribute`
  function handles the `.attribute` directive. The `Tag_RISCV_unaligned_access` attribute
  (Tag 3) is a boolean flag indicating whether the compiled object allows unaligned
  memory accesses. The issue arises when developers might pass integer values greater
  than 1, like `0x1234`, for this attribute. From an ABI perspective, this attribute
  is fundamentally a binary choice (enabled/disabled). This patch introduces a check
  `if (attr[Tag_RISCV_unaligned_access].i > 1)` and issues an `as_warn` message, reinforcing
  the inten…
primer_general: 'This patch is for `gas`, the assembler program for RISC-V processors
  (part of the binutils suite). The assembler converts human-written instructions
  into commands the computer can understand. Sometimes, developers add special information,
  called "attributes," to their code to tell the system about certain properties.
  One such attribute is `unaligned_access`, which indicates whether the program can
  access data in memory at addresses that are not perfectly aligned (e.g., trying
  to read a 4-byte number from a memory address that isn''t a multiple of 4). This
  attribute is meant to be a simple "yes" (1) or "no" (0). This change makes `gas`
  smarter: if a developer accidentally sets the `unaligned_access` attribute to a
  number other than 0 or 1, the assembler will now issue a warning. This helps developers
  ensure their code is built correctly and follows the expected rules for RISC-V systems.'
series_id: 'binutils:risc-v/gas: warn about non-boolean unaligned-access attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d26d357f-dbcb-4aa1-a193-2dd61bb9f40a@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This patch for the GNU Assembler (`gas`) on RISC-V introduces a warning for `unaligned-access` attributes that are not boolean (i.e., not 0 or 1). This ensures that developers using the `.attribute` directive for `unaligned_access` are alerted when providing semantically incorrect values, promoting adherence to the attribute's boolean nature. The patch also includes a new test case to verify this warning behavior.
