---
project: binutils
subsystem: fw
patch_id: null
tags:
- binutils
- readelf
- debugging
- DWARF
- patch review
discussion_id: 4bc8cb07-c3f7-4a0b-82c4-b2b997609924@suse.com
source_type: public_inbox
title: 'Re: FW: [PATCH] readelf: attach location views to DW_LLE_startx_endx/startx_length
  loclists'
headline: 'FW: [PATCH] readelf: attach location views to DW_LLE_startx_endx/startx_length
  loclists'
tldr: A reviewer requests specification details for DW_AT_GNU_locviews to validate
  a readelf patch.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Patch improves accuracy and reduces spurious warnings in `readelf` output for DWARF
  5 files.
- Reviewer's request for specification ensures adherence to standards and long-term
  maintainability.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Requests a specification pointer for DW_AT_GNU_locviews to validate a
    patch that addresses DWARF 5 location list processing.
  quote: While this looks entirely plausible, I wanted to check it against some kind
    of spec. Thing is - I don't appear to be able to locate such a spec for DW_AT_GNU_locviews
    (which is what I think would be relevant here). Can you perhaps provide a pointer?
primer_expert: This discussion centers on a patch to `readelf` that addresses a warning
  related to DWARF 5 location lists, specifically for the `DW_LLE_startx_endx` and
  `DW_LLE_startx_length` forms. The patch correctly decodes the location view pairs
  associated with these entries, which were previously unread, preventing a spurious
  'Hole and overlap detection requires adjacent view lists and loclists' warning.
  The reviewer is seeking definitive DWARF standard documentation for `DW_AT_GNU_locviews`
  to cross-reference the patch's logic.
primer_glossary:
- term: readelf
  definition: A utility from the GNU Binutils package that displays information about
    ELF (Executable and Linkable Format) files, including debugging information.
- term: location lists
  definition: A feature in DWARF debugging information that specifies the memory locations
    of variables or expressions at different points in the program's execution.
- term: DW_AT_GNU_locviews
  definition: A DWARF attribute, specific to GNU extensions, that associates location
    lists with particular views or contexts. This is relevant for advanced debugging
    scenarios.
- term: DW_LLE_startx_endx
  definition: A DWARF Location List Entry (LLE) format that defines a range by a starting
    offset plus a length, used for indexed location lists.
- term: DW_LLE_startx_length
  definition: Similar to DW_LLE_startx_endx, another DWARF Location List Entry format
    for indexed location lists, specifying a start and length.
- term: DWARF 5
  definition: The fifth version of the DWARF debugging data format standard. It introduced
    new features and clarifications, including enhanced location list handling.
- term: PR binutils/34366
  definition: A reference to a specific bug report (Problem Report) filed against
    the Binutils project, tracking an issue or feature request.
series_id: 4bc8cb07-c3f7-4a0b-82c4-b2b997609924@suse.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/4bc8cb07-c3f7-4a0b-82c4-b2b997609924@suse.com
bugzilla_url: null
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

Jan Beulich requested a specification reference for DW_AT_GNU_locviews after reviewing a patch by Kamil Bucki. The patch aims to fix a warning in readelf concerning location lists in DWARF 5 objects by correctly processing indexed bounded forms. Beulich seeks a spec to confirm the patch's correctness.
