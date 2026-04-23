---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- dead code
- error handling
discussion_id: d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
source_type: public_inbox
title: '[PATCH 17/19] RISC-V: drop dead code from subset parsing'
headline: 'Risc-V: Drop dead code from subset parsing'
tldr: Removes redundant checks and arguments in RISC-V subset parsing code to simplify
  error handling and improve code clarity.
stakes: Minor code cleanup; reduces complexity and potential for confusion in RISC-V
  ISA extension parsing.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes redundant checks, potentially slightly improving performance.
- Simplifies error handling logic, making the code easier to understand and maintain.
exchanges: []
primer_expert: The RISC-V backend in binutils uses a custom parser (`bfd/elfxx-riscv.c`)
  to handle ISA extensions specified via `-march` and `.option arch`. This patch cleans
  up dead code in `riscv_parse_extensions` and `riscv_update_subset1` to simplify
  error paths. The `errmsg_internal` argument was always empty when passed to error
  handlers and some functions could not return `NULL`, rendering checks redundant.
primer_general: The binutils suite includes assemblers and linkers that need to understand
  the instruction sets they are working with. For RISC-V, which has a modular ISA
  with many extensions, the tools need to parse the list of extensions enabled. This
  patch cleans up some error handling code in the RISC-V extension parsing logic to
  remove redundant checks and simplify the code.
series_id: 'binutils:risc-v: drop dead code from subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes a redundant argument passed to the error handler in `riscv_update_subset1()` and drops unnecessary NULL checks in `riscv_parsing_subset_version()`. These changes simplify the code and clarify that parsing failures should always emit an error message.
