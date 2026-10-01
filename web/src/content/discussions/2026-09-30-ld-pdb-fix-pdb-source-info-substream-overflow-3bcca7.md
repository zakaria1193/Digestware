---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- debugging
- overflow
- bugfix
discussion_id: 20260930193657.733-8-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] ld/pdb: Fix PDB source-info substream overflow'
headline: 'ld/pdb: Fix PDB source-info substream overflow'
tldr: Fixes buffer overflow in PDB source-info substream by using a 32-bit count for
  source files.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The PDB writer in binutils' linker (ld) was susceptible to a buffer
  overflow when generating the source-info substream. The `source_files_count` variable,
  intended to track the number of unique source files referenced across all modules,
  was declared as `uint16_t`. However, the logic for calculating this count did not
  deduplicate references, leading to a potentially much larger number if a single
  source file was included in many object files. When this count exceeded 65535, it
  wrapped around, causing `create_source_info_substream` to allocate a buffer that
  was too small. This patch corrects t…
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or shared library.
- term: substream
  definition: A distinct section or part of a larger data stream within the PDB file
    format, used to organize different types of information.
- term: buffer overflow
  definition: A condition where a program attempts to write data beyond the allocated
    buffer, potentially corrupting adjacent memory and causing instability or security
    vulnerabilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-8-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch resolves a buffer overflow vulnerability in the PDB source-info substream generation. The `source_files_count` was incorrectly using a 16-bit integer, which would wrap around for links with more than 65535 source file references. This led to an undersized buffer allocation for the substream, causing writes past its boundaries. The fix changes `source_files_count` to a 32-bit integer and includes new test cases to verify the correction.
