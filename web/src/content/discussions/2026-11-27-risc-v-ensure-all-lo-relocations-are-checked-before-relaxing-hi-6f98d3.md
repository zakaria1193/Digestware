---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- linker
- relocation
- abi
discussion_id: 20261127094133.26690-1-luke.zhuang@linux.alibaba.com
source_type: public_inbox
title: '[PATCH] RISC-V: Check all referring LOs before relaxing the PC-relative HI'
headline: 'RISC-V: Ensure all LO relocations are checked before relaxing HI'
tldr: Patch ensures all associated LO relocations are validated before relaxing PC-relative
  HI relocations in binutils for RISC-V, adhering to psABI.
proposer: Luke Zhuang <luke.zhuang@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves correctness and ABI compliance for RISC-V linker relaxation.
- Introduces a slight overhead for collecting and checking LO relocations, but optimized
  to once per section.
exchanges:
- author: Luke Zhuang <luke.zhuang@linux.alibaba.com>
  role: proposer
  position: Submitted a patch to fix RISC-V linker relaxation issues by ensuring all
    LO relocations are validated before relaxing the corresponding HI relocation.
  quote: 'PC-relative relaxation can delete the HI without checking whether all referring
    LOs are marked with R_RISCV_RELAX, causing

    "%pcrel_lo missing matching %pcrel_hi".


    The psABI forbids relaxing only part of a group: https://riscv-non-isa.github.io/riscv-elf-psabi-doc/#_linker_relaxation_types'
primer_expert: This patch for `binutils` targets the RISC-V linker relaxation mechanism.
  It addresses a specific violation of the RISC-V ELF PSABI concerning PC-relative
  relocations. The issue arises when a `R_RISCV_PCREL_HI` relocation is relaxed without
  ensuring that all its paired `R_RISCV_PCREL_LO` relocations are also marked with
  `R_RISCV_RELAX`. The proposed solution involves a more robust check, collecting
  and validating all associated LO relocations before proceeding with the HI relaxation,
  which is a prerequisite for other relaxation features like GOT load relaxation.
primer_glossary:
- term: linker relaxation
  definition: A linker optimization technique that adjusts the size of code or data
    at link time to accommodate certain relocation types, often improving code density
    or performance.
- term: R_RISCV_PCREL_HI
  definition: A RISC-V relocation type for the high part of a PC-relative address.
- term: R_RISCV_PCREL_LO
  definition: A RISC-V relocation type for the low part of a PC-relative address.
- term: R_RISCV_RELAX
  definition: A RISC-V relocation type indicating that a relocation is eligible for
    linker relaxation.
- term: PSABI
  definition: The Procedure Call Standard Application Binary Interface, defining conventions
    for function calls, data types, and other low-level details for a specific architecture
    and ABI.
- term: GOT
  definition: Global Offset Table, a data structure used in position-independent code
    (PIC) to store addresses of global variables and functions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127094133.26690-1-luke.zhuang@linux.alibaba.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in binutils' RISC-V support where PC-relative HI relocations could be relaxed without verifying that all corresponding LO relocations were marked for relaxation. This violates the RISC-V ELF PSABI, which forbids partial relaxation of such groups and can lead to errors like '%pcrel_lo missing matching %pcrel_hi'. The fix involves collecting all associated LO relocations before relaxing the HI and performing safety checks, maintaining performance by scanning only once per section.
