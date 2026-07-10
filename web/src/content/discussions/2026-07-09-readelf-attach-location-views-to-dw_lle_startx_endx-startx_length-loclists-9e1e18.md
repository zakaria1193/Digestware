---
project: binutils
subsystem: firmware
patch_id: null
tags:
- readelf
- dwarf
- debugging
- bugfix
- loclists
discussion_id: AM8PR07MB8310A1AD8CF6A572F05DBE49EDFE2@AM8PR07MB8310.eurprd07.prod.outlook.com
source_type: public_inbox
title: 'FW: [PATCH] readelf: attach location views to DW_LLE_startx_endx/startx_length
  loclists'
headline: 'readelf: attach location views to DW_LLE_startx_endx/startx_length loclists'
tldr: Fixes readelf to correctly display location views for indexed bounded loclist
  entries.
proposer: Kamil Bucki <kamil.bucki@nokia.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves the accuracy and completeness of debug information displayed by `readelf`.
- Resolves a spurious warning related to location list analysis.
exchanges: []
primer_expert: The `readelf` utility's `display_loclists_list` function previously
  only processed GNU location-view pairs for simpler bounded location list entries
  (`DW_LLE_offset_pair`, `DW_LLE_start_end`, `DW_LLE_start_length`). This commit extends
  that processing to the indexed bounded forms (`DW_LLE_startx_endx`, `DW_LLE_startx_length`).
  Without this change, `readelf` would incorrectly report adjacency issues when debugging
  DWARF 5 objects that use these newer location list entry types, because the location
  view associated with the indexed range was not consumed, causing the internal `vstart`
  pointer to…
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF files, including DWARF
    debugging information.
- term: DWARF
  definition: A debugging data format used by many compilers to store information
    about variables, types, and code structure.
- term: location list
  definition: A DWARF structure that specifies the memory address ranges where a variable
    or expression is valid.
- term: DW_LLE_startx_endx
  definition: A DWARF location list entry type indicating a range defined by an index
    and an end offset.
- term: DW_LLE_startx_length
  definition: A DWARF location list entry type indicating a range defined by an index
    and a length.
- term: DW_AT_GNU_locviews
  definition: A GNU-specific DWARF attribute that provides a mapping between location
    list entries and their corresponding views.
- term: loclists
  definition: Abbreviation for location lists, used in DWARF debugging information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/AM8PR07MB8310A1AD8CF6A572F05DBE49EDFE2@AM8PR07MB8310.eurprd07.prod.outlook.com
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in `readelf` where location views associated with indexed bounded location list entries (`DW_LLE_startx_endx` and `DW_LLE_startx_length`) were not being displayed. The `display_loclists_list` function decodes the range for these entries but fails to consume the corresponding view pair, causing `vstart` to lag and resulting in a spurious 'Hole and overlap detection' warning. By including these two indexed forms in the processing logic, the patch ensures that their view pairs are consumed and printed, resolving the warning and improving debug information display.
