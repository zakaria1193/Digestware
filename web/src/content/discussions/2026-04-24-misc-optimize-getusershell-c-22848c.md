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
discussion_id: 70a7356a-43a5-41d2-af1b-c03a822b7b90@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] misc: Optimize getusershell.c'
headline: 'Misc: Optimize getusershell.c'
tldr: Adhemerval Zanella Netto reviews Rocket Ma's patch to optimize getusershell.c
  and provides minor style comments.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Reduced memory footprint vs. increased complexity in iterating through shell names.
- Single large buffer allocation vs. multiple smaller allocations.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: reviewer
  position: Finds the patch OK but requests some style changes.
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
url: https://inbox.sourceware.org/libc-alpha/70a7356a-43a5-41d2-af1b-c03a822b7b90@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

Adhemerval Zanella Netto reviewed Rocket Ma's patch which rewrites `getusershell.c` to allocate a single large buffer instead of multiple smaller ones, aiming to reduce memory footprint and improve performance. Adhemerval finds the patch to be generally OK, and offers style suggestions.
