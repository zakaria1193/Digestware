---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- assert
- register qualifier
discussion_id: dce49376-b6cb-2817-3e5c-3d15416a5a76@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 10/23] aarch64: Add an assert to inherent_reg_qualifier'
headline: 'Aarch64: Add an assert to inherent_reg_qualifier'
tldr: Adds an assert to the default case of `inherent_reg_qualifier` function in `tc-aarch64.c`,
  marking it as unreachable.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improved code clarity and error detection during development.
- No runtime performance impact, as the assert is only enabled during development
  builds.
exchanges: []
primer_expert: The patch adds `gas_assert (0)` to the default case in `gas/config/tc-aarch64.c::inherent_reg_qualifier`.
  This function determines operand qualifiers for AArch64 registers. The default case
  was intended to be unreachable; this change turns it into an assertion, which will
  halt execution if triggered during assembly.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch adds a safety check to a function that determines extra
  properties of registers, to detect unforeseen cases during assembly.'
series_id: 'binutils:aarch64: add an assert to inherent_reg_qualifier'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/dce49376-b6cb-2817-3e5c-3d15416a5a76@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch adds an assert to the default case of the `inherent_reg_qualifier` function, which should be unreachable. This change clarifies the code's logic and helps catch potential errors during development by triggering an assertion if the default case is ever reached.
