---
project: glibc
subsystem: misc
patch_id: null
tags:
- memory footprint
- performance
- getusershell
- glibc
- shells
discussion_id: 20260422164926.62177-1-marocketbd@gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] misc: Optimize getusershell.c'
headline: 'Misc: Optimize getusershell.c'
tldr: Rewrites getusershell.c to reduce memory footprint by using a single large buffer.
proposer: Rocket Ma <marocketbd@gmail.com>
consensus: Proposed
outcome: ready
sentiment_score: 7
technical_tradeoffs:
- Reduced memory footprint vs. increased complexity in iterating through shell names.
- Single large buffer allocation vs. multiple smaller allocations.
exchanges:
- author: Rocket Ma <marocketbd@gmail.com>
  role: proposer
  position: Proposes rewriting the unit to allocate one big buffer to store shell
    names, to reduce memory footprint and improve performance.
  quote: The new implementation read the whole file into one buffer, and wipe out
    every byte but shell names. Later when addressing shell names from first shell,
    jump to next '\0' and then jump to next '/'. This could reduce memory footprint
    and shall improve some performance.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: reviewer
  position: Says the patch seems ok, with some minor style comments.
  quote: The patch seems ok, some minor comments (mostly style issues).
primer_expert: '`getusershell.c` provides `getusershell()`, `setusershell()`, and
  `endusershell()` which are used to iterate through valid login shells listed in
  `/etc/shells`.  The original implementation allocated a file-size buffer to store
  strings and (file size / 3 * 8) to store pointers. The patch replaces this with
  a single large buffer.'
primer_general: '`getusershell` is a function in glibc that iterates through the valid
  shells listed in the `/etc/shells` file.  This file determines the list of approved
  shells that a user can be assigned to on a Unix-like system. This patch optimizes
  the memory allocation strategy of `getusershell` to improve performance.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAO_32JqiqAgQ-+FCDg-ChrfRSncnroyZC9RqWeztVd7gzeQOxQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-23'
---

Rocket Ma proposes rewriting `getusershell.c` to allocate a single large buffer instead of multiple smaller ones, aiming to reduce memory footprint and improve performance. The new implementation reads the entire file into a single buffer, then iterates through it. A new unit test is added. Adhemerval Zanella Netto has reviewed the patch and provided minor style comments.
