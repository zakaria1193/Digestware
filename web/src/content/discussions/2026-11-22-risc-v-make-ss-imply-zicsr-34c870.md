---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- isa
- assembler
- linker
- supervisor
discussion_id: 337da3c77dcea04763169d236f571195951e6587.1795334376.git.jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v2 3/3] RISC-V: Make Ss imply Zicsr'
headline: 'RISC-V: Make Ss imply Zicsr'
tldr: Ensures that RISC-V supervisor profiles (Ss) automatically imply the Zicsr extension
  in binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies ISA specification for users by automatically including Zicsr with 'Ss'
  profiles.
- Ensures compliance with RISC-V supervisor architecture requirements.
exchanges: []
primer_expert: 'This patch modifies binutils'' RISC-V support to establish an implication
  relationship: the ''Ss'' (Supervisor ISA) profiles now implicitly include the ''Zicsr''
  extension. This is necessary because supervisor architecture features rely on Control
  and Status Register (CSR) instructions. By adding this implication in `bfd/elfxx-riscv.c`
  (`riscv_implicit_subsets`), users specifying a supervisor profile (e.g., `rv64i_ss1p11`)
  do not need to explicitly list `+zicsr` to assemble CSR instructions. New tests
  are added to GAS to confirm this behavior.'
primer_glossary:
- term: Ss
  definition: RISC-V Supervisor ISA profiles, indicating support for supervisor-level
    operations.
- term: Zicsr
  definition: A RISC-V extension that provides instructions for accessing Control
    and Status Registers (CSRs).
- term: RV64I
  definition: The base integer instruction set for the 64-bit RISC-V architecture.
- term: CSR
  definition: Control and Status Register; special-purpose registers used by the processor
    for configuration and monitoring.
- term: BFD
  definition: Binary File Descriptor library.
- term: GAS
  definition: The GNU Assembler.
- term: Implication
  definition: In ISA definitions, when one extension or feature is automatically included
    if another is selected.
series_id: 'binutils:risc-v: make ss imply zicsr'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/337da3c77dcea04763169d236f571195951e6587.1795334376.git.jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This is the third patch in a series, making the 'Ss' (Supervisor ISA) RISC-V profiles imply the 'Zicsr' extension. This change ensures that selecting a supervisor ISA version on RV64I automatically enables CSR access instructions. The modifications are in BFD's ELF handling and are accompanied by new GAS test cases to verify the implied Zicsr functionality for different supervisor versions.
