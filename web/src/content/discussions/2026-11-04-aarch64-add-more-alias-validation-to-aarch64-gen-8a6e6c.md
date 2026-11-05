---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- code generation
- validation
- aliases
discussion_id: d7bc0afd-4fa5-5498-5098-4d95a6e4da30@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 18/28] aarch64: Add more alias validation to aarch64-gen'
headline: 'aarch64: Add more alias validation to aarch64-gen'
tldr: Enhances AArch64 opcode validation to ensure alias consistency.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increases build-time checking for opcode definitions to catch aliasing errors.
- Removes some existing checks that are now redundant due to the new alias validation.
exchanges: []
primer_expert: Enhances the opcode table validation in `opcodes/aarch64-gen.c`. It
  introduces checks to ensure that the `F_ALIAS` and `F_HAS_ALIAS` flags are used
  correctly and consistently. Specifically, it verifies that every opcode marked as
  an alias (`F_ALIAS`) points to a valid opcode that has aliases (`F_HAS_ALIAS`),
  and that every opcode with `F_HAS_ALIAS` has at least one actual alias defined.
  This improves the integrity of the opcode table and catches potential inconsistencies
  during the build process.
primer_glossary:
- term: F_ALIAS
  definition: A flag indicating that an opcode is an alias for another instruction.
- term: F_HAS_ALIAS
  definition: A flag indicating that an opcode has one or more aliases.
- term: F_PSEUDO
  definition: A flag indicating a pseudo-instruction, which is not a real machine
    instruction but is used in assembly language.
series_id: 'binutils:aarch64: add more alias validation to aarch64-gen'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d7bc0afd-4fa5-5498-5098-4d95a6e4da30@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch improves validation in `opcodes/aarch64-gen.c` to ensure consistency in AArch64 instruction aliasing. It verifies that all opcodes marked `F_ALIAS` correctly alias an opcode marked `F_HAS_ALIAS`, and vice-versa. It also checks for consistent usage of `F_ALIAS`, `F_HAS_ALIAS`, and `F_PSEUDO` flags across related opcodes. Redundant error checks are removed as a result of these new validations.
