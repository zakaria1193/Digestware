---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- relaxation
- relocation
- bug fix
discussion_id: 20261120093011.2921789-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Keep -mno-relax branch relocations to labels in other sections'
headline: 'RISC-V: Keep -mno-relax branch relocations to labels in other sections'
tldr: Fixes an issue where '-mno-relax' incorrectly handled branch relocations to
  symbols in different sections.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Corrects incorrect relocation handling for `-mno-relax`.
- Improves accuracy of branch and jump instruction offsets.
- Ensures proper relocation emission.
exchanges: []
primer_expert: This patch addresses a specific behavior in the RISC-V assembler's
  handling of branch and jump instructions when the `-mno-relax` option is used. Since
  commit `af514e5f6d1`, Gas incorrectly resolves fixups for local symbols even if
  they reside in a different section. This leads to an incorrect offset calculation
  and the omission of a necessary relocation. The patch modifies `gas/config/tc-riscv.c`
  to ensure that such fixups are only applied when the target symbol (`fixP->fx_addsy`)
  belongs to the same segment (`seg`) as the instruction being fixed, mirroring the
  logic already present for `PCR…
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: -mno-relax
  definition: An assembler option that disables or modifies the relaxation process,
    which typically optimizes code by adjusting branch offsets and instruction lengths.
- term: relocation
  definition: The process of updating symbolic references and memory addresses in
    object code or executable files after compilation, typically performed by the
    linker.
- term: fixup
  definition: A placeholder or instruction in the assembly code that the assembler
    or linker resolves to a specific address or value.
- term: PCREL_HI20
  definition: A type of RISC-V relocation used for PC-relative addressing, specifically
    for the higher 20 bits of an immediate value.
- term: Gas
  definition: The GNU Assembler, part of the GNU Binutils suite.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120093011.2921789-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch corrects a bug in the RISC-V assembler where the `-mno-relax` option caused branch and jump fixups to local symbols in other sections to be resolved incorrectly. This resulted in wrong offsets and no relocation being emitted. The fix ensures that fixups are only resolved when the target symbol is in the same section, aligning with the behavior for `PCREL_HI20` relocations.
