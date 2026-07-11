---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- disassembler
- LOCK prefix
- control registers
discussion_id: 8b5974f8-7533-44a7-b357-40fd5f5f0db3@suse.com
source_type: public_inbox
title: '[PATCH] x86: accept LOCK on control register accesses only with ModR/M.reg
  == 0'
headline: 'x86: accept LOCK on control register accesses only with ModR/M.reg == 0'
tldr: Patch adjusts assembler and disassembler support for LOCK prefix on CR0/CR8
  accesses.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enforces stricter instruction encoding rules for LOCK prefix with control registers,
  potentially rejecting previously accepted but technically incorrect code.
- Introduces a new feature flag (`altmovcr8`) requiring explicit CPU support, which
  might affect older or less common processor configurations.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Submits a patch to enforce that the LOCK prefix is only accepted for MOV
    instructions accessing CR0 or CR8, specifically when ModR/M.reg is 0. This change
    also adds a new feature indicator `altmovcr8` to gas to track CPU support, restricts
    CR9-CR15 outside of 64-bit mode, and handles LOCK prefix usage in 64-bit mode
    f…
  quote: 'Reportedly (e.g. [1]) the LOCK handling is special to %cr0 / %cr8 only.

    Deal with it this way also in assembler and disassembler.


    For the assembler also introduce a separate feature indicator: Not all

    64-bit CPUs support this insn form; only most AMD (and presumably all

    Hygon) ones do. Register names %cr9 ... %cr15 thus become invalid outside

    of 64-bit mode altogether (unprefixed forms become or…'
primer_expert: This patch refines the x86 assembler and disassembler's handling of
  the LOCK prefix in conjunction with MOV instructions targeting control registers
  CR0 and CR8. Historically, LOCK prefixes are not generally permitted on instructions
  modifying CRs, but exceptions exist for CR0 and CR8 under specific encoding conditions
  (ModR/M.reg == 0). The patch introduces an `altmovcr8` feature flag for gas to gate
  this behavior based on CPU support, as it's not universal. It also rectifies disassembler
  behavior, ensuring correct parsing in 64-bit mode and avoiding misinterpretation
  with the `intel64` CPU…
primer_glossary:
- term: ModR/M.reg
  definition: A field within the ModR/M byte of an x86 instruction that specifies
    a register, often used to denote the destination register or an extension of the
    opcode.
- term: LOCK prefix
  definition: An x86 instruction prefix that makes the subsequent instruction uninterruptible
    and ensures atomicity, typically used for memory access synchronization.
- term: CR0/CR8
  definition: Control Registers in x86 architecture used for system control and configuration.
    CR0 holds flags for CPU mode, paging, etc., while CR8 is used for extended system
    registers.
- term: assembler
  definition: A program that translates assembly language source code into machine
    code.
- term: disassembler
  definition: A program that translates machine code back into assembly language.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: altmovcr8
  definition: A feature flag indicating support for the alternative MOV to/from CR8
    instruction with LOCK prefix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8b5974f8-7533-44a7-b357-40fd5f5f0db3@suse.com
bugzilla_url: null
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

Jan Beulich proposes a patch to restrict LOCK prefix handling for MOV to CR0/CR8 instructions, aligning with documented behavior. The patch introduces a new feature indicator for assemblers to denote CPU support for this instruction form. For the disassembler, it ensures correct handling in 64-bit mode and distinguishes it from 'intel64' option usage. The changes also update the documentation to include the new `altmovcr8` mnemonic.
