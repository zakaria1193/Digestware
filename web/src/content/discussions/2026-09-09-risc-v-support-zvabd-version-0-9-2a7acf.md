---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- binutils
- assembler
- extension support
discussion_id: 20260909082433.69750-1-garthlei@linux.alibaba.com
source_type: public_inbox
title: '[PATCH] RISC-V: Support Zvabd version 0.9'
headline: 'RISC-V: Support Zvabd version 0.9'
tldr: Updates RISC-V binutils support for the Zvabd extension to version 0.9, reflecting
  changes in instruction variants and encodings.
proposer: Bohan Lei <garthlei@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures compatibility with the latest RISC-V Zvabd instruction set.
- Requires updates across multiple binutils components (BFD, gas, opcodes).
exchanges: []
primer_expert: This patch updates binutils to support version 0.9 of the RISC-V Zvabd
  (integer vector absolute difference) extension. The Zvabd extension itself is part
  of the RISC-V vector extension family, designed to accelerate vector operations,
  specifically absolute differences between vector elements. The update reflects changes
  in instruction encodings and variants as defined in the RISC-V ISA manual and the
  Zvabd specification. This ensures that binutils can correctly assemble and process
  code using the latest Zvabd instructions.
primer_glossary:
- term: Zvabd
  definition: A RISC-V extension for integer vector absolute difference operations.
    It provides instructions to compute the absolute difference between elements of
    two vectors or between a vector and a scalar.
- term: RISC-V
  definition: An open-standard instruction set architecture based on Reduced Instruction
    Set Computer principles.
- term: version 0.9
  definition: The specific version of the Zvabd extension that this patch adds support
    for, indicating a finalized or near-finalized specification.
- term: instruction variants
  definition: Different forms or encodings of an instruction that may perform slightly
    different operations or operate on different data types.
- term: encodings
  definition: The binary representation of machine instructions.
- term: BFD
  definition: Binary File Descriptor library, a part of binutils that provides a common
    interface to various object file formats.
- term: gas
  definition: GNU Assembler, part of binutils, responsible for converting assembly
    language code into machine code.
- term: opcodes
  definition: The part of a machine language instruction that specifies the operation
    to be performed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260909082433.69750-1-garthlei@linux.alibaba.com
bugzilla_url: null
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

This patch updates the binutils support for the RISC-V Zvabd (integer vector absolute difference) extension to its latest approved version, 0.9. The RISC-V Architecture Review Committee (ARC) revised the instruction variants and encodings, necessitating this update. The changes affect BFD, gas, and opcodes components, including modifications to ELF definitions, NEWS file, test cases, and opcode definitions.
