---
project: binutils
subsystem: mips
patch_id: null
tags:
- mips
- a.out
- gold
- processor classification
discussion_id: alpine.DEB.2.21.2611081808180.17804@angie.orcam.me.uk
source_type: public_inbox
title: '[committed] MIPS: Correct LSI CW4010 classification for a.out/gold'
headline: 'MIPS: Correct LSI CW4010 classification for a.out/gold'
tldr: Classifies LSI CW4010 processor core as MIPS II for a.out and gold formats.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This change adjusts the processor core identification for the LSI CW4010
  within the MIPS architecture's a.out and gold object file formats. Specifically,
  it ensures the 'mach_mips4010' value is correctly associated with the MIPS II architecture,
  aligning its classification across different toolchain components like BFD and gold.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2611081808180.17804@angie.orcam.me.uk
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This commit corrects the classification of the LSI MiniRISC CW4010 processor core to MIPS II for both a.out and gold formats. It complements a previous commit that marked the LSI CW4010 as MIPS II for BFD.
