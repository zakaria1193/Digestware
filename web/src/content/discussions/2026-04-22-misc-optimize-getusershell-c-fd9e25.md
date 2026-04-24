---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- getusershell
- optimization
- regression
- PLT
discussion_id: 46833eeb-72b9-4756-b750-6ab54355fe7f@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] misc: Optimize getusershell.c'
headline: 'misc: Optimize getusershell.c'
tldr: An optimization patch for `getusershell.c` in glibc caused CI regressions due
  to the use of non-internal function names.
proposer: Adhemerval Zanella Netto
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Reports CI regressions caused by the patch due to the use of non-internal
    functions.
  quote: "This has cause CI regressions [1]:\n\n  elf-check-localplt.out\n  \n  Extra\
    \ PLT reference: libc.so: endusershell\n  Extra PLT reference: libc.so: fread\n\
    \  Extra PLT reference: libc.so: setbuf\n\nThis is due the use of the non-internal\
    \ function names that generated extra\nPLT calls."
primer_expert: This patch modifies `getusershell.c` in glibc, which is responsible
  for providing a list of valid user shells.  The optimization aims to reduce memory
  footprint.  The introduction of non-internal function calls (e.g., `fread`, `setbuf`)
  adds PLT entries, which impacts performance due to increased indirection.
primer_general: The `getusershell` function in glibc retrieves a list of valid user
  shells from the `/etc/shells` file. This file specifies the allowed shell programs
  that users can use. This patch attempts to optimize the function for improved memory
  usage or performance. However, the changes introduced have resulted in regressions
  due to the use of non-internal functions, which can negatively impact performance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/46833eeb-72b9-4756-b750-6ab54355fe7f@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

A patch that rewrites `getusershell.c` to optimize memory footprint and performance has caused CI regressions. Adhemerval Zanella Netto notes that the regressions are due to the use of non-internal function names (`endusershell`, `fread`, `setbuf`), which resulted in extra PLT calls.
