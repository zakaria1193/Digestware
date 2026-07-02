---
project: binutils
subsystem: bfd/sh
patch_id: null
tags:
- bfd
- relocation
- sh
- code cleanup
discussion_id: ortssthyck.fsf@lxoliva.fsfla.org
source_type: public_inbox
title: 'Re: [PATCH 3/8] bfd/sh: drop unused relocation enumerators'
headline: 'Bfd/sh: Drop unused relocation enumerators'
tldr: Removes unused relocation enumerators in the SH backend of the Binary File Descriptor
  (BFD) library, likely leftovers from SH5's 64-bit ISA.
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
  position: Agrees with dropping the unused relocation enumerators, suspects they
    are leftovers from SH5's 64-bit ISA.
  quote: 'Ok, thanks.


    I''m pretty sure these are left-overs from SH5''s 64-bit ISA, SHmedia.'
primer_expert: The Binary File Descriptor (BFD) library uses relocation enumerators
  to define how to adjust addresses in object files during linking. This patch removes
  unused enumerators specific to the SH architecture. These are likely remnants from
  the SH5 architecture's 64-bit ISA, SHmedia, which was never fully implemented.
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that provides a uniform interface for manipulating different object file formats.  Relocation
  enumerators are symbolic names for different types of address fixups that might
  be needed when linking or loading code. This patch removes definitions for fixups
  that are no longer used, which simplifies the BFD code and reduces the risk of accidentally
  using an incorrect fixup type.
series_id: 'binutils:bfd/sh: drop unused relocation enumerators'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ortssthyck.fsf@lxoliva.fsfla.org
bugzilla_url: null
date: '2026-04-30'
---

This patch removes unused relocation enumerators from the SH backend of the BFD library. These enumerators are likely remnants from the SH5 architecture's 64-bit ISA, SHmedia, which never fully materialized. Removing them cleans up the code and prevents potential confusion or misuse.
