---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- getusershell
- optimization
- memory footprint
- unit test
discussion_id: 20260420130550.3404747-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH] misc: Optimize getusershell.c'
headline: 'misc: Optimize getusershell.c'
tldr: This patch rewrites getusershell.c to improve performance and reduce memory
  footprint by reading the entire file into a single buffer.
stakes: Optimizing getusershell.c can improve the performance of programs that rely
  on it to retrieve valid user shells, such as login and su. Reduced memory footprint
  can also benefit systems with limited resources.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reading the entire file into memory might increase memory usage for very large /etc/shells
  files, but it improves iteration performance.
- The new implementation might introduce subtle bugs if the iteration logic is not
  carefully implemented.
exchanges: []
primer_expert: '`getusershell.c` provides the `getusershell()` and `setusershell()`
  functions, used to iterate through the valid user shells listed in `/etc/shells`.
  This patch aims to improve performance by reducing memory allocations and improving
  the iteration logic. The patch also adds a missing unit test to ensure the functionality
  remains correct. Knowledge of file I/O and string manipulation is helpful to understand
  this patch.'
primer_general: The `getusershell()` function in glibc is used to retrieve a list
  of valid user shells from the `/etc/shells` file.  A user shell is a command interpreter
  that provides a command-line interface for interacting with the operating system.
  This patch proposes to optimize the implementation of `getusershell()` to improve
  its performance and reduce its memory footprint. The new implementation reads the
  entire `/etc/shells` file into memory at once, which allows for faster access to
  the list of valid shells.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260420130550.3404747-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-20'
---

Rocket Ma proposes a complete rewrite of `getusershell.c` to improve performance and reduce memory usage. The new implementation reads the entire file into a single buffer and then iterates to find valid shells.  A missing unit test is added as well.
