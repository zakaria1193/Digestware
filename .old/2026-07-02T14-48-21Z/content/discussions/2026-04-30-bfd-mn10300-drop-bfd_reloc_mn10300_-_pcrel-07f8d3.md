---
project: binutils
subsystem: bfd/mn10300
patch_id: null
tags:
- bfd
- relocation
- mn10300
- code cleanup
discussion_id: ory0i5hyfa.fsf@lxoliva.fsfla.org
source_type: public_inbox
title: 'Re: [PATCH 2/8] bfd/mn10300: drop BFD_RELOC_MN10300_*_PCREL'
headline: 'Bfd/mn10300: Drop BFD_RELOC_MN10300_*_PCREL'
tldr: Removes unused PC-relative relocation enumerators for the mn10300 architecture
  in the Binary File Descriptor (BFD) library.
proposer: Alexandre Oliva <oliva@gnu.org>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code.
exchanges:
- author: Alexandre Oliva <oliva@gnu.org>
  role: proposer
  position: Agrees to drop the unused PC-relative relocation enumerators.
  quote: Ok, thanks
primer_expert: The BFD library uses relocation enumerators to describe how to adjust
  addresses in object files during linking. This patch removes unused PC-relative
  relocation enumerators specific to the mn10300 architecture.  These relocations
  are relative to the Program Counter (PC).
primer_general: The Binary File Descriptor (BFD) library provides a uniform interface
  for manipulating different object file formats. Relocations are adjustments applied
  to addresses within object files or executables during linking or loading, to account
  for the final memory location of code and data. PC-relative relocations calculate
  addresses relative to the current instruction's location. This patch removes definitions
  for PC-relative fixups that are no longer used for the mn10300 architecture.
series_id: 'binutils:bfd/mn10300: drop bfd_reloc_mn10300_*_pcrel'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ory0i5hyfa.fsf@lxoliva.fsfla.org
bugzilla_url: null
date: '2026-04-30'
---

This patch removes unused PC-relative relocation enumerators (`BFD_RELOC_MN10300_*_PCREL`) from the mn10300 backend of the BFD library. These enumerators are not currently used. Removing them cleans up the code and reduces the potential for confusion.
