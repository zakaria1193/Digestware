---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- getusershell
- optimization
discussion_id: 70a7356a-43a5-41d2-af1b-c03a822b7b90@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] misc: Optimize getusershell.c'
headline: 'misc: Optimize getusershell.c'
tldr: The patch seems ok with minor style comments
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
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
  position: The patch seems ok, some minor comments (mostly style issues).
  quote: The patch seems ok, some minor comments (mostly style issues).
primer_expert: The `getusershell` family of functions parses `/etc/shells`. The patch
  in question rewrites the function to improve performance. Reviewers outside of glibc
  might not be aware of internal glibc coding styles and best practices.
primer_general: '`getusershell` is a function used to retrieve valid user shells from
  a file, typically `/etc/shells`. This file lists the approved shells for user accounts
  on a system. The patch aims to improve the efficiency of this function. Understanding
  this requires knowing that `getusershell` is part of the standard C library and
  is used for security and system administration purposes.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/70a7356a-43a5-41d2-af1b-c03a822b7b90@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

Adhemerval reviewed Rocket Ma's patch to optimize getusershell.c and provided minor style comments.
