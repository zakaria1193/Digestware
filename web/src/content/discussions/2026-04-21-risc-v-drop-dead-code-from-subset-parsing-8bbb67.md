---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- gas
- dead code
discussion_id: d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
source_type: public_inbox
title: '[PATCH 17/19] RISC-V: drop dead code from subset parsing'
headline: 'RISC-V: Drop dead code from subset parsing'
tldr: Removes unnecessary checks and simplifies error handling in RISC-V subset parsing
  code.
stakes: Simplifies code and potentially improves performance by removing dead code
  in the RISC-V assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced code complexity.
- Potentially improved performance due to fewer checks.
exchanges: []
primer_expert: This patch simplifies the RISC-V subset parsing logic in `bfd/elfxx-riscv.c`
  and `gas/config/tc-riscv.c` by removing dead code. The patch removes an unused argument
  passed to the error handler in `riscv_update_subset1()` and removes NULL checks,
  as `riscv_parsing_subset_version()` cannot return NULL.
primer_general: The GNU Assembler (gas) translates human-readable assembly code into
  machine code.  This patch cleans up code related to how the assembler handles specific
  features (or "subsets") of the RISC-V processor.  It removes some unnecessary checks
  and simplifies the way errors are reported, making the code easier to understand
  and maintain. This doesn't change the functionality of the assembler, but makes
  the underlying code cleaner.
series_id: 'binutils:risc-v: drop dead code from subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes dead code and simplifies error handling within the RISC-V subset parsing logic. Specifically, it removes an unnecessary argument from an error handler call and removes checks for a function that cannot return NULL, clarifying that there is no issue with a missing error message.
