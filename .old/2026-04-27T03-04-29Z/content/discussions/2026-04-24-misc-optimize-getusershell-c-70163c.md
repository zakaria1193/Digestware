---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- getusershell
- optimization
- performance
- unit test
discussion_id: 20260422164926.62177-1-marocketbd@gmail.com
source_type: public_inbox
title: '[PATCH v3] misc: Optimize getusershell.c'
headline: 'misc: Optimize getusershell.c'
tldr: This patch rewrites getusershell.c to improve performance and add a missing
  unit test by reading the whole file into one buffer.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Under Review
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Increased memory usage for the buffer to hold the entire file, but potentially reduced
  overall memory footprint due to fewer allocations.
- Potential performance improvements due to reading the file once instead of multiple
  times.
- Risk of introducing new bugs due to the complete rewrite of the unit.
- The new implementation assumes read-only strings, which might break compatibility
  if users expect to modify the returned values.
exchanges:
- author: Rocket Ma
  role: proposer
  position: Rewrites the `getusershell.c` unit, allocating one big buffer for shell
    names, and adds a missing unit test to improve performance and reduce memory footprint.
  quote: The new implementation read the whole file into one buffer, and wipe out
    every byte but shell names. Later when addressing shell names from first shell,
    jump to next '\0' and then jump to next '/'. This could reduce memory footprint
    and shall improve some performance.
- author: Adhemerval Zanella Netto
  role: reviewer
  position: Provided style and contract comments on the patch.
  quote: The patch seems ok, some minor comments (mostly style issues).
primer_expert: '`getusershell.c` provides functions to iterate through valid user
  shells listed in `/etc/shells`.  This rewrite focuses on reducing memory footprint
  and improving performance by reading the entire file into a single buffer. This
  function is used by login and other system utilities to validate user shells.  The
  primary interaction is with the file system.'
primer_general: '`getusershell` is a function in the C standard library (glibc) that
  retrieves a list of valid login shells from the `/etc/shells` file. This file contains
  a list of approved shells that users can be assigned to. The `getusershell` function
  is used by programs like `login` to ensure that users are only assigned to valid,
  system-approved shells, preventing potential security risks. This patch aims to
  optimize the function''s performance by changing how it reads and stores shell names.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260424172759.212189-1-marocketbd@gmail.com
bugzilla_url: null
date: '2026-04-24'
---

This patch completely rewrites `misc/getusershell.c` to improve performance, reduce memory footprint, and add a missing unit test. The new implementation reads the entire file into a single buffer, extracting shell names by jumping to the next '\0' and then to the next '/'. The patch also addresses reviewer comments regarding API contracts and code style.
