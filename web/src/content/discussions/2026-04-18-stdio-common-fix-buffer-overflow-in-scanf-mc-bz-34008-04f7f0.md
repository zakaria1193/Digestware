---
project: glibc
subsystem: stdio-common
patch_id: null
tags:
- security
- buffer overflow
- scanf
- glibc
discussion_id: 20260418064841.3299863-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH v6] stdio-common: Fix buffer overflow in scanf %mc [BZ #34008]'
headline: 'Stdio-common: Fix buffer overflow in scanf %mc [BZ #34008]'
tldr: This patch fixes a one-byte buffer overflow in glibc's scanf when using the
  %mc format specifier.
stakes: This patch fixes a user-controlled buffer overflow, which could lead to security
  vulnerabilities (CVE-2026-5450).
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Ready to Land
outcome: ready
sentiment_score: 9
sentiment_rationale: Fixes a security vulnerability and has been reviewed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260418064841.3299863-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-18'
---

A patch has been proposed to fix a buffer overflow in glibc's scanf function. The vulnerability occurs when using the %mc or %mC format specifiers, where the allocated buffer is one byte smaller than required, leading to a potential overflow. The patch includes a fix and a new test case.
