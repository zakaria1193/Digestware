---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- csr
- isa
discussion_id: 20261027034041.1667435-3-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 2/5] RISC-V: Remove the N extension CSRs'
headline: 'RISC-V: Remove the N extension CSRs'
tldr: Removes definitions for RISC-V N extension CSRs as they are obsolete in the
  current privileged spec.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the opcode header file.
- Ensures the assembler correctly identifies and flags usage of non-existent CSRs.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Removes obsolete RISC-V N extension CSR definitions from include/opcode/riscv-opc.h,
    as they are no longer valid in privileged spec 1.13.
  quote: 'The N extension CSRs (ustatus, uie, utvec, uscratch, uepc, ucause,

    utval, uip, sedeleg and sideleg) were removed in the privileged spec

    1.12.  Now that the privileged spec is always 1.13, they are never

    valid, so remove them.'
primer_expert: This patch cleans up the RISC-V opcode definitions by removing obsolete
  N extension CSRs (e.g., CSR_USTATUS, CSR_SEDELEG). These CSRs were part of earlier
  privileged spec versions but were removed in spec 1.12. Since the toolchain is now
  based on spec 1.13, these definitions are vestigial. Their removal simplifies the
  opcode definitions and ensures that the assembler correctly flags attempts to use
  these non-existent CSRs as errors.
primer_glossary:
- term: CSR
  definition: Control and Status Register. Special registers in RISC-V used for system
    control and status information.
- term: N extension
  definition: A RISC-V extension that historically defined certain Control and Status
    Registers (CSRs) related to supervisor mode. It has been superseded and its CSRs
    removed in later specifications.
- term: privileged spec
  definition: Defines the base instruction set and extensions related to system-level
    privileges in RISC-V architecture, including aspects like Control and Status Registers
    (CSRs) and memory management.
- term: assembler
  definition: A program that translates assembly language code into machine code (object
    code).
- term: disassembler
  definition: A program that translates machine code (object code) back into assembly
    language.
series_id: 'binutils:risc-v: remove the n extension csrs'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261027034041.1667435-3-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This patch removes the definitions for the RISC-V N extension Control and Status Registers (CSRs), such as ustatus and sedeleg, from the opcode header file. These CSRs were deprecated and removed in privileged spec version 1.12. As the toolchain now defaults to privileged spec 1.13, these definitions are obsolete. The assembler will now report them as unknown CSRs, and the disassembler already handles them by printing their numeric values.
