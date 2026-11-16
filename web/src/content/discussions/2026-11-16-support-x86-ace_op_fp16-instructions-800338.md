---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- ace
- instructions
- assembler
- disassembler
discussion_id: 20261116081937.1879560-3-haochen.jiang@intel.com
source_type: public_inbox
title: Support x86 ACE_OP_FP16/ instructions
headline: Support x86 ACE_OP_FP16/ instructions
tldr: Adds support for ACE_OP_FP16/32/64 instructions, refining register usage and
  error handling for assembler and disassembler.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves accuracy in distinguishing similar register usage patterns.
- Enhances error reporting for invalid instruction usage.
exchanges: []
primer_expert: 'This is part of a series adding support for new x86 ACE instructions.
  Specifically, this patch handles the ACE_OP_FP16/32/64 variants. The key change
  in the assembler is adapting the `process_operands` function to differentiate register
  pair usage for TOP1PD between Xeon Phi and AMX/ACE contexts, moving from a count-based
  check to a type-based check. It also elevates invalid register pair usage from a
  warning to an error, reflecting hardware #UD exceptions. The disassembler is updated
  to support these instructions via existing macros.'
primer_glossary:
- term: ACE_OP_FP16/32/64
  definition: Instruction set extensions for x86 processors, related to floating-point
    operations on 16, 32, and 64-bit data, part of the ACE (Advanced Core Extensions)
    umbrella.
- term: TOP1PD
  definition: A specific instruction within the ACE instruction set that uses a register
    pair for its operands.
- term: zmm register
  definition: Extended registers used in AVX-512 and later instruction sets, offering
    a wider vector width (512 bits) compared to xmm (128-bit) and ymm (256-bit).
- term: Xeon Phi
  definition: A series of microprocessors from Intel designed for high-performance
    computing, featuring many-core architectures.
- term: AMX
  definition: Advanced Matrix Extensions, a set of instructions introduced by Intel
    to accelerate matrix operations, primarily for AI and deep learning workloads.
- term: '#UD'
  definition: An Intel x86 exception indicating an 'Invalid Opcode' detected by the
    processor.
series_id: binutils:support x86 ace_op_fp16/ instructions
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081937.1879560-3-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch series updates binutils to support the ACE_OP_FP16/32/64 instructions. It refines the assembler's handling of register pairs for the TOP1PD instruction to distinguish between Xeon Phi and AMX/ACE usage, and enforces stricter error checking for invalid register pair usage. The disassembler's logic is also adjusted to accommodate these new instructions. This update addresses specific register usage nuances and improves error reporting for these advanced x86 instructions.
