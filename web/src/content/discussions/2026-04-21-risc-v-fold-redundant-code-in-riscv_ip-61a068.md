---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- code refactoring
- gas
- insn directive
discussion_id: 21140ce3-6786-497e-9a80-528af1153617@suse.com
source_type: public_inbox
title: '[PATCH 02/19] RISC-V: fold redundant code in riscv_ip()'
headline: 'RISC-V: fold redundant code in riscv_ip()'
tldr: Reduces code duplication in the parsing of 'F' and 'O' operands within the `riscv_ip()`
  function in the RISC-V assembler.
stakes: Simplifies the RISC-V assembler code, making it easier to maintain and extend
  with new features.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced code duplication.
- Improved maintainability.
- Easier extension with new features.
exchanges: []
primer_expert: This patch refactors the `riscv_ip()` function in `gas/config/tc-riscv.c`
  to reduce code duplication in the parsing of 'F' and 'O' operands. It simplifies
  value insertion into instruction by centralizing the common code and abstracting
  operand processing.
primer_general: This patch focuses on improving the internal structure of the RISC-V
  assembler. It reduces code duplication within the `riscv_ip()` function, which handles
  the parsing of instruction operands. By consolidating common code, the patch makes
  the assembler's codebase more maintainable and easier to extend in the future. This
  simplification can lead to fewer bugs and easier integration of new RISC-V features.
series_id: 'binutils:risc-v: fold redundant code in riscv_ip()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/21140ce3-6786-497e-9a80-528af1153617@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch folds redundant code in the `riscv_ip()` function, which is responsible for parsing `.insn` operands in the RISC-V assembler. The parsing of 'F' and 'O' operands is simplified by having a single instance of common code, which reduces code duplication and makes it easier to add new sub-forms.
