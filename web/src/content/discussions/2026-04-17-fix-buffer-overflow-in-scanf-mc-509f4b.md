---
project: glibc
subsystem: stdio-common
patch_id: null
tags:
- stdio
- scanf
- vfscanf
- buffer overflow
- security
discussion_id: 68917648-fed6-45a2-a1ff-8f5b978b1353@redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/3] stdio-common: Fix buffer overflow in scanf %mc [BZ #34008]'
headline: Fix buffer overflow in scanf %mc
tldr: This patch fixes a buffer overflow vulnerability in scanf's %mc format specifier,
  identified as CVE-2026-5450.
stakes: Fixes a security vulnerability that could allow user-controlled buffer overflows
  when using the %mc format specifier in scanf.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Ready to Land
outcome: ready
sentiment_score: 9
sentiment_rationale: Fixes a security vulnerability and has been reviewed.
technical_tradeoffs:
- Modifies the buffer resizing logic in `vfscanf-internal.c`.
series_id: 'glibc:stdio-common: fix buffer overflow in scanf %mc [bz #34008]'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/68917648-fed6-45a2-a1ff-8f5b978b1353@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

This patch corrects a buffer overflow in `vfscanf-internal.c` related to the `%mc` and `%mC` format specifiers.  The issue occurs during buffer enlargement, where one byte less than required is allocated.  The patch has been reviewed and the reviewer's approval can be kept for v6 if the fix remains unchanged.
