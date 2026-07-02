---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- PE/COFF
- binutils
- linker
- sections
discussion_id: 20260701175852.1111-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Safely raise PE section limit to 65279 by handling symbol section numbers as
  unsigned values.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased section limit compatibility with other toolchains.
- Improved error handling for malformed input.
- Requires new test cases to ensure correctness.
exchanges:
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: proposer
  position: Proposes to raise the normal PE section limit to 65279 by correctly handling
    symbol section numbers as unsigned values, and includes new tests for this change.
  quote: 'PE/COFF stores symbol section numbers in a 16-bit field.  Binutils used
    signed 16-bit handling there, which limited normal PE objects to 32767 sections
    even though MSVC and Clang already accept a larger unsigned range.


    Raise the normal PE section limit to 65279, while keeping the PE/COFF special
    section-number values for undefined, absolute and debug symbols working correctly.'
primer_expert: This patch modifies binutils' PE/COFF handling, specifically how symbol
  section numbers are interpreted. Historically, binutils used signed 16-bit integers
  for these numbers, limiting PE objects to 32767 sections. This change aligns binutils
  with MSVC and Clang by using unsigned 16-bit integers for normal section numbers
  up to 65279, while correctly preserving reserved values.
primer_general: PE/COFF is a file format used for executables, object code, and DLLs
  on Windows. This change in binutils addresses how the tool interprets section numbers
  within object files. Previously, a limitation in binutils restricted the number
  of sections in a PE file to 32767. This update removes that limitation, allowing
  up to 65279 sections, which is more compatible with compilers like MSVC and Clang
  and avoids potential issues with large projects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260701175852.1111-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch safely increases the maximum number of sections allowed in normal PE objects from 32767 to 65279. It achieves this by correctly decoding and encoding symbol section numbers as unsigned values, while preserving the special handling for undefined, absolute, and debug symbols. Additionally, it improves error handling by rejecting malformed reserved symbol section numbers during input reading.
