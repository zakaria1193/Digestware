---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- assembler
- GAS
- relocation
- DWARF
discussion_id: 20260910092253.526336-3-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 2/3] LoongArch: Mark .reloc *, R_LARCH_RELAX target frag'
headline: 'LoongArch: Mark .reloc *, R_LARCH_RELAX as linker-relaxable'
tldr: Ensures GAS correctly identifies fragments with R_LARCH_RELAX as linker-relaxable.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Corrects invalid code generation for linker-relaxable fragments.
- Ensures accurate DWARF debugging information.
- Introduces new hook functions (`loongarch_md_finish`, `tc_frob_file_before_fix`)
  for managing relaxable states.
exchanges: []
primer_expert: This patch addresses an issue in the LoongArch GAS backend where `.reloc
  *, R_LARCH_RELAX` directives, which mark a fragment as linker-relaxable, were not
  properly propagated. The assembler would incorrectly treat distances within such
  fragments as fixed. This caused problems with same-frag symbol subtraction (incorrectly
  converted to PC-relative relocations) and DWARF line table generation (using invalid
  fixed advance opcodes). The patch introduces `loongarch_md_finish` to record the
  presence of these relaxable relocations and uses `tc_frob_file_before_fix` to mark
  the relevant frags and sec…
primer_glossary:
- term: .reloc *, R_LARCH_RELAX
  definition: An assembler directive on LoongArch that marks a code fragment as 'linker-relaxable',
    meaning its final size or position can be adjusted by the linker.
- term: linker-relaxable
  definition: A code fragment or instruction whose size or position can be adjusted
    by the linker during the relaxation phase to optimize code density or performance.
- term: PC-relative relocation
  definition: A type of relocation where the target address is calculated relative
    to the current program counter.
- term: DWARF line tables
  definition: A debugging information format used by DWARF that maps machine code
    addresses to source code lines, enabling debuggers to set breakpoints and step
    through code.
- term: DW_LNS_fixed_advance_pc
  definition: A specific DWARF Line Number Statement (LNS) opcode indicating a fixed
    advance in the program counter, used for tracking source code locations.
series_id: 'binutils:loongarch: mark .reloc *, r_larch_relax target frag'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910092253.526336-3-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch corrects how the LoongArch assembler (GAS) handles `.reloc *, R_LARCH_RELAX` directives. Previously, GAS marked such fragments as linker-relaxable but did not record this state in the containing frag and section. This led to incorrect assumptions about fixed distances between symbols, resulting in the conversion of same-frag symbol subtraction to PC-relative relocations and the use of special DWARF line table opcodes, both invalid after linker relaxation. The fix involves recording the relaxable state and adjusting relocation decisions and DWARF line table generation accordingly.
