---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- instruction matching
- macro instructions
- assembler
- disassembler
discussion_id: 8788ef02-dad2-411b-b4a0-29139d976b0d@suse.com
source_type: public_inbox
title: '[PATCH 04/19] RISC-V: match_*() improvements'
headline: 'RISC-V: match_*() improvements'
tldr: Improves the match functions for RISC-V macro instructions by avoiding unconditional
  calls to `match_opcode()` and adding an assertion.
stakes: Ensures that RISC-V macro instructions are matched correctly, even if the
  macro enumeration changes.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved accuracy of instruction matching for macro instructions.
- Prevention of false negatives when the macro enumeration changes.
exchanges: []
primer_expert: This patch modifies `opcodes/riscv-opc.c` to improve the accuracy of
  instruction matching for RISC-V macro instructions. It ensures that the `match_*`
  functions, such as `match_rd_even` and `match_rs2_even`, do not unconditionally
  call `match_opcode` when used by macro instructions. This prevents potential false
  negatives if the macro enumeration changes, and it adds an assertion to `match_rs1_nonzero`
  to ensure it is only used by macro instructions.
primer_general: This patch focuses on improving the instruction matching process in
  the RISC-V assembler and disassembler. Specifically, it targets the `match_*()`
  functions used to identify instructions, especially macro instructions. The changes
  ensure that these functions correctly match instructions even if the set of available
  macro instructions changes over time. This helps to maintain the accuracy of the
  assembler and disassembler in handling RISC-V code.
series_id: 'binutils:risc-v: match_*() improvements'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8788ef02-dad2-411b-b4a0-29139d976b0d@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves the RISC-V `match_*()` functions used for matching instructions, especially those referenced by macro instructions. It avoids unconditionally invoking `match_opcode()` to prevent false negatives if the macro enumeration changes. It also adds an assertion to `match_rs1_nonzero()` and removes a pointless attribute.
