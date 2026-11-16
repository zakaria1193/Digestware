---
project: binutils
subsystem: mips
patch_id: null
tags:
- mips
- optimization
- scheduling
- architecture
discussion_id: alpine.DEB.2.21.2611100359300.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Swap INSN_MULT opcode flag for INSN_DIV'
headline: 'MIPS: Swap INSN_MULT opcode flag for INSN_DIV'
tldr: Replaces INSN_MULT flag with INSN_DIV for scheduling restrictions on MIPS architecture,
  simplifying instruction handling.
proposer: Maciej W. Rozycki
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies the opcode table by removing an inconsistent flag.
- Improves interlock optimization for certain MIPS instructions on specific CPUs.
exchanges: []
primer_expert: The MIPS architecture's opcode table uses flags to denote instruction
  properties, such as scheduling restrictions. The INSN_MULT flag was an anomaly,
  indicating when an instruction *could* be preceded by others, unlike most flags
  that denote a dependency. This change normalizes this by using INSN_DIV for division
  instructions and adjusting logic in `insns_between` to correctly handle interlocks
  for multiplication-related instructions on specific CPUs like the Toshiba TX39,
  which have unique HI/LO register interlock behaviors.
primer_glossary:
- term: INSN_MULT
  definition: An opcode flag in the MIPS instruction set used to indicate specific
    scheduling behaviors related to multiplication instructions.
- term: INSN_DIV
  definition: An opcode flag in the MIPS instruction set indicating scheduling restrictions
    for division instructions.
- term: interlock optimization
  definition: Compiler or assembler optimizations that ensure correct instruction
    sequencing by inserting necessary delays (e.g., NOPs) to avoid pipeline hazards
    or data dependencies.
- term: Toshiba TX39
  definition: A specific MIPS processor that has particular pipeline constraints related
    to the HI and LO registers, especially concerning division and multiply-add instructions.
- term: HI/LO registers
  definition: Special-purpose registers on MIPS processors that store the high and
    low parts of multiplication or division results.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611100359300.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This change modifies how instruction scheduling restrictions are handled for MIPS multiplication and division operations. It removes the unique INSN_MULT flag, which had an inverse effect on scheduling, and replaces it with the more conventional INSN_DIV flag. This change aims to unify the opcode table and improve interlock optimization for instructions like MTHI and MFLO, especially on the Toshiba TX39 processor, by allowing them to be preceded by instructions that read HI/LO registers.
