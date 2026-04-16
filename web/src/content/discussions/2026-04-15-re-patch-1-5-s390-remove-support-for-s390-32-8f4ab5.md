---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: cf830cd6-924c-4c65-83b2-003f50700385@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 1/5] s390: Remove support for s390-32.'
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/cf830cd6-924c-4c65-83b2-003f50700385@linaro.org
bugzilla_url: null
date: '2026-04-15'
---



On 09/04/26 05:47, Stefan Liebler wrote:
> The linux 6.19 release has removed support for compat syscalls on s390x.
> Therefore s390-linux-gnu (31bit) configuration was deprecated with glibc 2.43:
>
