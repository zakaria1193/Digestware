---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- disassembler
- vector extensions
discussion_id: 20260630033438.143289-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH 1/2] RISC-V: Add Zvdota extension classes'
headline: 'RISC-V: Add Zvdota extension classes'
tldr: Adds assembler/disassembler support for RISC-V Zvdota extensions and their use
  of vtype alternative formats.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds new extension classes and constants to support Zvdota instructions and their
  specific VTYPE requirements.
- Increases the complexity of the assembler's instruction parsing and validation logic.
exchanges: []
primer_expert: This patch introduces support for the RISC-V Zvdota extension family
  into Binutils. Zvdota instructions perform dot products on vector registers and
  utilize the 'altfmt' bit within the `vtype` CSR. The modifications in `bfd/elfxx-riscv.c`
  and `gas/config/tc-riscv.c` introduce new extension classes and constants like `e8alt`
  and `e16alt` for `vsew` to correctly handle these operations and specific `vtype`
  configurations.
primer_general: This patch enhances the Binutils assembler and disassembler to support
  new RISC-V vector instructions designed for calculating dot products. These instructions
  are part of the Zvdota family. The changes also include support for a specific feature
  of these instructions called 'altfmt', which modifies how vector element types are
  interpreted. This allows assembly programmers to more precisely control the behavior
  of these vector operations, leading to more efficient code for applications that
  rely on vector computations.
series_id: 'binutils:risc-v: add zvdota extension classes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630033438.143289-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch adds assembler and disassembler support for the RISC-V Zvdota family of extensions, which compute dot products between vector register groups. It also addresses the use of the vtype alternative format bit ('altfmt') by these instructions, adding symbolic constants for `vsetvli`/`vsetivli` to enable assembly code to select the required alternative element formats. Changes span BFD and GAS, including new `ChangeLog` entries and test cases.
