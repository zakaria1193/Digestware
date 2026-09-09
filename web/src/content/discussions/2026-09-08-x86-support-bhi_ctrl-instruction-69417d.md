---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- instruction
- disassembler
- assembler
discussion_id: 20260908074213.709182-1-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH v2] x86: Support BHI_CTRL instruction'
headline: 'x86: Support BHI_CTRL instruction'
tldr: Patch adds support for the BHI_CTRL instruction (ibhf) to the x86 disassembler
  and assembler.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Ensuring correct disassembler output for both REX.W and REX2.W encodings of the
  BHI_CTRL instruction.
- Integrating new instructions close to release cycles, requiring clear communication
  about their inclusion.
exchanges:
- author: Haochen Jiang
  role: proposer
  position: Submitted a patch to add support for the BHI_CTRL instruction, clarifying
    its encoding and confirming compatibility with REX2.W.
  quote: 'I just get the clarification that for ibhf, both rex.w and rex2.w took

    the same effect. Thus, it will not cause extra burden from software side.

    I have added REX2 test for BHI_CTRL to explicitly show that.'
- author: Jan Beulich
  role: reviewer
  position: Provided feedback on the new test cases, specifically requesting the removal
    of \s whitespace characters in favor of tab characters for better readability
    and consistency.
  quote: "As also said to Rohan on (I think) the AVX2-aux patch, no \\s in new tests\n\
    please. [\t] helps readability, by making the whitesp"
primer_expert: This patch introduces support for the BHI_CTRL instruction (opcode
  ibhf) into the x86 backend of binutils. The instruction, detailed in Intel's May
  2025 technical paper on Branch History Injection, uses a specific encoding (F3 48
  0F 1E F8) that leverages REX.W. Crucially, REX2.W is also a valid prefix for this
  instruction, a detail clarified in the patch's rationale. The changes update `i386-opc.tbl`,
  `i386-gen.c`, `i386-dis.c`, and add new test cases to the `gas/testsuite/gas/i386/`
  directory to cover both the basic and REX2-encoded forms of the instruction, ensuring
  correct disassembly and…
primer_glossary:
- term: BHI_CTRL
  definition: An instruction related to Branch History Injection, likely used for
    security purposes to mitigate speculative execution attacks.
- term: ibhf
  definition: The mnemonic for the Branch History Injection instruction.
- term: REX.W / REX2.W
  definition: Instruction prefixes in x86-64 that extend the instruction set, with
    the '.W' bit typically signifying 64-bit operand size.
- term: Disassembler
  definition: A tool that converts machine code into human-readable assembly language.
- term: SDM
  definition: Software Developer's Manual, a comprehensive guide for programmers detailing
    processor instructions and features.
- term: NOP encoding
  definition: No-Operation instruction encoding. Instructions that do nothing but
    consume CPU cycles. Some NOP encodings can be used by other instructions.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260908074213.709182-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Haochen Jiang submits a patch to add support for the BHI_CTRL instruction, known as 'ibhf', to Binutils. This instruction uses REX.W encoding, and importantly, REX2.W is also permissible without causing additional burden. The patch updates the disassembler and assembler to correctly handle this instruction, including adding new test cases for both REX2 and general x86-64 scenarios. The information about this instruction will be available in the Q4 2026 Software Developer's Manual (SDM).
