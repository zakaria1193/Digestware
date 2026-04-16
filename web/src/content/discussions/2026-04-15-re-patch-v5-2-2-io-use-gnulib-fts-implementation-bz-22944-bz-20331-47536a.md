---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 27c05ce4-c073-4a92-873c-4762a4b12c49@cs.ucla.edu
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
proposer: Paul Eggert <eggert@cs.ucla.edu>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/27c05ce4-c073-4a92-873c-4762a4b12c49@cs.ucla.edu
bugzilla_url: null
date: '2026-04-15'
---

On 2026-04-13 09:15, Collin Funk wrote:
> Also worth noting that if dracut only needs the file type it can
> continue to use FTS_NOSTAT. In the Gnulib implementation
> fts_statp->st_mode will be set t
