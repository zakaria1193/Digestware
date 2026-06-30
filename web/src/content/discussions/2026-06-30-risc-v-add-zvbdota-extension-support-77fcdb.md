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
discussion_id: 20260630033438.143289-2-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH 2/2] RISC-V: Add Zvbdota extension support'
headline: 'RISC-V: Add Zvbdota extension support'
tldr: Assembler and disassembler support for RISC-V Zvbdota family of batched dot-product
  extensions.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in assembler/disassembler logic to support new instruction
  formats and operands.
- Adds new test cases to ensure correctness for the Zvbdota extensions.
exchanges: []
primer_expert: This patch series adds support for the Zvbdota extension family in
  Binutils. Zvbdota offers batched dot product operations, extending the functionality
  of existing Zvdota extensions. The changes focus on assembler and disassembler support
  within `bfd/elfxx-riscv.c` and `gas/config/tc-riscv.c`, introducing new operand
  types and vtype definitions to handle the EMUL=8 `vs2` register group and scaled
  `ci` immediate.
primer_general: This series of patches enhances the Binutils assembler and disassembler
  to support new RISC-V instructions. These instructions, known as the Zvbdota family,
  are designed for efficient computation of dot products, a common operation in digital
  signal processing and machine learning. By processing multiple dot products at once,
  they offer significant performance improvements over previous single dot product
  instructions. The changes ensure that 'gas' (the GNU assembler) and 'binutils' can
  correctly interpret and generate code for these advanced vector operations.
series_id: 'binutils:risc-v: add zvbdota extension support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630033438.143289-2-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch series adds assembler and disassembler support for the RISC-V Zvbdota family of extensions. These extensions compute up to eight dot products simultaneously, utilizing an EMUL=8 `vs2` vector register group and a scaled-by-8 `ci` immediate. The changes include updates to BFD and GAS to recognize these new instructions and their operand constraints, along with new test cases.
