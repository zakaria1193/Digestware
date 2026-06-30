---
project: binutils
subsystem: bfd/readelf
patch_id: null
tags:
- elf
- core dump
- readelf
- ARM
- debugging
discussion_id: 20260629073158.36053-1-srinath.parvathaneni@arm.com
source_type: public_inbox
title: '[PATCH v1] bfd/readelf: Add core file support for FEAT_S1POE'
headline: 'bfd/readelf: Add core file support for FEAT_S1POE'
tldr: Adds support for reading NT_ARM_POE notes in core files.
proposer: srinath.parvathaneni@arm.com
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Adds support for the NT_ARM_POE note type within the BFD library's
  core file handling. This involves registering a new note type handler in `elfcore_grok_note`
  and implementing `elfcore_grok_aarch_poe` to create a pseudo-section for it.
primer_general: This patch enhances the binutils software, specifically the readelf
  tool and its underlying library (BFD), to understand and display a new type of information
  found in Linux core dump files on ARM processors. This information, related to 'FEAT_S1POE',
  is now correctly parsed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260629073158.36053-1-srinath.parvathaneni@arm.com
bugzilla_url: null
date: '2026-06-29'
is_stub: false
stub_reason: ''
---

This patch introduces support for the NT_ARM_POE note type in core files, enabling the readelf utility to process and display this information. The changes involve modifications to BFD's ELF core file handling and the readelf program itself. The author has regression tested this on an aarch64 target.
