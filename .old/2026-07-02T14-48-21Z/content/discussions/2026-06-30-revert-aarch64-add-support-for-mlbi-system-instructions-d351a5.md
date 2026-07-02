---
project: binutils
subsystem: gas
patch_id: null
tags:
- revert
- aarch64
- gas
- ARM
- instructions
discussion_id: 20260630094203.2328048-5-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH v3 4/7] Revert "aarch64: Add support for MLBI system instructions"'
headline: 'Revert "aarch64: Add support for MLBI system instructions"'
tldr: Reverts the addition of MLBI system instructions for aarch64 due to issues.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Reverts the commit that added support for MLBI system instructions
  to `gas/config/tc-aarch64.c` and various opcode definitions/test cases. This is
  a rollback due to potential issues with the initial implementation.
primer_general: This change reverts a previous update to the binutils software that
  added support for specific instructions related to memory management on ARM processors.
  The functionality for 'MLBI' system instructions has been temporarily removed because
  the initial implementation caused problems. This action is taken to ensure stability
  while the issues are addressed.
series_id: 'binutils:revert "aarch64: add support for mlbi system instructions"'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630094203.2328048-5-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch reverts commit d8e004f124877849c654c0f24c2960970dbc1ee8, which had added support for the MLBI (Memory-level Branch Indicator) system instructions on aarch64. The reversion indicates that the initial implementation introduced problems, leading to its removal pending further work or resolution.
