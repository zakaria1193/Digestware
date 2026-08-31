---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- xtensa
- relocation
- dwarf
- debugging
- patch
discussion_id: 32d0ae39fbeb6106c3054c89e24512baa5141b9b.camel@espressif.com
source_type: public_inbox
title: 'Re: [PATCH v3] xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
headline: 'xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
tldr: A review is requested for a patch adding a new relocation type for Xtensa DWARF
  debugging information.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reserving a relocation type number preemptively might conflict with future needs
  if not carefully managed.
- The effectiveness of this relocation depends on the specific tooling and compilers
  supporting Xtensa and DWARF.
exchanges:
- author: Alexey Lapshin <alexey.lapshin@espressif.com>
  role: proposer
  position: Requests a review for a patch adding a new Xtensa relocation type and
    asks to reserve a reloc type number.
  quote: 'Gentle ping. A review would be much appreciated.


    If review needs more time, could we at least

    reserve reloc type 63 for R_XTENSA_PDIFF_ULEB128?'
primer_expert: This patch introduces a new ELF relocation type, R_XTENSA_PDIFF_ULEB128,
  for the Xtensa architecture. This relocation is specifically for handling differences
  in unsigned LEB128 encoded values within DWARF debugging information. The author
  is seeking a review and proposing a reservation for the relocation type number.
primer_glossary:
- term: Xtensa
  definition: A configurable and extensible processor architecture used in various
    embedded systems, particularly by Tensilica (now part of Cadence).
- term: R_XTENSA_PDIFF_ULEB128
  definition: A custom ELF relocation type proposed for the Xtensa architecture, designed
    to calculate differences between unsigned LEB128 encoded values.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about variables, types, and code structure.
- term: uleb128
  definition: Unsigned Little-Endian Base 128. A variable-length encoding for unsigned
    integers, commonly used in DWARF and other formats.
- term: relocation
  definition: A process performed by the linker to resolve symbol references and adjust
    addresses in object files and executables.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program or another object file.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/32d0ae39fbeb6106c3054c89e24512baa5141b9b.camel@espressif.com
bugzilla_url: null
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

Alexey Lapshin is gently pinging for a review of a patch that adds the R_XTENSA_PDIFF_ULEB128 relocation type, intended for DWARF uleb128 diffs on Xtensa architectures. Without immediate review, they request that reloc type 63 be reserved for this purpose.
