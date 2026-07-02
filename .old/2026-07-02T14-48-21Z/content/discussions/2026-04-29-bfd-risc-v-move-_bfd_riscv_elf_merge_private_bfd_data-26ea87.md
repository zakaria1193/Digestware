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
discussion_id: 2e1cf135-ac03-4172-af5c-4ee32552845d@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 18/19] bfd/RISC-V: move _bfd_riscv_elf_merge_private_bfd_data()'
headline: 'bfd/RISC-V: move _bfd_riscv_elf_merge_private_bfd_data()'
tldr: The ARCH_SIZE parameter is factored out of _bfd_riscv_elf_merge_private_bfd_data()
  to avoid building the code twice.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- None apparent; this is a straightforward refactoring.
exchanges:
- author: Jiawei
  role: contributor
  position: Agrees with the patch, which factors out the ARCH_SIZE parameter to avoid
    building the function twice.
  quote: The sole size dependent parameter used there is ARCH_SIZE. For just this
    there's no good reason to build all of the involved code twice.
primer_expert: This patch concerns the BFD library, a generic interface for manipulating
  object file formats. The RISC-V backend uses `_bfd_riscv_elf_merge_private_bfd_data()`
  to merge private data from different object files.  Avoiding code duplication improves
  maintainability.
primer_general: The Binary File Descriptor (BFD) library provides a common way to
  access and manipulate different types of object files (executables, libraries, etc.).
  This patch modifies a function within the RISC-V-specific part of the BFD library
  to avoid unnecessary code duplication. This makes the code easier to maintain and
  reduces the overall size of the library.
series_id: 'binutils:bfd/risc-v: move _bfd_riscv_elf_merge_private_bfd_data()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2e1cf135-ac03-4172-af5c-4ee32552845d@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch modifies the `_bfd_riscv_elf_merge_private_bfd_data()` function in the RISC-V backend of the Binary File Descriptor (BFD) library. The change refactors the code to accept `ARCH_SIZE` as a function parameter, preventing the function from being built twice with different `ARCH_SIZE` values, thus reducing code duplication.
