---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- documentation
- .insn directive
discussion_id: fe9ca0aa-83b4-42c6-9e48-ffe7514c654a@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 01/19] RISC-V: improve .insn documentation'
headline: 'RISC-V: improve .insn documentation'
tldr: Updates documentation for the .insn directive in the RISC-V assembler to clarify
  syntax and reflect current mapping symbol support.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves documentation clarity.
- Ensures the documentation reflects the current assembler behavior.
- No functional code changes.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Acknowledges the correctness of the patch and points out a minor grammatical
    issue in pre-existing documentation.
  quote: 'LGTM.


    While reading the patch, I noticed one small pre-existing nit:


    "an instructions" could be changed to "an instruction".


    This is not introduced by this patch, though.'
primer_expert: This patch modifies `gas/doc/c-riscv.texi`, which documents RISC-V-specific
  assembler directives for GNU AS. The `.insn` directive allows specifying instructions
  numerically, and the documentation is being updated to reflect current syntax and
  the use of mapping symbols.
primer_general: The GNU Assembler (gas) converts assembly code into machine code.  Assembler
  directives are special commands that control the assembly process. The `.insn` directive
  allows developers to directly specify instruction encodings. This patch updates
  the documentation for the RISC-V `.insn` directive to ensure it's accurate and reflects
  current assembler behavior.
series_id: 'binutils:risc-v: improve .insn documentation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/fe9ca0aa-83b4-42c6-9e48-ffe7514c654a@iscas.ac.cn
bugzilla_url: null
date: '2026-04-28'
---

This patch updates the documentation for the `.insn` directive in the RISC-V assembler.  It removes the incorrect comma from the documented syntax and updates the `.word` related text to reflect the current support for mapping symbols. The documentation change improves clarity and accuracy for developers using the `.insn` directive.
