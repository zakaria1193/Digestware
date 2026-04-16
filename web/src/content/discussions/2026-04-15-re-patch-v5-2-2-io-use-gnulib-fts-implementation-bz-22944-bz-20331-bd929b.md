---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: efc34c0d-10ca-4720-8089-1ff95d73c5a4@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/efc34c0d-10ca-4720-8089-1ff95d73c5a4@linaro.org
bugzilla_url: null
date: '2026-04-15'
---



On 13/04/26 12:53, Paul Eggert wrote:
> On 2026-04-11 10:06, Florian Weimer wrote:
>> I think we need to version the symbol, with an internal flag that
>> does more stat'ing with FTS_NOSTAT.
> 
> Oh
