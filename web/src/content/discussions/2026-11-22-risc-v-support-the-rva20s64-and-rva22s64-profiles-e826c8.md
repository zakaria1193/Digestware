---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- isa
- assembler
- linker
discussion_id: 20261122061904.132162-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH] RISC-V: Support the RVA20S64 and RVA22S64 profiles'
headline: 'RISC-V: Support the RVA20S64 and RVA22S64 profiles'
tldr: Adds support for RVA20S64 and RVA22S64 RISC-V profiles to binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increases the complexity of the RISC-V backend by adding support for new profiles.
- Requires additions to test suites to ensure correct functionality.
exchanges: []
primer_expert: This patch updates binutils' RISC-V ELF backend (bfd/elfxx-riscv.c)
  and assembler (gas) to recognize and correctly process the RVA20S64 and RVA22S64
  profiles. These profiles represent specific configurations of the RISC-V ISA, including
  mandatory extensions and supervisor ISA versions, which are encoded in the ELF `E_FLAGS`
  field. The changes ensure that assemblers and linkers can correctly handle code
  targeting these profiles.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles.
- term: RVA20S64
  definition: A specific profile of the RISC-V ISA, indicating a 64-bit architecture
    with certain standard extensions and supervisor ISA version requirements.
- term: RVA22S64
  definition: Another RISC-V profile, similar to RVA20S64 but with potentially different
    or newer extension requirements and supervisor ISA versions.
- term: Zifencei
  definition: A RISC-V extension that provides instructions for managing instruction
    fetches, crucial for certain architectural profiles.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by GNU Binutils
    for reading and writing various executable file formats.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261122061904.132162-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This patch introduces support for the RVA20S64 and RVA22S64 RISC-V profiles, which include specific supervisor ISA versions and extensions like Zifencei. The changes affect BFD and GAS, adding new tests for the updated attributes.
