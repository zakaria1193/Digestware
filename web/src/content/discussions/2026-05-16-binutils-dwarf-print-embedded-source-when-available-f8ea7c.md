---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- dwarf
- debugging
- objdump
- source code
discussion_id: 20260516104948.543067-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v6] binutils/dwarf: Print embedded source, when available'
headline: 'binutils/dwarf: Print embedded source, when available'
tldr: objdump now prints embedded source code from DWARFv5, enabling easier debugging
  when source files are unavailable.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased size of debugging information.
- Potential performance impact when processing large amounts of embedded source.
exchanges: []
primer_expert: DWARFv5 allows embedding source code directly in the debugging information.
  This patch modifies objdump to extract and display this embedded source. The relevant
  DWARF structures are in `dwarf2.h`, and the logic for parsing and displaying the
  line table entries is in `binutils/dwarf.c`.
primer_general: DWARF is a debugging data format used to describe the structure and
  contents of compiled programs, facilitating source-level debugging. DWARFv5 introduced
  the ability to embed source code directly within the debugging information. This
  patch enhances the `objdump` utility to extract and print this embedded source code,
  which assists in debugging scenarios where the original source files are not readily
  available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260516104948.543067-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This patch enables objdump to extract and display embedded source code stored in DWARFv5 debugging information.  This is useful when the original source files are missing or inaccessible during debugging. The patch adds new tests and updates the dwarf.c file to handle the new DWARFv5 line table entry.
