---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: d4d7dfc2-3047-4d6e-a652-9de07025dfa1@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 3/5] s390: Switch to common-code headers'
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/d4d7dfc2-3047-4d6e-a652-9de07025dfa1@linaro.org
bugzilla_url: null
date: '2026-04-15'
---



On 09/04/26 05:47, Stefan Liebler wrote:
> The removal of s390-32 allows us to switch to common-code headers
> instead of providing s390-64 specific headers:
> 
> from sysdeps/unix/sysv/linux/s390/b
