---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- misc
- getusershell
- optimization
- memory footprint
discussion_id: 20260420130550.3404747-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH] misc: Optimize getusershell.c'
headline: 'misc: Optimize getusershell.c'
tldr: Rewrites getusershell.c to read the whole file into one buffer, potentially
  reducing memory footprint and improving performance.
stakes: May improve the performance and resource usage of applications that call getusershell.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reading the entire file into memory may consume more memory for very large /etc/shells
  files.
- The new implementation might be faster for most cases, but could be slower if only
  a few shells are needed.
- The change adds complexity but improves maintainability with a new test suite.
exchanges: []
primer_expert: '`getusershell.c` in glibc''s `misc` directory provides functions for
  iterating through valid user shells listed in `/etc/shells`.  The patch replaces
  the original implementation with one that reads the entire file into memory at once,
  aiming to reduce memory allocation overhead. The changes include a new test suite
  (`misc/tst-getusershell.c`) and a data file (`misc/tst-getusershell.shells`)'
primer_general: '`getusershell` is a function in glibc that retrieves a list of valid
  user shells from the `/etc/shells` file.  This file typically contains a list of
  approved command interpreters that users can use as their login shell. This patch
  rewrites the implementation of `getusershell` to improve its efficiency, potentially
  making programs that use this function run faster and use less memory.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420130550.3404747-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-20'
---

Rocket Ma proposes a complete rewrite of `misc/getusershell.c` to optimize its performance. The new implementation reads the entire file into a single buffer and iterates through it. This approach aims to reduce memory footprint and improve performance. A missing unit test is also added.
