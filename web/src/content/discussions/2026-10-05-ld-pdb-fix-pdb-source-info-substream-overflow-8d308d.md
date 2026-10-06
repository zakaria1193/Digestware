---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- binutils
- linker
- pdb
- windows
- overflow
discussion_id: 4394290d-8569-48a0-9260-35ebb0ca3f49@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld/pdb: Fix PDB source-info substream overflow'
headline: 'ld/pdb: Fix PDB source-info substream overflow'
tldr: A fix for a PDB substream overflow bug in the linker by increasing the size
  of a counter.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased memory usage for the `source_files_count` variable, though negligible.
- Fixes a potential crash/corruption bug.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Acknowledges and accepts the proposed fix.
  quote: Okay.
- author: Oleg Tolmatcev
  role: proposer
  position: Explains that `source_files_count` was too narrow and caused buffer overflows
    when exceeding 65,535 references, proposing to change it to `uint32_t`.
  quote: 'source_files_count counts every source file reference across all

    modules, not the deduplicated count that goes into the substream

    header, so a uint16_t is too narrow. A link with more than 65535

    references wraps it, allocates too small a buffer for the source-info

    substream, and then writes past the end of it.'
primer_expert: This patch in `ld/pdb.c` fixes a buffer overflow vulnerability within
  the PDB (Program Database) generation for Windows executables. The overflow occurs
  in the `create_source_info_substream` function when the number of unique source
  file entries exceeds the capacity of a `uint16_t` used to track them. By promoting
  `source_files_count` to `uint32_t`, the linker can correctly handle larger object
  files with numerous source files, preventing writes beyond the allocated buffer
  for the PDB's source information substream.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft Windows to store information
    about executable files, used by debuggers and other tools.
- term: linker
  definition: A program that combines object code from multiple sources into a single
    executable or library.
- term: substream
  definition: A smaller, logically distinct part of a larger data structure, such
    as within a PDB file.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4394290d-8569-48a0-9260-35ebb0ca3f49@suse.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the linker's PDB (Program Database) handling where a `uint16_t` counter for source file references could overflow if a link involved more than 65,535 references. This overflow led to a buffer allocation that was too small for the source-info substream, resulting in a write past the buffer's end. The fix changes the counter to `uint32_t` to accommodate a larger number of references.
