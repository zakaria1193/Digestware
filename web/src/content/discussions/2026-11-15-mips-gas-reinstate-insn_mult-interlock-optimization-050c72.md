---
project: binutils
subsystem: mips/gas
patch_id: null
tags:
- mips
- gas
- optimization
- pipeline
- risc
discussion_id: alpine.DEB.2.21.2611081723470.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS/GAS: Reinstate INSN_MULT interlock optimization'
headline: 'MIPS/GAS: Reinstate INSN_MULT interlock optimization'
tldr: Restores a previously removed optimization in GAS for MIPS to prevent unnecessary
  NOPs before multiplication instructions on Toshiba TX39.
proposer: Maciej W. Rozycki
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Restores lost functionality and fixes test regressions.
- Reintroduces specific MIPS architecture handling into GAS.
exchanges: []
primer_expert: GAS on MIPS has specific logic in `insns_between` to handle pipeline
  hazards related to HI/LO register reads preceding division instructions. This optimization,
  controlled by the INSN_MULT flag (which uses negative logic), was removed in commit
  `71400594f26d`. This patch restores that logic to prevent NOP insertion issues on
  targets like the R3900, which were failing tests. It also clarifies comments about
  the limited applicability of this optimization.
primer_glossary:
- term: GAS
  definition: GNU Assembler, part of the GNU Binutils package, responsible for translating
    assembly language code into machine code.
- term: INSN_MULT
  definition: An opcode flag in the MIPS instruction set used to indicate specific
    scheduling behaviors related to multiplication instructions.
- term: interlock optimization
  definition: Compiler or assembler optimizations that ensure correct instruction
    sequencing by inserting necessary delays (e.g., NOPs) to avoid pipeline hazards
    or data dependencies.
- term: NOP
  definition: No-Operation instruction; a placeholder instruction that does nothing
    but consume one clock cycle.
- term: HI/LO registers
  definition: Special-purpose registers on MIPS processors that store the high and
    low parts of multiplication or division results.
- term: Toshiba TX39
  definition: A specific MIPS processor that has particular pipeline constraints related
    to the HI and LO registers, especially concerning division and multiply-add instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611081723470.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This patch reinstates an optimization in the GNU Assembler (GAS) for MIPS processors that was inadvertently removed in a previous commit. The optimization correctly handles interlocks for multiplication instructions on the Toshiba TX39 by ensuring that division instructions (DIV, DIVU) do not immediately follow instructions that read the HI/LO registers. Without this, unnecessary NOPs were being inserted, causing test regressions. The patch also updates comments and adjusts test cases.
