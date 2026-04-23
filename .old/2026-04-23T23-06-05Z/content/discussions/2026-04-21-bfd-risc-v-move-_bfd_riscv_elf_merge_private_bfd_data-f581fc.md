---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- binutils
- bfd
- risc-v
- code duplication
- refactoring
discussion_id: 07919897-963f-406e-9583-729ea168b0b9@suse.com
source_type: public_inbox
title: '[PATCH 18/19] bfd/RISC-V: move _bfd_riscv_elf_merge_private_bfd_data()'
headline: 'BFD/RISC-V: Move _bfd_riscv_elf_merge_private_bfd_data()'
tldr: Moves RISC-V ELF data merging to avoid code duplication based on architecture
  size.
stakes: Reduces code duplication and improves maintainability in the BFD library for
  RISC-V.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduces code duplication, improving maintainability.
- Increases code complexity slightly by introducing a function parameter.
- No functional change, only a refactoring.
exchanges: []
primer_expert: This patch refactors `bfd/elfnn-riscv.c` to avoid code duplication
  in `_bfd_riscv_elf_merge_private_bfd_data`.  The original code was duplicated based
  on `ARCH_SIZE` (architecture size). The patch makes `ARCH_SIZE` a function parameter
  to avoid this duplication, streamlining the code.
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that provides a generic interface for working with different object file formats.
  This patch focuses on the RISC-V architecture within BFD. The patch aims to reduce
  code duplication in BFD's RISC-V ELF handling by modifying a function responsible
  for merging private BFD data.
series_id: 'binutils:bfd/risc-v: move _bfd_riscv_elf_merge_private_bfd_data()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/07919897-963f-406e-9583-729ea168b0b9@suse.com
bugzilla_url: null
date: '2026-04-21'
---

Jan Beulich proposes to move the `_bfd_riscv_elf_merge_private_bfd_data()` function to avoid code duplication. The existing implementation duplicates code based on the `ARCH_SIZE` parameter. The change makes the architecture size a function parameter instead, eliminating the need for separate code blocks.
