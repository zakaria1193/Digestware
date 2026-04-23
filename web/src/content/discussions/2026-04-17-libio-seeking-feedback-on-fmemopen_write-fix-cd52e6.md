---
project: glibc
subsystem: libio
patch_id: null
tags:
- libio
- fmemopen
- append
- bugfix
discussion_id: CAO_32JoTKeJpUmG+_PiVJGRThrQ0Y2DU+mSDx8iCfxH2w=_5gA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] libio: Fix fmemopen_write on appending condition'
headline: 'libio: Seeking feedback on fmemopen_write fix'
tldr: Rocket Ma is pinging for feedback on a patch to fix `fmemopen_write` in appending
  condition.
stakes: Corrects memory stream handling, potentially preventing unexpected behavior
  when appending with fmemopen.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Under Review
outcome: under_review
sentiment_score: 5
sentiment_rationale: The author is explicitly asking for feedback, indicating uncertainty.
  requests, and returning `EINVAL` if space is insufficient. This approach may limit
  flexibility.
  may introduce inconsistencies if the user sets the buffer manually.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAO_32JoTKeJpUmG+_PiVJGRThrQ0Y2DU+mSDx8iCfxH2w=_5gA@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

Rocket Ma is requesting feedback on version 2 of a patch that aims to fix `fmemopen_write` when used in appending condition. The patch's approach is under discussion, particularly regarding how it handles buffer size and potential inconsistencies with `setbuf`.
