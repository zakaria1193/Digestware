---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- binutils
- bfd
- vector floating-point
- isa extensions
discussion_id: 77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
source_type: public_inbox
title: '[PATCH 07/19] bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
headline: 'Bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
tldr: Clarifies that the Zvfbfwma extension implies Zvfbfmin in the RISC-V BFD backend
  for binutils.
stakes: Ensures correct dependency handling for RISC-V vector floating-point extensions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensures correct dependency handling of RISC-V extensions.
- No performance impact.
exchanges: []
primer_expert: The RISC-V BFD backend (`bfd/elfxx-riscv.c`) defines implicit subsets
  for ISA extensions. This patch corrects the implicit subset definition for `zvfbfwma`
  to include `zvfbfmin`. This ensures that when `zvfbfwma` is enabled, `zvfbfmin`
  is also implicitly enabled, adhering to the RISC-V specification.
primer_general: Binutils uses the BFD library to handle object file formats. This
  patch updates the RISC-V BFD backend to correctly specify the relationship between
  two vector floating-point extensions. If the user enables `zvfbfwma`, then `zvfbfmin`
  is implicitly enabled.
series_id: 'binutils:bfd/risc-v: zvfbfwma implies zvfbfmin'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/77e6a033-451e-4a00-bb4c-77f3d90e73bb@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the RISC-V BFD backend in binutils to explicitly state that the Zvfbfwma extension implies the Zvfbfmin extension. This is based on the RISC-V specification and ensures that the tools correctly handle the dependencies between these vector floating-point extensions.
