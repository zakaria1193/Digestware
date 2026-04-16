---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: e27f14be-3499-4d23-a144-ab7a9d192e6f@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 2/5] s390: Remove s390-32 specific code in non s390-32 specific
  files'
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/e27f14be-3499-4d23-a144-ab7a9d192e6f@linaro.org
bugzilla_url: null
date: '2026-04-15'
---



On 09/04/26 05:47, Stefan Liebler wrote:
> This patch removes s390-32 specific code in either common-code files
> or shared files between s390-64 and s390-32.
> 
> Such code was guarded with preproc
