---
project: binutils
subsystem: mips
patch_id: null
tags:
- mips
- gas
- pipeline
- hazard
- architecture
discussion_id: alpine.DEB.2.21.2611100146370.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Correct Toshiba TX39 MADD/MADDU HI/LO instruction flags'
headline: 'MIPS: Correct Toshiba TX39 MADD/MADDU HI/LO instruction flags'
tldr: Fixes instruction flags for MIPS multiply-add instructions on Toshiba TX39 to
  correctly handle pipeline hazards with HI/LO registers.
proposer: Maciej W. Rozycki
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures correct instruction sequencing for MIPS multiply-add instructions on a specific
  architecture.
- Adds flags to instruction definitions to enable hazard detection.
exchanges: []
primer_expert: The `insns_between` logic in GAS for MIPS handles pipeline hazards
  by checking instruction flags. For MIPS multiply-add instructions (MADD, MADDU)
  on the Toshiba TX39, a hazard exists if they are followed by DIV or DIVU. This is
  because MADD/MADDU *read* the HI/LO registers, which DIV/DIVU modify. The patch
  adds the INSN_READ_HI and INSN_READ_LO flags to these instructions in `opcodes/mips-opc.c`
  so `insns_between` can correctly identify and mitigate this hazard by inserting
  NOPs.
primer_glossary:
- term: GAS
  definition: GNU Assembler, part of the GNU Binutils package, responsible for translating
    assembly language code into machine code.
- term: MADD
  definition: MIPS multiply-add instruction.
- term: MADDU
  definition: MIPS unsigned multiply-add instruction.
- term: HI/LO registers
  definition: Special-purpose registers on MIPS processors that store the high and
    low parts of multiplication or division results.
- term: DIV/DIVU
  definition: MIPS division instructions.
- term: pipeline hazard
  definition: A situation in a CPU's instruction pipeline where the next instruction
    cannot execute because it depends on the result of a previous instruction that
    has not yet completed.
- term: Toshiba TX39
  definition: A specific MIPS processor that has particular pipeline constraints related
    to the HI and LO registers, especially concerning division and multiply-add instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611100146370.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This patch corrects the instruction flags in GAS for Toshiba TX39's MADD and MADDU instructions. These instructions, when reading from HI/LO registers, have a pipeline hazard with subsequent DIV or DIVU instructions. Previously, GAS did not recognize this hazard for MADD/MADDU due to missing INSN_READ_HI/INSN_READ_LO flags. By adding these flags, GAS will now correctly emit NOP instructions to separate hazardous instruction sequences, ensuring proper operation and passing test cases.
