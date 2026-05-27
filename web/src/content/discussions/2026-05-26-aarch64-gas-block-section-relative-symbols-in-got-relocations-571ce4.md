---
project: binutils
subsystem: binutils
patch_id: null
tags:
- AArch64
- assembler
- GOT
- relocation
- PIC
discussion_id: PAWPR08MB8982EA96A85A9846678CCFB5830B2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: '[PATCH] AArch64 gas: Block section relative symbols in GOT relocations [PR30788]'
headline: 'AArch64 gas: Block section relative symbols in GOT relocations'
tldr: This patch prevents the AArch64 assembler from incorrectly using section-relative
  symbols in GOT relocations, fixing PR30788.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses an issue in the AArch64 assembler's handling of
  GOT relocations. The assembler was incorrectly allowing section-relative symbols
  to be used in GOT relocations, which is invalid on AArch64. This could lead to runtime
  errors due to incorrect address calculations.
primer_general: The Global Offset Table (GOT) is a data structure used in position-independent
  code (PIC) to hold the addresses of global variables. This patch fixes a bug in
  the AArch64 assembler that could cause it to generate incorrect code when accessing
  global variables, potentially leading to crashes or incorrect program behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/PAWPR08MB8982EA96A85A9846678CCFB5830B2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

Wilco Dijkstra proposes a patch to the AArch64 assembler to prevent the generation of section-relative symbols in Global Offset Table (GOT) relocations.  This is incorrect because GOT relocations do not support offsets. The patch updates `aarch64_fix_adjustable()` to explicitly disallow this, resolving PR30788.
