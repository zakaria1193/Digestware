---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- binutils
- bfd
- risc-v
- refactoring
- code duplication
discussion_id: 07919897-963f-406e-9583-729ea168b0b9@suse.com
source_type: public_inbox
title: '[PATCH 18/19] bfd/RISC-V: move _bfd_riscv_elf_merge_private_bfd_data()'
headline: 'BFD/RISC-V: Move _bfd_riscv_elf_merge_private_bfd_data()'
tldr: Refactors _bfd_riscv_elf_merge_private_bfd_data() to avoid code duplication
  by passing ARCH_SIZE as a parameter.
stakes: Reduces code duplication and improves maintainability by centralizing the
  _bfd_riscv_elf_merge_private_bfd_data function.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced code duplication.
- Improved maintainability.
- Slightly increased complexity of function signature.
exchanges: []
primer_expert: The Binary File Descriptor (BFD) library provides a generic interface
  for manipulating object file formats. This patch refactors code in `bfd/elfnn-riscv.c`
  to avoid building the `_bfd_riscv_elf_merge_private_bfd_data` function twice.  The
  function is used for merging private BFD data, and was duplicated to handle different
  `ARCH_SIZE` values. The patch changes the code to pass `ARCH_SIZE` as a parameter,
  eliminating duplicated code.
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that allows programs to work with different types of object files (like executables
  and libraries) in a generic way, without needing to know the specifics of each file
  format. This patch reorganizes some internal code related to the RISC-V processor
  architecture to avoid having duplicate copies of the same code. This makes the code
  easier to understand and maintain, which helps ensure the tools work correctly for
  RISC-V programs.
series_id: 'binutils:bfd/risc-v: move _bfd_riscv_elf_merge_private_bfd_data()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/07919897-963f-406e-9583-729ea168b0b9@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch refactors the `_bfd_riscv_elf_merge_private_bfd_data()` function in the BFD library for RISC-V targets. The function was previously duplicated due to its dependence on `ARCH_SIZE`. This patch modifies the function to accept `ARCH_SIZE` as a parameter, thus avoiding code duplication and improving maintainability.
