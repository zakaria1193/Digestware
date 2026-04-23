---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- zvfbfwma
- zvfbfmin
- extension dependency
- binutils
discussion_id: 77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
source_type: public_inbox
title: '[PATCH 07/19] bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
headline: 'Bfd/Risc-V: Zvfbfwma implies Zvfbfmin'
tldr: Corrects the implicit extension dependencies in the RISC-V backend, stating
  that Zvfbfwma implies Zvfbfmin.
stakes: Ensures correct feature detection and code generation for RISC-V vector floating-point
  extensions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- This change fixes a functional bug and doesn't introduce new tradeoffs.
exchanges: []
primer_expert: In `bfd/elfxx-riscv.c`, the `riscv_implicit_subsets` table defines
  implicit dependencies between RISC-V extensions. This patch corrects the entry for
  `zvfbfwma` to include `+zvfbfmin`, reflecting the ISA spec's requirement that `Zvfbfwma`
  implies `Zvfbfmin`. This ensures proper handling of these extensions by the BFD
  library.
primer_general: RISC-V uses extensions to add features like vector floating-point
  operations. Some extensions implicitly enable other extensions. This patch corrects
  the binutils configuration to reflect the correct dependencies between the `Zvfbfwma`
  and `Zvfbfmin` extensions, ensuring that the toolchain correctly recognizes and
  supports these features when compiling RISC-V code.
series_id: 'binutils:bfd/risc-v: zvfbfwma implies zvfbfmin'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch fixes an incorrect implicit dependency in the RISC-V backend of binutils. It changes the implicit subset relationship such that enabling the `Zvfbfwma` extension automatically implies the `Zvfbfmin` extension. This correction aligns with the RISC-V specification.
