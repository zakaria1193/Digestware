---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- pe/coff
- sections
- file format
- windows
discussion_id: 20260630205916.1179-3-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: 'PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Increases the maximum number of sections in PE/COFF files from 32767 to 65279
  by handling section numbers as unsigned.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Requires careful handling of reserved section number values to maintain compatibility.
- Adds new test cases to ensure correctness.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Submits a patch to increase the PE/COFF section limit by using unsigned
    arithmetic for normal section numbers, ensuring compatibility with MSVC and Clang
    and adding new tests.
  quote: Raise the normal PE section limit to 65279, while keeping the PE/COFF special
    section-number values for undefined, absolute and debug symbols working correctly.
primer_expert: This patch in binutils' PE/COFF handling modifies the interpretation
  of symbol section numbers. Historically, these were treated as signed 16-bit values
  (limiting to 32767 sections). This change decodes/encodes them as unsigned values
  (up to 65279) for normal sections, while explicitly preserving the special values
  (undefined, absolute, debug). This aligns binutils with behavior seen in MSVC and
  Clang.
primer_general: This change increases the maximum number of sections that can be defined
  within a Windows Portable Executable (PE) file. Previously, the tools used to process
  these files limited the number of sections to around 32,000 due to how they interpreted
  section numbers. This update allows for a much higher number of sections (up to
  ~65,000) by correctly treating these numbers as unsigned, aligning with modern compiler
  capabilities and enabling larger, more complex executables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630205916.1179-3-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

Oleg Tolmatcev proposes safely raising the section limit in PE/COFF files. Previously, binutils used signed 16-bit integers for section numbers, limiting objects to 32767 sections. This change introduces unsigned handling for normal PE section numbers, increasing the limit to 65279 while preserving special reserved section values. New tests are included to verify this extended range.
