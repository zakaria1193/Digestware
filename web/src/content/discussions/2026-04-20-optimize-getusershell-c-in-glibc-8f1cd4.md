---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- optimization
- memory
- performance
- shell
discussion_id: 20260420130550.3404747-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH] misc: Optimize getusershell.c'
headline: Optimize getusershell.c in glibc
tldr: This patch optimizes the `getusershell.c` function in glibc by reducing memory
  footprint and improving performance.
stakes: Potentially improves the performance and resource usage of applications that
  rely on `getusershell`.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The new implementation reads the entire file into memory, which might be a concern
  for very large shell files.
- The patch improves performance by reducing the number of system calls and memory
  allocations.
primer_expert: '`getusershell.c` is a utility function in glibc''s `misc/` directory
  that retrieves valid user shells from a file. This patch replaces the implementation
  to reduce memory footprint. The patch introduces a new unit test (`tst-getusershell.c`)
  and a data file (`tst-getusershell.shells`) for testing the function.'
primer_general: The `getusershell` function, part of the GNU C Library (glibc), retrieves
  a list of valid user shells from a system file (typically `/etc/shells`).  This
  function is used by programs like `login` to determine which shells are allowed
  for users.  This patch optimizes the function's implementation to reduce memory
  usage and improve performance, which can benefit applications that rely on this
  function.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420130550.3404747-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch rewrites the `getusershell.c` function in glibc to optimize memory usage and improve performance. The new implementation reads the entire file into a single buffer, marking shell names and jumping to the next shell. It also adds a missing unit test.
