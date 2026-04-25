---
project: glibc
subsystem: misc
patch_id: null
tags:
- memory
- optimization
- concurrency
- BSD
- regression
discussion_id: 20260422164926.62177-1-marocketbd@gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] misc: Optimize getusershell.c'
headline: 'Misc: Optimize getusershell.c'
tldr: A proposed rewrite of getusershell.c to read the entire /etc/shells file into
  memory is being challenged due to potential memory and concurrency issues.
proposer: Collin Funk <collin.funk1@gmail.com>
consensus: NACK'd
outcome: proposed
sentiment_score: 3
technical_tradeoffs:
- Reading the entire file into memory may improve performance for small files but
  degrades performance and memory usage for large files.
- The proposed change alters the behavior of getusershell, making it different from
  BSD versions.
- Reading the file into memory introduces a potential concurrency issue if the /etc/shells
  file is modified while the function is running, preventing dynamically updated shells
  from being valid.
exchanges:
- author: Collin Funk <collin.funk1@gmail.com>
  role: reviewer
  position: Objects to reading the entire `/etc/shells` file into memory due to potential
    size issues and behavioral differences from BSD versions. Raises concerns about
    concurrency issues if the file is modified while the function is running.
  quote: However, I am against this change. The /etc/shells file can be arbitrarily
    long, so we shouldn't read it all into memory. It also changes the behavior of
    the function to be different to all the BSD versions.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Notes that the patch introduces extra PLT calls, causing CI regressions.
  quote: null
- author: Rocket Ma <marocketbd@gmail.com>
  role: proposer
  position: Acknowledges the concerns and apologizes for the noise, stating that they
    confused the glibc version with a Gnulib version.
  quote: Ah, thanks to you and Rocket for pointing out my mistake. I think I was mixing
    up the one in glibc and the one I wrote for Gnulib to work around some issues.
    Sorry for the extra noise.
primer_expert: '`getusershell.c` retrieves valid login shells from `/etc/shells`.
  The proposal replaces the traditional line-by-line parsing with reading the whole
  file at once. This touches `_PATH_SHELLS` and stdio functions. A toolchain dev might
  not immediately know about the non- BSD behavior change.'
primer_general: '`getusershell` is a function in glibc that retrieves a list of valid
  user shells from the `/etc/shells` file. This file specifies the legitimate shells
  available on a system. Rather than parsing the file line by line, the patch proposes
  to read the entire file into memory. This approach could lead to memory allocation
  issues if `/etc/shells` becomes very large, and could have concurrency implications
  if it''s modified while being read.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/874il3lyig.fsf@gmail.com
bugzilla_url: null
date: '2026-04-22'
---

Rocket Ma proposed rewriting `getusershell.c` to read the entire `/etc/shells` file into memory for performance and reduced memory footprint. Collin Funk objects, citing concerns about arbitrarily long files, behavior differences from BSD versions, and potential concurrency issues if the file is modified during the function's execution. The patch also introduces extra PLT calls, causing CI regressions.
