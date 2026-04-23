---
project: glibc
subsystem: stdio-common
patch_id: null
tags:
- security
- stdio
- scanf
- buffer overflow
discussion_id: e48ff256-40b9-4fc4-9898-8bce0e6b4651@redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 0/3] Re: [PATCH v4 2/2] stdio-common: Fix buffer overflow in
  scanf %mc [BZ #34008]'
headline: 'stdio-common: Fix buffer overflow in scanf %mc [BZ #34008]'
tldr: The scanf %mc format specifier had a buffer overflow; upstream requests that
  the fix and its regression test be combined into a single commit.
stakes: Fixes a security vulnerability.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The discussion is focused on code quality and bisectability,
  indicating a positive and constructive environment.
series_id: 'glibc:[patch v4 ] stdio-common: fix buffer overflow in scanf %mc [bz #34008]'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e48ff256-40b9-4fc4-9898-8bce0e6b4651@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

A patch series fixes a buffer overflow in the scanf %mc format specifier. The overflow occurs due to missing size validation when allocating memory.  The patch adds a regression test and fixes the overflow.  The patch author has been asked to combine the fix and the regression test into a single commit for bisectability.
