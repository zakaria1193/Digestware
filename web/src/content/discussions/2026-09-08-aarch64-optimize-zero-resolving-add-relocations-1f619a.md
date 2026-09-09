---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- AArch64
- optimization
- linker
- relocations
discussion_id: 68718532-7533-55c0-3646-08fdd29abafa@e124511.cambridge.arm.com
source_type: public_inbox
title: 'AArch64: Optimize ADD relocations that resolve to zero'
headline: 'AArch64: Optimize zero-resolving ADD relocations'
tldr: AArch64 ADD relocations that resolve to zero are now optimized to MOV or NOP
  instructions.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves code density and potentially performance by replacing redundant ADD instructions.
- Adds complexity to the relocation handling logic.
- Ensures compatibility with `--no-relax` option.
exchanges:
- author: Alice Carlotti
  role: reviewer
  position: Agrees with the patch but requests renaming the `optimize_add_zero` boolean
    to `optimize_relocations` for better future-proofing.
  quote: 'Please rename the bool optimize_add_zero to optimize_relocations, wherever
    it

    occurs. This will be a more appropriate name if/when any further optimisations

    are implemented.


    Ok with that change.'
- author: Sivan Shani
  role: proposer
  position: Submitted a patch to optimize AArch64 ADD instructions that resolve to
    zero, replacing them with MOV or NOP.
  quote: "The \"ELF for the Arm 64-bit Architecture\" specification, section 5.7.9,\n\
    recommends that linkers optimize ADD instructions whose immediate becomes\nzero\
    \ after relocation.  In particular:\n\n   ADD x0, x1, 0\n   ADD x2, x2, 0\n\n\
    may be replaced with:\n\n   MOV x0, x1\n   NOP"
primer_expert: This patch optimizes AArch64 ADD instructions that, after relocation,
  have an immediate value of zero. The optimization replaces `ADD Rx, Ry, 0` with
  `MOV Rx, Ry` and `ADD Rx, Rx, 0` with `NOP`. This is based on ELF for AArch64 spec
  section 5.7.9. The changes affect `aarch64_relocate` and `aarch64_build_one_stub`
  in `elfnn-aarch64.c`, honoring `--no-relax`. A test case is added to verify the
  behavior with `--no-relax`.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: ADD relocation
  definition: A relocation operation that modifies the immediate value of an ADD instruction
    after linking.
- term: MOV instruction
  definition: A processor instruction that copies a value from a source operand to
    a destination operand.
- term: NOP
  definition: No Operation. A processor instruction that does nothing but consume
    clock cycles.
- term: --no-relax
  definition: A linker option that prevents relaxation, a process where the linker
    modifies instructions to optimize for code size or performance. In this context,
    it ensures that ADD instructions resolving to zero are not modified if relaxation
    is disabled.
series_id: 'binutils:aarch64: optimize add relocations that resolve to zero'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/68718532-7533-55c0-3646-08fdd29abafa@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch introduces an optimization for AArch64 AArch64 ADD instructions where the immediate value becomes zero after relocation. According to the ARM architecture specification, such instructions can be replaced with a `MOV` instruction (for different source and destination registers) or a `NOP` (for the same source and destination register). This optimization is applied conditionally, respecting the `--no-relax` linker option, and ensures that 32-bit operations correctly clear the upper bits.
