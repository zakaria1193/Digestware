---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- code refactoring
- .insn directive
discussion_id: 21140ce3-6786-497e-9a80-528af1153617@suse.com
source_type: public_inbox
title: '[PATCH 02/19] RISC-V: fold redundant code in riscv_ip()'
headline: 'RISC-V: Fold redundant code in riscv_ip()'
tldr: Refactors the riscv_ip() function to reduce redundant code for parsing 'F' and
  'O' .insn operands.
stakes: Simplifies the assembler's code, making it easier to maintain and extend with
  new sub-forms for the .insn directive.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- No functional changes, purely a code cleanup.
- May require careful review to ensure no unintended behavior changes.
exchanges: []
primer_expert: The patch modifies `gas/config/tc-riscv.c`, specifically the `riscv_ip()`
  function. This function handles the parsing of operands for the `.insn` directive,
  which allows specifying raw instruction encodings. The refactoring aims to reduce
  code duplication in the parsing of 'F' and 'O' operands, improving maintainability
  and simplifying the addition of new instruction forms.
primer_general: The RISC-V assembler translates assembly code into machine code.  The
  `.insn` directive allows embedding raw instruction encodings directly into assembly.
  This patch refactors the `riscv_ip()` function, which is responsible for parsing
  the operands provided to the `.insn` directive. By reducing redundant code, the
  patch makes the assembler's code easier to understand and maintain.  'F' and 'O'
  refer to specific types of operands used with the `.insn` directive, likely representing
  instruction fields.
series_id: 'binutils:risc-v: fold redundant code in riscv_ip()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/21140ce3-6786-497e-9a80-528af1153617@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch refactors the `riscv_ip()` function in the RISC-V assembler to eliminate redundant code related to parsing 'F' and 'O' operands within the `.insn` directive. By consolidating common code, the patch simplifies the function and makes it easier to add new sub-forms in the future. The patch also raises a question about renaming `O4` to better reflect its function.
