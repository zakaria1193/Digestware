---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- macros
- instruction matching
discussion_id: c1799431-3096-424c-8dbd-ba2116a57dcc@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 04/19] RISC-V: match_*() improvements'
headline: 'RISC-V: match_*() improvements'
tldr: For RISC-V, macro instruction matching functions now assert macro-only usage
  and avoid potentially incorrect opcode matching due to macro enumeration changes.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds an assertion that will halt execution if `match_rs1_nonzero` is not used in
  macro context.
- Slightly modifies instruction matching logic to avoid opcode matching for macro
  instructions, which could have subtle performance implications.
- Improves the correctness of macro instruction matching.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Agrees with the changes, noting that skipping `match_opcode()` for macro
    entries is reasonable, and the assertion documents the macro-only use nicely.
  quote: 'LGTM.


    Skipping match_opcode() for macro entries looks reasonable to me, and the assertion
    in match_rs1_nonzero() documents its macro-only use nicely.'
primer_expert: The patch modifies functions like `match_rd_even` and `match_rs1_nonzero`
  in `opcodes/riscv-opc.c`. These functions are used during assembly to determine
  if an instruction matches a given pattern. The change ensures that macro instructions
  are handled correctly, avoiding potential errors due to changes in macro enumeration.
primer_general: When assembling code, the assembler needs to determine which instruction
  matches the given input. This involves matching the instruction's opcode and operands
  against known patterns. This patch modifies the matching logic for RISC-V macro
  instructions in the GNU assembler (gas). It ensures that the matching process is
  accurate and avoids potential errors caused by changes in the set of defined macros.
series_id: 'binutils:risc-v: match_*() improvements'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c1799431-3096-424c-8dbd-ba2116a57dcc@iscas.ac.cn
bugzilla_url: null
date: '2026-04-28'
---

This patch improves the RISC-V instruction matching functions. It adds an assertion to `match_rs1_nonzero()` to ensure it's only used by macro instructions. It also skips `match_opcode()` for macro entries to prevent false negatives when the macro enumeration changes. This change ensures the matching functions behave as expected when dealing with macro instructions.
