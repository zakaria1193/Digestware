---
project: glibc
subsystem: libio
patch_id: null
tags:
- libio
- streams
- bugfix
- review
discussion_id: 3b0b72f7-7c84-406c-b8ad-b030fe606038@redhat.com
source_type: public_inbox
title: 'Re: [PATCH v2] libio: Fix wrong reference to byte stream'
headline: 'libio: Split patch fixing _IO_wdefault_pbackfail and _IO_wdefault_finish'
tldr: The patch fixing stream pointer dereferencing in libio should be split and include
  a copyright header and test description.
stakes: Fixes potential bugs in wide stream handling, which can lead to incorrect
  program behavior.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Needs Revision
outcome: needs_revision
sentiment_score: 7
sentiment_rationale: Constructive feedback, indicating a need for revision.
  regressions.
  and improves maintainability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/3b0b72f7-7c84-406c-b8ad-b030fe606038@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

Carlos O'Donell requests that Rocket Ma split the patch fixing `_IO_wdefault_pbackfail` and `_IO_wdefault_finish` into separate patches. He also asks for a copyright header and a description of the test case to be added.
