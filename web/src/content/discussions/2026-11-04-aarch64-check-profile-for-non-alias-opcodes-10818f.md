---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- disassembler
- code quality
- architecture
discussion_id: 5c7722f7-84f4-e97a-7b7e-884566f7b979@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 02/28] aarch64: Check profile for non-alias opcodes'
headline: 'aarch64: Check profile for non-alias opcodes'
tldr: Extends AArch64 profile checks to non-alias instructions and replaces gotos
  with returns in the decoder.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves correctness by ensuring profile compatibility for all opcodes.
- Enhances code readability and maintainability by removing goto statements.
exchanges: []
primer_expert: This patch updates `opcodes/aarch64-dis.c` by adding a check for CPU
  feature availability (A-profile vs. R-profile) for non-alias opcodes, mirroring
  existing checks for alias opcodes. Additionally, it cleans up the `aarch64_opcode_decode`
  function by eliminating `goto` statements and using early returns instead, which
  simplifies control flow.
primer_glossary:
- term: A-profile
  definition: A specific configuration or feature set of the AArch64 architecture,
    distinct from R-profile.
- term: R-profile
  definition: Another specific configuration or feature set of the AArch64 architecture,
    distinct from A-profile. Often associated with server or embedded use cases.
- term: Alias Opcode
  definition: An instruction that is a synonym or alternative representation for another
    instruction, often for compatibility or historical reasons.
- term: goto
  definition: A control flow statement in C that transfers execution to a different
    part of the program, often used for error handling or complex branching, but sometimes
    criticized for making code harder to follow.
series_id: 'binutils:aarch64: check profile for non-alias opcodes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/5c7722f7-84f4-e97a-7b7e-884566f7b979@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch extends the AArch64 instruction decoding logic to verify that both alias and non-alias opcodes are available for the current CPU's profile (A-profile vs. R-profile). It also refactors the `aarch64_opcode_decode` function to replace `goto` statements with immediate `return` statements, improving code readability and maintainability.
