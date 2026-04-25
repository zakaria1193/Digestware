---
project: glibc
subsystem: misc
patch_id: null
tags:
- optimization
- regression
- plt
- symbol visibility
discussion_id: 46833eeb-72b9-4756-b750-6ab54355fe7f@linaro.org
source_type: public_inbox
title: 'Re: [PATCH] misc: Optimize getusershell.c'
headline: 'Misc: Optimize getusershell.c'
tldr: A proposed optimization of getusershell.c is causing CI regressions due to the
  use of non-internal function names.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Needs Revision
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Optimizing for performance may introduce unintended side effects, such as increased
  code size or extra PLT calls.
- Using non-internal function names can lead to increased overhead.
exchanges:
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Reports that the patch causes CI regressions due to the use of non-internal
    function names, leading to extra PLT calls.
  quote: 'This has cause CI regressions [1]: ... Extra PLT reference: libc.so: endusershell
    Extra PLT reference: libc.so: fread Extra PLT reference: libc.so: setbuf'
primer_expert: '`getusershell.c` retrieves valid login shells from `/etc/shells`.  The
  proposal aims to optimize this by reading the entire file into memory. The regression
  is due to the introduction of non-internal symbols, affecting PLT entries. Understanding
  symbol visibility is crucial here.'
primer_general: '`getusershell` is a function that retrieves a list of valid user
  shells from a configuration file.  This patch attempts to optimize the function,
  but it has introduced unintended side effects. It is causing extra overhead during
  program execution due to how the code is using functions and symbols which causes
  a performance regression.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/46833eeb-72b9-4756-b750-6ab54355fe7f@linaro.org
bugzilla_url: null
date: '2026-04-22'
---

The proposed rewrite of `getusershell.c`, which aims to improve performance by reading the entire `/etc/shells` file into memory, is causing CI regressions. Adhemerval Zanella Netto notes that the regressions are due to the use of non-internal function names, which results in extra PLT calls. This issue needs to be resolved before the patch can be considered further.
