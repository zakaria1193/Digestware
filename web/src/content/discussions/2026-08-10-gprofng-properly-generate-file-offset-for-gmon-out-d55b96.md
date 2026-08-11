---
project: binutils
subsystem: gprofng
patch_id: null
tags: []
discussion_id: CAMe9rOpYCtZT3UzHLuhRtq0nCG443bwiygD-cUMtfAKt_HkEGQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH] gprofng: Properly generate file offset for gmon.out'
headline: 'gprofng: Properly generate file offset for gmon.out'
tldr: Patch corrects gprofng's map file generation by using the correct file offset
  from core_text_sect.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to fix gprofng's map file generation for gmon.out by using
    the correct file offset.
  quote: 'When generating the map file for gmon.out, get the file offset from the

    filepos field of core_text_sect.  This fixes


    FAIL: tmpdir/gp-gmon


    on Linux/x86-64.


    PR gprofng/34502

    * src/gp-gmon.cc (gen_gmon_map): Get the file offset from the

    filepos field of core_text_sect.'
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpYCtZT3UzHLuhRtq0nCG443bwiygD-cUMtfAKt_HkEGQ@mail.gmail.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

H.J. Lu proposes a patch for gprofng to correctly generate the file offset for gmon.out when creating a map file. The fix involves retrieving the file offset from the `filepos` field of `core_text_sect`, which resolves a failure in the `tmpdir/gp-gmon` test case on Linux/x86-64.
