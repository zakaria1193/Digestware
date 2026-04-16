---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: DHUQXGOSTCWA.1ZGICJN98HCLA@tum.de
source_type: public_inbox
title: 'Re: [PATCH] rtld: cache cpuid results on the stack for intel'
proposer: Fabian Rast <fabian.rast@tum.de>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/DHUQXGOSTCWA.1ZGICJN98HCLA@tum.de
bugzilla_url: null
date: '2026-04-16'
---

On Thu Apr 16, 2026 at 12:03 PM CEST, Florian Weimer wrote:
> Do AMD CPUs even have P-cores and E-cores?

I messed up the terminology here, sorry.
To be precise, according to AMDs product page [1] the
