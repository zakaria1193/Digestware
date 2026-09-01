---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- binutils
- xtensa
- dwarf
- debugging
- linker
discussion_id: d7cf1d0c5b4096889659c0016b210febbdfe38eb.camel@espressif.com
source_type: public_inbox
title: 'Re: [PATCH v3] xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
headline: 'xtensa: add R_XTENSA_PDIFF_ULEB128 for DWARF uleb128 diffs'
tldr: Introduces R_XTENSA_PDIFF_ULEB128 relocation for DWARF 5 location/range lists.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Enables linker relaxation for functions with DWARF 5 debug info.
- Introduces a new relocation type, increasing complexity.
exchanges:
- author: Alexey Lapshin <alexey.lapshin@espressif.com>
  role: proposer
  position: Requests a review for the patch and suggests reserving reloc type 63 if
    a full review is not immediately possible.
  quote: Gentle ping. A review would be much appreciated. If review needs more time,
    could we at least reserve reloc type 63 for R_XTENSA_PDIFF_ULEB128?
- author: Max Filippov <jcmvbkbc@gmail.com>
  role: reviewer
  position: Acknowledges the patch and indicates that the necessary changes for DWARF
    5 location and range lists have been incorporated.
  quote: 'DWARF 5 location and range lists encode many same-section symbol

    differences as uleb128.  Today the assembler must mark all covered code

    no_transform so linker relaxation cannot change those differences, which

    effectively disables relaxation for nearly every function that has DWARF 5

    debug info.


    Emit R_XTENSA_PDIFF_ULEB128 instead: like R_XTENSA_PDIFF32 the difference

    stays in the section cont'
primer_expert: This patch introduces `R_XTENSA_PDIFF_ULEB128` to better support DWARF
  5 location and range lists on Xtensa. These lists use `uleb128` to encode differences
  between same-section symbols. Previously, the assembler had to disable linker relaxation
  (`no_transform`) for all code within such functions to prevent these differences
  from being altered. The new relocation allows relaxation to proceed by encoding
  these differences in a way that the linker can handle, specifically for Xtensa's
  DWARF support.
primer_glossary:
- term: R_XTENSA_PDIFF_ULEB128
  definition: A new relocation type proposed for Xtensa, designed to encode unsigned
    little-endian base 128 differences used in DWARF debug information.
- term: DWARF 5
  definition: The fifth version of the DWARF debugging data format specification.
- term: uleb128
  definition: Unsigned Little Endian Base 128. A variable-length encoding used in
    DWARF for unsigned integers.
- term: location lists
  definition: DWARF data structures that specify the address ranges where a variable
    is valid.
- term: range lists
  definition: DWARF data structures used to indicate the address ranges of various
    program entities.
- term: linker relaxation
  definition: An optimization process where the linker adjusts code or data addresses
    and instruction encodings to improve efficiency or code size.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/32d0ae39fbeb6106c3054c89e24512baa5141b9b.camel@espressif.com
bugzilla_url: null
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This patch introduces a new relocation type, R_XTENSA_PDIFF_ULEB128, to handle differences in DWARF 5 location and range lists that are encoded as uleb128. Previously, such differences would force linker relaxation to be disabled for entire functions containing DWARF 5 debug info. This new relocation allows relaxation to continue by encoding these differences more efficiently.
