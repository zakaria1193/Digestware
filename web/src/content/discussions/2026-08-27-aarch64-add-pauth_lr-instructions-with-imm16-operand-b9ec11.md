---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- assembler
- disassembler
- addressing
discussion_id: 20260827151014.9719-7-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH 6/7] aarch64: add PAuth_LR instructions with imm16 operand'
headline: 'aarch64: add PAuth_LR instructions with imm16 operand'
tldr: Adds immediate PC-relative forms (AUTIA<k>SPPC, RETA<k>SPPC) for AArch64 PAuth_LR
  instructions using a 16-bit offset.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Handles PC-relative addressing internally within the assembler, reducing the need
  for linker relocations but making the assembler logic more complex.
exchanges: []
primer_expert: This patch adds support for immediate, PC-relative addressing modes
  for AArch64 PAuth_LR instructions, specifically `AUTIA<k>SPPC` and `RETA<k>SPPC`.
  These instructions use a 16-bit unsigned immediate value, which is scaled by 4,
  to calculate a target address relative to the current Program Counter (PC). The
  patch introduces `ADDR_UPCREL16` as a new operand type in `gas/config/tc-aarch64.c`
  and modifies `opcodes/aarch64-opc.c` and `opcodes/aarch64-tbl.h` to handle the encoding
  and decoding. Crucially, this offset is resolved internally by `gas` as a fixup,
  meaning no relocation information is…
primer_glossary:
- term: FEAT_PAuth_LR
  definition: A specific AArch64 hardware feature extension for Pointer Authentication
    of the Link Register.
- term: PC-relative address
  definition: An address calculated relative to the current value of the Program Counter
    (PC). This allows instructions to refer to nearby code or data without needing
    absolute addresses.
- term: imm16
  definition: A 16-bit immediate value. This refers to a constant value embedded directly
    within an instruction.
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language code into machine code.
- term: assembler-internal fixup
  definition: A mechanism within an assembler to resolve addresses or other values
    that are not fully known at the time of initial assembly. The assembler performs
    these calculations internally before generating the final machine code.
- term: relocation
  definition: Information emitted into an object file that tells the linker how to
    modify addresses in the code or data sections when the code is moved to a different
    memory location.
series_id: 'binutils:aarch64: add pauth_lr instructions with imm16 operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260827151014.9719-7-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

This patch implements the immediate PC-relative variants of AArch64 FEAT_PAuth_LR instructions: `AUTIA<k>SPPC` and `RETA<k>SPPC`. These instructions utilize an unsigned 16-bit offset, scaled by 4, to determine a PC-relative address. The patch introduces a new operand type `ADDR_UPCREL16` and handles it as an assembler-internal fixup within gas, as no object-file relocation is required. It also updates disassembly to correctly compute target addresses and adds corresponding gas tests.
