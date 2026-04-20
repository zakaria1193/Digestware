---
project: glibc
subsystem: libio
patch_id: null
tags:
- glibc
- libio
- security
- vulnerability
- ungetwc
discussion_id: 20260418101742.3355742-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH v4] libio: Fix ungetwc operating on byte stream [BZ #33998]'
headline: Fixes potential information leak in libio ungetwc
tldr: This patch fixes a potential information leak in `libio`'s `ungetwc` function
  when operating on byte streams, addressing CVE-2026-5928.
stakes: Fixes a security vulnerability where an attacker could potentially leak information.
  Addresses CVE-2026-5928.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: Addresses a security concern and includes a test case.
technical_tradeoffs:
- Minor code change to fix the bug.
- Addition of a new test case.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260418101742.3355742-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-18'
---

A vulnerability exists in `libio/wgenops.c` where `_IO_wdefault_pbackfail` incorrectly compares a wchar to push back with the last char from the byte stream. This patch corrects the comparison and adds a regression test (`libio/bug-wgenops-bz33998.c`) to prevent future regressions. The patch resolves bug 33998 and has been assigned CVE-2026-5928.
