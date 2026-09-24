---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- patch
- risc-v
- binutils
- linker
- refactoring
discussion_id: 20260923151722.3185239-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Describe relax passes with a pass table'
headline: 'RISC-V: Describe relax passes with a pass table'
tldr: Refactors RISC-V relax passes into a table for better extensibility and maintainability.
proposer: Kito Cheng
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increases code complexity by introducing a new data structure (pass table) but improves
  maintainability and extensibility.
- Allows for vendor-specific extensions without modifying core relaxation logic.
exchanges: []
primer_expert: This patch restructures the RISC-V relaxation passes in binutils' BFD
  and linker. Previously, `_bfd_riscv_relax_section` used a chain of branches based
  on `info->relax_pass`, and the linker hard-coded the number of passes. This RFC
  introduces a `riscv_relax_pass` struct and a pass table managed by `bfd_elfNN_riscv_init_relax_passes`.
  Each entry in the table describes a pass (reloc selector, hooks, optimization flag),
  enabling easier addition of new passes like vendor-specific ones or Zcmt table jumps
  without modifying the core relax logic.
primer_glossary:
- term: Relaxation passes
  definition: In linkers, these are passes that adjust relocation entries after initial
    linking to optimize code, for example, by shortening branch instructions or handling
    position-dependent code.
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: reloc selector
  definition: A function or mechanism that determines which relocation entries are
    applicable to a particular relaxation pass.
- term: hooks
  definition: Callback functions that can be invoked at specific points during a process,
    such as at the end of a pass or after processing a section.
- term: Zcmt
  definition: Likely refers to a specific extension or feature within the RISC-V architecture,
    possibly related to control-transfer instructions or memory management.
- term: BFD
  definition: Binary File Descriptor library, a backend for the GNU toolchain that
    provides a generic interface to various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260923151722.3185239-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This patch refactors the RISC-V relax pass mechanism in binutils to use a pass table instead of hard-coded branches. This change aims to improve extensibility, allowing for easier addition of new relax passes, such as vendor-specific ones or those for Zcmt table jumps. The new structure defines each pass with a reloc selector, optional hooks, and a flag for optimization disabling, while maintaining the existing functionality.
