---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- gas
- relocation
- fixup
discussion_id: 20260924014435.30185-2-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3 1/4] microblaze: add BFD_RELOC_8 and BFD_RELOC_16 cases'
headline: 'microblaze: add BFD_RELOC_8 and BFD_RELOC_16 cases'
tldr: Adds support for 8-bit and 16-bit relocations in MicroBlaze's `md_apply_fix`
  function.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds explicit handling for 8-bit and 16-bit relocations.
- Uses `md_number_to_chars` for consistent byte writing, simplifying the code.
- Fixes test cases and improves assembler robustness for MicroBlaze.
exchanges: []
primer_expert: This patch, the first in a series for MicroBlaze `md_apply_fix` and
  `md_assemble` cleanup, adds handling for 8-bit and 16-bit relocations. The `md_apply_fix`
  function in `gas/config/tc-microblaze.c` previously lacked explicit cases for `BFD_RELOC_8`
  and `BFD_RELOC_16`, causing them to fall through and result in zero-value fixups.
  This change adds these cases, utilizing `md_number_to_chars` for writing the values
  in target byte order. This resolves the `gas/all/simple-forward` test and allows
  the `gas/all/forward` test to be removed from the xfail list. The test results show
  a reduction in une…
primer_glossary:
- term: md_apply_fix
  definition: A BFD function responsible for applying relocation fixups to data or
    code during the assembly process for a specific target architecture.
- term: BFD_RELOC_8
  definition: A relocation type indicating an 8-bit value needs to be adjusted.
- term: BFD_RELOC_16
  definition: A relocation type indicating a 16-bit value needs to be adjusted.
- term: md_number_to_chars
  definition: A generic BFD utility function that converts a number into a sequence
    of bytes respecting the target's endianness.
- term: Fixup
  definition: A placeholder in assembled code that needs to be resolved by the linker
    to a final address or value. In this context, if a fixup is not properly handled,
    it can lead to incorrect code.
series_id: 'binutils:microblaze: add bfd_reloc_8 and bfd_reloc_16 cases'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924014435.30185-2-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch introduces support for `BFD_RELOC_8` and `BFD_RELOC_16` relocations within the MicroBlaze assembler's `md_apply_fix` function. Previously, these relocation types were not handled, causing byte or halfword data that was only known at fixup time to be assembled as zero. This would then be resolved to `BFD_RELOC_NONE`, preventing the linker from correcting the value. The patch implements these cases using `md_number_to_chars`, which writes in the target's byte order, thus fixing issues in the `gas/all/simple-forward` test and removing an xfail for `gas/all/forward`. The test suite results show an improvement in passing counts for both `microblaze-elf` and `microblazeel-elf`.
