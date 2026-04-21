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
tldr: The patch optimizes `getusershell.c` by reading the whole file into one buffer,
  potentially reducing memory footprint and improving performance.
stakes: Optimizing `getusershell` can improve the performance of programs that rely
  on it to determine valid user shells.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reading the entire file into memory might be less efficient for very large `/etc/shells`
  files, but likely improves performance for typical use cases.
- The new implementation may be more complex to maintain than the original.
exchanges: []
primer_expert: '`getusershell.c` in glibc''s `misc` directory provides functions to
  iterate through valid user shells listed in `/etc/shells`.  The patch aims to optimize
  this by changing the memory allocation strategy. Toolchain developers outside the
  immediate glibc team likely haven''t touched this file, despite its integration
  role.'
primer_general: '`getusershell` is a function used to retrieve a list of valid user
  shells from the `/etc/shells` file. This file contains a list of acceptable login
  shells for a system. The `getusershell` function is used by programs like `login`
  and `chsh` to validate user-specified shells. This patch optimizes the implementation
  of `getusershell` to improve its efficiency and reduce memory usage, which can benefit
  any program that uses this function.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420130550.3404747-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch rewrites the `getusershell.c` function to improve its performance and reduce memory usage. The new implementation reads the entire `/etc/shells` file into a single buffer, then parses the buffer in place. A new unit test is also added.
