---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- extension
- assembler
- linker
discussion_id: 20261122044931.8147-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH] RISC-V: Add Svukte 1.0 extension support'
headline: 'RISC-V: Add Svukte 1.0 extension support'
tldr: Adds support for the RISC-V Svukte 1.0 extension to binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the RISC-V support by incorporating a new extension.
- Requires new test cases to validate the extension's behavior and constraints.
exchanges: []
primer_expert: This patch enhances the RISC-V support in binutils by adding the 'Svukte'
  extension. This involves modifying BFD's ELF handling (bfd/elfxx-riscv.c) to recognize
  'Svukte' as an implicit subset of '+zicsr' and to enforce constraints, specifically
  rejecting its use with RV32 as it requires Sv39. GAS is updated to include Svukte
  in its architecture attribute parsing and testing facilities.
primer_glossary:
- term: Svukte
  definition: A RISC-V extension related to address-independent fault latency.
- term: Zicsr
  definition: A RISC-V extension that provides access to Control and Status Registers
    (CSRs).
- term: RV32
  definition: The 32-bit version of the RISC-V architecture.
- term: Sv39
  definition: A RISC-V virtual memory specification, indicating a 39-bit virtual address
    space.
- term: GAS
  definition: The GNU Assembler.
- term: BFD
  definition: Binary File Descriptor library.
- term: ELF
  definition: Executable and Linkable Format.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261122044931.8147-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This patch introduces support for the Svukte extension in binutils, which deals with address-independent fault latency. It registers version 1.0, implies the Zicsr extension, and rejects RV32 due to the extension's requirement for Sv39. The changes include updates to BFD and GAS, along with new tests for RV64 architecture attributes, RV32 rejection, and -march help.
