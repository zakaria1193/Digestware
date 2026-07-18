---
project: binutils
subsystem: fw
patch_id: null
tags:
- binutils
- readelf
- DWARF
- debugging
- GCC
discussion_id: 7ac24bb0-2107-4ffd-8df0-bcd50d00287e@suse.com
source_type: public_inbox
title: 'Re: FW: [PATCH] readelf: attach location views to DW_LLE_startx_endx/startx_length
  loclists'
headline: 'FW: [PATCH] readelf: attach location views to DW_LLE_startx_endx/startx_length
  loclists'
tldr: Discussion on the specification and implementation of GNU's non-standard DW_AT_GNU_locviews
  attribute in DWARF debugging information.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Supporting non-standard extensions like `DW_AT_GNU_locviews` improves debugging
  capabilities for users of specific toolchains but complicates standardization efforts.
- The lack of a formal specification for these extensions makes it challenging for
  other tools (like `readelf`) to interpret the debugging information correctly.
exchanges:
- author: Kamil Bucki (Nokia)
  role: contributor
  position: Explains that DW_AT_GNU_locviews is a GNU extension, not a standardized
    DWARF attribute, and provides pointers to its origin and related GCC code.
  quote: Thanks for checking. You're right that there is no entry for DW_AT_GNU_locviews
    in the official DWARF standard - it isn't a standardized attribute. It's a GNU
    (GCC) extension ("Location Views" / LVU), so the lack of a spec in the DWARF documents
    is expected rather than a mistake on our side.
- author: Jan Beulich
  role: reviewer
  position: Expresses difficulty in finding information about the encoding of location
    views, specifically for `DW_LLE_startx_endx`/`startx_length` loclists and `DW_LLE_offset_pair`,
    in the provided documentation.
  quote: 'Neither this nor ...

    ... this helps me very much. I''m perhaps blind, but I can''t spot anything

    towards the encoding this patch is about, also not for DW_LLE_start_{end,length}.

    Neither document mentions DW_LLE_offset_pair at all.'
primer_expert: The discussion centers on the `DW_AT_GNU_locviews` attribute, a non-standard
  extension to the DWARF debugging format introduced by GCC. This attribute provides
  'location views' for variables, allowing more detailed information about variable
  locations, especially in optimized code. The patch in question deals with `readelf`'s
  ability to interpret location lists encoded with `DW_LLE_startx_endx`, `DW_LLE_startx_length`,
  and potentially `DW_LLE_offset_pair`. The core of the debate is the clarity and
  completeness of the specification for these encodings, with Jan Beulich seeking
  definitive docum…
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers, debuggers, and profiling
    tools. It provides information about variables, functions, types, and code structure.
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files, including DWARF debugging information.
- term: DW_AT_GNU_locviews
  definition: A non-standard GCC extension attribute within DWARF, used to specify
    location views for variables.
- term: location lists
  definition: A DWARF mechanism that describes the memory locations of a variable
    over different program execution ranges.
- term: DW_LLE_startx_endx
  definition: A DWARF Location List Entry (LLE) opcode indicating the start and end
    of a range for which the subsequent location description is valid.
- term: DW_LLE_startx_length
  definition: A DWARF LLE opcode indicating the start of a range and its subsequent
    length, for which the location description is valid.
- term: DW_LLE_offset_pair
  definition: A DWARF LLE format consisting of two values, typically representing
    a start and end offset for a location range.
- term: GCC
  definition: The GNU Compiler Collection, a widely used compiler system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/7ac24bb0-2107-4ffd-8df0-bcd50d00287e@suse.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This email thread discusses the `DW_AT_GNU_locviews` attribute in DWARF debugging information, a GNU extension not yet part of the official DWARF standard. Jan Beulich raises concerns about the lack of clear specification for the encoding of location views, particularly for `DW_LLE_startx_endx`/`startx_length` loclists and `DW_LLE_offset_pair`. Kamil Bucki clarifies that it's a GNU extension and points to existing GCC source code and a design document for more details. However, Beulich still finds the provided documentation insufficient for understanding the specific encoding mentioned in the patch.
