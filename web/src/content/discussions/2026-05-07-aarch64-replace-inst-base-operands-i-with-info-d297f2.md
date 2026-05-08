---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- refactoring
- readability
discussion_id: 54ad2177-8b3c-5845-ef14-ca086e36a4b4@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 09/23] aarch64: Replace inst.base.operands[i]. with info->'
headline: 'Aarch64: Replace inst.base.operands[i]. with info->'
tldr: Shortens code in `parse_operands` by using `info->` instead of `inst.base.operands[i].`
  where possible, as `info` is a pointer to the latter.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improved code readability and maintainability.
- No performance impact.
exchanges: []
primer_expert: This patch simplifies code in `gas/config/tc-aarch64.c::parse_operands`
  by using a pointer alias `info` instead of the full struct member access `inst.base.operands[i]`.  No
  functional change.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch makes local code more readable.'
series_id: 'binutils:aarch64: replace inst.base.operands[i]. with info->'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/54ad2177-8b3c-5845-ef14-ca086e36a4b4@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch refactors the `parse_operands` function in the AArch64 assembler to use the `info->` pointer, which points to `inst.base.operands[i]`, instead of the longer form `inst.base.operands[i].` directly. This change simplifies the code and improves readability, without altering functionality.
