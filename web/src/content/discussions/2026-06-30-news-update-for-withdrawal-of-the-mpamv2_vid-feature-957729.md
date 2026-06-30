---
project: binutils
subsystem: news
patch_id: null
tags:
- aarch64
- news
- feature removal
- ARM
discussion_id: 20260630094203.2328048-8-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH v3 7/7] NEWS: Update for withdrawal of the MPAMv2_VID feature.'
headline: 'NEWS: Update for withdrawal of the MPAMv2_VID feature.'
tldr: Update NEWS file to reflect withdrawal of aarch64 MPAMv2_VID feature.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: withdrawn
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Updates the `gas/NEWS` file to reflect the withdrawal of the aarch64
  MPAMv2_VID feature, similar to the TME extension. It notes that these features were
  never implemented and have been removed from the architecture. The assembler will
  now warn on their use.
primer_general: This change updates the release notes for the binutils software. It
  informs users that certain features for ARM processors, specifically MPAMv2_VID
  and TME, have been officially removed from the architecture by Arm because they
  were never implemented in real products. The assembler will now warn developers
  if they attempt to use these withdrawn features.
series_id: 'binutils:news: update for withdrawal of the mpamv2_vid feature'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630094203.2328048-8-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch updates the NEWS file to announce the withdrawal of the aarch64 MPAMv2_VID feature, alongside the TME extension. Arm has withdrawn these features from the architecture as they were never implemented in products. The assembler will now issue warnings for any detected use of these features.
