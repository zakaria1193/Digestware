---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- feature removal
- build system
- ARM
discussion_id: 20260630094203.2328048-7-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH v3 6/7] aarch64: Remove +mpamv2 feature option'
headline: 'aarch64: Remove +mpamv2 feature option'
tldr: Removes the +mpamv2 feature option for aarch64 as it's no longer needed.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Removes the `+mpamv2` feature option from `tc-aarch64.c`, `c-aarch64.texi`,
  `aarch64-sys-regs.def`, and testsuite files. The rationale is that MPAMv2 system
  registers are now handled without a dedicated feature option, aligning with binutils
  conventions.
primer_general: This change removes an obsolete configuration option (`+mpamv2`) for
  the aarch64 architecture in the binutils software. This option was used to enable
  certain features, but those features are now managed differently. Removing the option
  simplifies the build process and removes unnecessary configuration choices for developers.
series_id: 'binutils:aarch64: remove +mpamv2 feature option'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630094203.2328048-7-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch removes the `+mpamv2` architecture option for aarch64. Since the remaining MPAMv2 functionalities are handled through system registers and do not require a specific feature option according to binutils conventions, this option is now obsolete. Associated test cases are also adjusted.
