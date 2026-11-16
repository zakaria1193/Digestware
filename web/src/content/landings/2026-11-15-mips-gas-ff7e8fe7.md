---
project: binutils
subsystem: mips/gas
patch_id: null
tags:
- mips
- assembler
- optimization
- bugfix
commit_hash: ff7e8fe777f8a6be213a01c99d2c6bb6a08532bf
source_type: public_inbox
author: Maciej W. Rozycki
headline: 'MIPS/GAS: Reinstate INSN_MULT interlock optimization'
tldr: MIPS assembler re-enables optimization for multiplication instructions to prevent
  unnecessary NOPs.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit restores the `INSN_MULT` interlock optimization in `gas/config/tc-mips.c`
  that was lost in commit 71400594f26d. This optimization correctly handles cases
  where multiplication instructions (MULO, MULOU) are preceded by an instruction reading
  the HI/LO registers, preventing unnecessary NOPs. The `INSN_MULT` flag uses negative
  logic and needs to be cleared when no previous instruction is available in `insns_between`
  to correctly suppress NOPs for DIV/DIVU and related macros. This fix addresses test
  regressions on R3900 and ensures consistent behavior across targets.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into machine code.
- term: INSN_MULT
  definition: An opcode flag used in the MIPS assembler to mark multiplication instructions
    that have specific interlock requirements. This flag was previously removed and
    is now reinstated.
- term: HI/LO registers
  definition: Special MIPS registers used to store the high and low 32-bit parts of
    the result from multiplication (MULT, MULTU) and division (DIV, DIVU) operations.
- term: NOP
  definition: No Operation. An instruction that does nothing. NOPs are often used
    for timing, padding, or to fill pipeline stages.
- term: R3900
  definition: A specific MIPS processor core, likely from Toshiba, which has particular
    pipeline behavior and interlock requirements that this commit addresses.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261115111158.F3E994B920C7@sourceware.org
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

A previously removed optimization for MIPS multiplication instructions, related to HI/LO register reads, has been reinstated in the GAS assembler. This optimization was silently dropped in a previous commit, leading to the emission of unnecessary NOP instructions before multiplication opcodes. The change corrects this by reintroducing logic to handle data dependencies, preventing regressions in test cases for multiplication and division operations on specific MIPS cores.
