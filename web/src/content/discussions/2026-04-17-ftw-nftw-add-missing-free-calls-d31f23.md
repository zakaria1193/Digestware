---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- ftw
- nftw
- readdir
- memory leak
discussion_id: xnqzod439n.fsf@greed.delorie.com
source_type: public_inbox
title: 'Re: [PATCH] io: Fix silent readdir failures in ftw/nftw (BZ 33085)'
headline: 'ftw/nftw: Add missing free() calls'
tldr: Reviewers note that the proposed patch to fix silent readdir failures in ftw/nftw
  needs `free()` calls and has typos.
stakes: Fixes a bug where readdir failures were not properly signaled, potentially
  leading to unexpected behavior.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The review is positive, pointing out necessary improvements.
technical_tradeoffs:
- The patch adds error handling, increasing code complexity slightly.
- Failing to free memory on error can lead to memory leaks, potentially destabilizing
  the application.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/xnqzod439n.fsf@greed.delorie.com
bugzilla_url: null
date: '2026-04-17'
---

DJ Delorie reviews a patch from Adhemerval Zanella that fixes silent readdir failures in ftw/nftw. The review points out missing `free()` calls in the error handling paths and some typos in the test case.
