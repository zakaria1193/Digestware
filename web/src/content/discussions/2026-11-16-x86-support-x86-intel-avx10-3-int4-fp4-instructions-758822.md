---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- avx10
- int4
- fp4
- instructions
discussion_id: 20261116081322.1851772-2-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH 1/3] x86: Support x86 Intel AVX10.3 INT4/FP4 instructions'
headline: 'x86: Support x86 Intel AVX10.3 INT4/FP4 instructions'
tldr: Adds support for AVX10.3 INT4/FP4 instructions in binutils, refining assembler
  logic for down-converts.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds support for new integer and floating-point data types in vector instructions.
- Refines assembler logic for specific down-conversion scenarios.
exchanges: []
primer_expert: This patch adds support for INT4/FP4 instructions within the AVX10.3
  extension to binutils. It modifies `config/tc-i386.c` and `opcodes/i386-opc.tbl`
  to recognize these new instructions. A key change is the introduction of the `%HF`
  macro in `opcodes/i386-dis.c` to handle specific operand requirements for down-converts,
  ensuring HF source goes to W0 and BF16 to W1. The disassembler's EVEX prefix, width,
  and table definitions are also updated, and new test cases are added.
primer_glossary:
- term: AVX10.3
  definition: A version of Intel's Advanced Vector Extensions instruction set, which
    includes enhancements over previous versions like AVX10.2.
- term: INT4/FP4
  definition: Instructions operating on 4-bit integer and floating-point data types,
    part of the AVX10.3 instruction set extensions.
- term: W table
  definition: Likely refers to a part of the disassembler's internal tables or logic
    used to determine instruction encoding details, such as operand size or type.
- term: HF
  definition: Likely refers to the half-precision (FP16) floating-point format.
- term: BF16
  definition: BFloat16 (Brain Floating Point), a 16-bit floating-point format optimized
    for machine learning.
series_id: 'binutils:x86: support x86 intel avx10.3 int4/fp4 instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081322.1851772-2-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch series introduces support for AVX10.3 INT4/FP4 instructions, which are part of the broader AVX10.3 specification. It updates the assembler's configuration, documentation, and test suites, as well as the opcode definitions for the disassembler. A new macro, `%HF`, is introduced to correctly handle the W table skipping for down-converts, ensuring the correct source operand is placed in W0 for HF and W1 for BF16. The patch also refines opcode definitions and regenerates related tables.
