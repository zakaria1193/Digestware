---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- RISC-V
- linker
- relocation
- relaxation
discussion_id: 5bb12fd3-45f9-4d31-bbe7-b94beebd1c7e@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: Add new relocation types for global array accesses'
headline: 'RISC-V: Add new relocation types for global array accesses'
tldr: Reviewer Jiawei points out that R_RISCV_BASE_IDX_ADD relocation handling is
  too broad and may conflict with existing relaxation rules.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: needs_revision
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- 'Optimization vs. Correctness: Balancing the efficiency gains from new relocation
  types against the risk of incorrect code generation due to relaxation issues.'
- 'Generic vs. Specific Handling: Deciding whether a general relaxation rule can accommodate
  new relocation types or if specific handling is required.'
- 'ABI Stability: Ensuring that changes to relocation handling do not break the established
  ABI for RISC-V.'
exchanges:
- author: Jiawei
  role: reviewer
  position: Identifies a potential problem with the `R_RISCV_BASE_IDX_ADD` relocation
    handling, stating it overly broad and may conflict with existing relaxation on
    `_bfd_riscv_relax_lui`.
  quote: "Currently INTERNAL_R_RISCV_BASE_IDX_ADD use gp rewrite rs2 with no limit,\
    \ but the existing relaxation range of '_bfd_riscv_relax_lui' is not \nlimited\
    \ to gp-relative only.\n\nWhen symbol"
- author: wengliqin
  role: proposer
  position: Introduced new relocation types for efficient global array access with
    non-constant subscripts.
  quote: 'This patch introduces support for new RISC-V relocation types

    (R_RISCV_BASE_IDX_*) to enable more efficient code generation for

    global array accesses with non-constant array subscripts.


    New Reloc includes :

    R_RISCV_BASE_IDX_LO12/R_RISCV_BASE_IDX_LO12_S/R_RISCV_BASE_IDX_ADD'
primer_expert: This discussion concerns a patch introducing new relocation types to
  binutils for RISC-V to optimize global array access. The reviewer, Jiawei, raises
  a concern about the `R_RISCV_BASE_IDX_ADD` relocation. Specifically, it appears
  that the relaxation logic, intended to rewrite the `rs2` register to use the global
  pointer (`gp`) as a base, is not sufficiently constrained. This could lead to conflicts
  with other relaxation mechanisms like `_bfd_riscv_relax_lui`, especially when dealing
  with symbols whose displacements relative to `gp` are not well-defined or limited
  by the current relaxation pr…
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) based on reduced instruction
    set computing principles.
- term: relocation
  definition: The process of updating symbolic references in object files to point
    to the correct memory addresses after linking.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executable,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: R_RISCV_BASE_IDX_ADD
  definition: A specific relocation type defined for RISC-V, likely for handling indexed
    access to global data structures.
- term: gp
  definition: Global Pointer, a register used in some architectures (like RISC-V)
    to access global variables and data efficiently.
- term: relaxation
  definition: A linker optimization process that may replace certain instructions
    with equivalent ones that have a larger addressing range, potentially changing
    code size and addresses.
- term: _bfd_riscv_relax_lui
  definition: A specific relaxation function within the BFD library for RISC-V, likely
    related to the `lui` (load upper immediate) instruction used for address calculations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/5bb12fd3-45f9-4d31-bbe7-b94beebd1c7e@iscas.ac.cn
bugzilla_url: null
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

Jiawei reviews a patch proposing new RISC-V relocation types for global array accesses and points out a potential issue with `R_RISCV_BASE_IDX_ADD`. The reviewer notes that this relocation type's handling of rewriting the `rs2` register to use `gp` as the base is too permissive and may conflict with existing relaxation rules, specifically `_bfd_riscv_relax_lui`. The issue arises when the symbol's displacement from `gp` is not adequately limited by the relaxation mechanism.
