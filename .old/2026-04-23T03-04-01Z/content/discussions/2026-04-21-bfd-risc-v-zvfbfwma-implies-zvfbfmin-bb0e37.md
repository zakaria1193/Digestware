---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- binutils
- bfd
- zvfbfwma
- zvfbfmin
discussion_id: 77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
source_type: public_inbox
title: '[PATCH 07/19] bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
headline: 'Bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
tldr: 'Updates RISC-V implicit subset dependencies: Zvfbfwma now implies Zvfbfmin.'
stakes: Ensures correct feature dependencies are enabled when using the Zvfbfwma extension.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensures correct implicit feature enabling.
- No impact if the user explicitly enables both Zvfbfwma and Zvfbfmin.
exchanges: []
primer_expert: The BFD library uses implicit subset dependencies to automatically
  enable required features based on other enabled features. This patch modifies the
  `riscv_implicit_subsets` table in `bfd/elfxx-riscv.c` to reflect the dependency
  between Zvfbfwma and Zvfbfmin.
primer_general: When working with RISC-V, certain extensions require other extensions
  to be present. This patch updates the toolchain to automatically enable the Zvfbfmin
  extension when the Zvfbfwma extension is enabled, due to their dependency.
series_id: 'binutils:bfd/risc-v: zvfbfwma implies zvfbfmin'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the implicit subset dependencies for RISC-V configurations.  Specifically, it changes the dependency such that enabling the Zvfbfwma extension also implicitly enables the Zvfbfmin extension. This aligns with the RISC-V specification.
