---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- assembler
- instruction-set
- error-correction
- testsuite
discussion_id: 20261016073246.3301-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Remove support for xvhseli.d'
headline: 'LoongArch: Remove support for xvhseli.d'
tldr: Removes an invalid LoongArch instruction from the assembler and test suite.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures correctness by removing support for a non-existent instruction.
- Reduces potential confusion and errors for users attempting to assemble LoongArch
  code.
exchanges:
- author: zhaozhou
  role: proposer
  position: Submits a patch to remove the `xvhseli.d` instruction from LoongArch support
    because it is not a valid instruction.
  quote: Remove xvhseli.d that is not a valid LoongArch instruction.
primer_expert: This patch addresses an error in the LoongArch instruction set support
  within binutils. The instruction `xvhseli.d` was erroneously added or recognized
  and is not part of the official LoongArch ISA. The patch corrects this by removing
  the instruction's definition from the opcode table (`opcodes/loongarch-opc.c`) and
  consequently deleting its associated test cases from the gas testsuite (`gas/testsuite/gas/loongarch/insn_lasx.d`,
  `gas/testsuite/gas/loongarch/vector.d`, etc.). This ensures that the assembler will
  reject attempts to use this non-existent instruction.
primer_glossary:
- term: LoongArch
  definition: A family of instruction set architectures (ISAs) developed by Loongson
    Technology, primarily for high-performance computing and servers. Binutils provides
    support for assembling and disassembling LoongArch code.
- term: instruction
  definition: A command to a computer processor, specifying an operation to be performed.
    Each instruction has a unique binary code (opcode).
- term: assembler
  definition: A program that translates assembly language source code into machine
    code (object code) that a computer's processor can execute.
- term: opcode
  definition: Operation code. The part of a machine language instruction that specifies
    the operation to be performed by the CPU.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It supports a wide
    variety of processor architectures, including LoongArch.
- term: testsuite
  definition: A collection of test cases used to verify the correctness of software.
    For gas, test suites ensure that instructions are assembled and disassembled correctly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016073246.3301-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch removes the `xvhseli.d` instruction from the LoongArch support in binutils. The instruction was incorrectly identified as valid and had test cases associated with it. By removing it, the assembler will no longer recognize this non-existent instruction, ensuring correctness and preventing potential assembly errors or misinterpretations for LoongArch binaries. The change involves updating opcode definitions and removing corresponding test files.
