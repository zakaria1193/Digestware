---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- isa
- assembler
- linker
discussion_id: 9a14ed2827a5ebe50e88d20efeb0f690553c64a7.1795334376.git.jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v2 2/3] RISC-V: Add Ss1p13 and Zifencei to RVA23S64 and RVB23S64'
headline: 'RISC-V: Add Ss1p13 and Zifencei to RVA23S64 and RVB23S64'
tldr: Updates RISC-V profiles RVA23S64 and RVB23S64 in binutils to include Ss1p13
  and Zifencei extensions.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the RISC-V profile definitions.
- Enhances GAS and BFD's ability to support newer RISC-V specifications.
exchanges: []
primer_expert: This patch updates the definitions of two RISC-V profiles, RVA23S64
  and RVB23S64, within binutils. It incorporates the 'Ss1p13' (Supervisor ISA version
  1.13) and 'Zifencei' (instruction-fetch fence) extensions into these profiles. This
  is achieved by modifying the `riscv_profiles_table` in `bfd/elfxx-riscv.c` and updating
  corresponding tests in `gas/testsuite/gas/riscv/`. The goal is to ensure that binutils
  correctly handles assembly and ELF attribute generation for these profiles.
primer_glossary:
- term: Ss1p13
  definition: RISC-V Supervisor ISA version 1.13.
- term: Zifencei
  definition: A RISC-V extension providing instruction-fetch fence instructions.
- term: RVA23S64
  definition: A RISC-V profile for 64-bit systems, including specific supervisor extensions.
- term: RVB23S64
  definition: Another RISC-V profile for 64-bit systems, possibly related to RVA23S64
    with variations.
- term: CSR
  definition: Control and Status Register, special-purpose registers used by the processor
    to control its operation.
- term: ELF
  definition: Executable and Linkable Format.
- term: BFD
  definition: Binary File Descriptor library.
- term: GAS
  definition: The GNU Assembler.
series_id: 'binutils:risc-v: add ss1p13 and zifencei to rva23s64 and rvb23s64'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9a14ed2827a5ebe50e88d20efeb0f690553c64a7.1795334376.git.jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This patch, the second in a series, adds the Ss1p13 supervisor ISA version and the Zifencei extension to the RVA23S64 and RVB23S64 RISC-V profiles. These additions are necessary for correctly assembling CSR access instructions and for the ELF architecture attribute. The changes modify the BFD ELF backend and update GAS test suites to verify the new attributes.
