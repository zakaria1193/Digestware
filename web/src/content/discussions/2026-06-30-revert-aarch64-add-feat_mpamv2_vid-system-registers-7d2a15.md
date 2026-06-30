---
project: binutils
subsystem: gas
patch_id: null
tags:
- revert
- aarch64
- gas
- ARM
- registers
discussion_id: 20260630094203.2328048-6-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH v3 5/7] Revert "aarch64: Add FEAT_MPAMv2_VID system registers"'
headline: 'Revert "aarch64: Add FEAT_MPAMv2_VID system registers"'
tldr: Reverts the addition of MPAMv2_VID system registers for aarch64.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Reverts the commit that added FEAT_MPAMv2_VID system registers in `aarch64-sys-regs.def`
  and related test files. This rollback removes support for these specific system
  registers, possibly due to the feature's withdrawal or implementation issues.
primer_general: This change removes support for certain system registers related to
  the MPAMv2_VID feature on ARM processors from the binutils software. Previously
  added support has been rolled back, indicating a potential issue or a change in
  the feature's status. This ensures the assembler does not incorrectly handle these
  registers.
series_id: 'binutils:revert "aarch64: add feat_mpamv2_vid system registers"'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630094203.2328048-6-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch reverts commit 5fc6b09c078532fa4206a350e34d82488b80a5fb, which had added support for the FEAT_MPAMv2_VID system registers on aarch64. The reversion removes these registers and associated test cases, likely due to issues or a change in feature status that requires their removal.
