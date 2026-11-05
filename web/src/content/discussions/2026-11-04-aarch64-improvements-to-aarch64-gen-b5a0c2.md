---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- code generation
- disassembler
- refactoring
discussion_id: 6432b803-6a8f-c1e5-a1d0-073342a71917@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 00/28] aarch64: Improvements to aarch64-gen'
headline: 'aarch64: Improvements to aarch64-gen'
tldr: Series of patches overhauls AArch64 opcode generation and lookup for simplification
  and efficiency.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Simplifies opcode table management and generation.
- Improves decoding performance by optimizing lookup chains.
- Increases correctness by extending profile checks and fixing bugs.
- Makes decode prioritization explicit, improving maintainability.
exchanges: []
primer_expert: This is the cover letter for a series of 28 patches touching AArch64
  instruction decoding and generation in binutils. The core of the work appears to
  be in refactoring `aarch64-gen.c` and the generated opcode tables (`aarch64-tbl-*.h`,
  `aarch64-dis-*.c`). Notable functional changes include expanding profile checks
  for instructions, allowing more flexible alias opcode matching, and fixing a GICR
  encoding bug. Non-functional improvements focus on making decode prioritization
  explicit via flags, removing the functional impact of table order, and reducing
  `aarch64_find_next_opcode` chain lengths…
primer_glossary:
- term: aarch64-gen
  definition: A code generator tool within binutils responsible for creating AArch64
    assembler, disassembler, and opcode table source files from definitions.
- term: Opcode Table
  definition: A data structure used by disassemblers and assemblers to map instruction
    byte patterns to mnemonic names and vice-versa. In binutils, these tables define
    the instructions a specific architecture supports.
- term: F_HAS_ALIAS
  definition: A flag used in the AArch64 opcode table to denote an instruction that
    is an alias for another instruction.
- term: Decode Tree
  definition: A hierarchical data structure used in instruction decoders to efficiently
    map instruction bit patterns to their corresponding operations.
- term: A-profile / R-profile
  definition: Different feature sets or configurations of the AArch64 architecture,
    where instructions may be available in one but not the other.
- term: GICR
  definition: Likely refers to a specific instruction or feature within the AArch64
    architecture, possibly related to Generic Interrupt Controller Region or similar.
series_id: 'binutils:aarch64: improvements to aarch64-gen'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/6432b803-6a8f-c1e5-a1d0-073342a71917@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch series introduces significant improvements to the AArch64 opcode generation and lookup mechanisms within binutils. Key changes include extending profile checks to non-alias instructions, refining the decode tree, and allowing alias opcodes to match multiple F_HAS_ALIAS entries. The series also streamlines the `aarch64-gen` tool itself, enhances validation, and updates the build process to handle generation failures gracefully. These changes aim to simplify the opcode table, improve decoding efficiency, and increase overall maintainability.
