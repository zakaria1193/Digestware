---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- optimization
- getusershell
- security
discussion_id: 20260420130550.3404747-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH] misc: Optimize getusershell.c'
headline: 'Misc: Optimize getusershell.c'
tldr: This patch optimizes `getusershell.c` by reading the entire file into one buffer,
  reducing memory footprint and improving performance.
stakes: Improved performance for applications that frequently call `getusershell`,
  such as login programs and shells.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The new implementation might have different performance characteristics in edge
  cases.
- Reading the entire file into memory could be a concern for extremely large /etc/shells
  files, though this is unlikely in practice.
primer: '`getusershell` is a glibc function that returns a valid shell from the `/etc/shells`
  file.  The `/etc/shells` file contains a list of approved login shells on a system.  Optimizing
  `getusershell` can improve the performance of programs that rely on it to validate
  or retrieve shell paths, especially in environments with frequent user logins or
  shell executions.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420130550.3404747-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-20'
---

The patch rewrites `getusershell.c` to read the entire file of valid shells into a single buffer, replacing the previous implementation. It adds a missing unit test and aims to reduce memory footprint and improve performance by minimizing memory allocations and jumping to the next shell name. The updated implementation wipes out every byte but shell names, then jumps to the next '\0' and then to the next '/'.
