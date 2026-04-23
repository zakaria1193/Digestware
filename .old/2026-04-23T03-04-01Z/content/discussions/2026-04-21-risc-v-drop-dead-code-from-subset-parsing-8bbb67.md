---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- disassembler
- code cleanup
discussion_id: d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
source_type: public_inbox
title: '[PATCH 17/19] RISC-V: drop dead code from subset parsing'
headline: 'Risc-V: Drop dead code from subset parsing'
tldr: Removes redundant checks and arguments in RISC-V subset parsing code, simplifying
  error handling.
stakes: Minor code cleanup; reduces code size and complexity.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes code, decreasing code size.
- Simplifies error handling logic.
- Potentially improves code readability.
exchanges: []
primer_expert: The RISC-V backend parses ISA subset strings (e.g. "rv32imac") to configure
  the assembler and disassembler. The `riscv_update_subset1` function is responsible
  for updating the parsed subset. This patch removes redundant checks and arguments
  related to error handling within these functions.
primer_general: When assembling or disassembling RISC-V code, the toolchain needs
  to understand which extensions to the base RISC-V ISA are in use. This is often
  specified via a string like "rv32imac". The binutils RISC-V backend includes code
  to parse these strings and configure the assembler and disassembler accordingly.
  This patch simplifies some error handling within that parsing code.
series_id: 'binutils:risc-v: drop dead code from subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d53852fe-455a-44e4-9df7-72ab794141d5@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes a redundant argument from the error handler in `riscv_update_subset1()` and drops unnecessary NULL checks in `riscv_parsing_subset_version()`. These changes simplify the code and clarify error handling during RISC-V ISA subset parsing.
