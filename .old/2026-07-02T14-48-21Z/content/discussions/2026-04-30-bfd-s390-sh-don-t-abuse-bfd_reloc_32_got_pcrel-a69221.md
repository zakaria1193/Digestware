---
project: binutils
subsystem: bfd/s390+sh
patch_id: null
tags:
- bfd
- relocation
- s390
- sh
- code quality
discussion_id: orlde5hy5u.fsf@lxoliva.fsfla.org
source_type: public_inbox
title: 'Re: [PATCH 5/8] bfd/s390+sh: don''t abuse BFD_RELOC_32_GOT_PCREL'
headline: 'Bfd/s390+sh: Don''t abuse BFD_RELOC_32_GOT_PCREL'
tldr: Fixes incorrect usage of a PC-relative relocation enumerator for non-PC-relative
  relocations in the s390 and SH backends of the Binary File Descriptor (BFD) li…
proposer: Alexandre Oliva <oliva@gnu.org>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Corrects existing mis-use of relocation enumerators.
exchanges:
- author: Alexandre Oliva <oliva@gnu.org>
  role: proposer
  position: Agrees to the changes for SH.
  quote: SH bits look good, thanks.
primer_expert: The BFD library uses relocation enumerators to describe how to adjust
  addresses in object files during linking. This patch corrects the use of `BFD_RELOC_32_GOT_PCREL`
  which specifies a 32-bit relocation relative to the Program Counter (PC).  The s390
  and SH backends were incorrectly using it for non-PC-relative GOT relocations.
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that provides a uniform interface for manipulating different object file formats.
  Relocations are adjustments applied to addresses within object files or executables
  during linking or loading, to account for the final memory location of code and
  data. PC-relative relocations calculate addresses relative to the current instruction's
  location. This patch fixes an incorrect assumption about which relocations are PC-relative,
  ensuring correct code execution.
series_id: 'binutils:bfd/s390+sh: don''t abuse bfd_reloc_32_got_pcrel'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/orlde5hy5u.fsf@lxoliva.fsfla.org
bugzilla_url: null
date: '2026-04-30'
---

This patch corrects the usage of `BFD_RELOC_32_GOT_PCREL` in the s390 and SH backends of the BFD library. The enumerator was being incorrectly used for `R_390_GOT32` and `R_SH_GOT32` relocations, which are not PC-relative. Correcting this usage helps to properly use the enumerator and avoids potential issues in the future.
