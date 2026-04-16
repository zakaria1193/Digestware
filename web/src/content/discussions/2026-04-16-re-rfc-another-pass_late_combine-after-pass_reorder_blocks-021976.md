---
project: gcc
subsystem: unknown
patch_id: null
discussion_id: aeDBXwFw5HnhP77F@tucnak
source_type: public_inbox
title: 'Re: RFC: Another pass_late_combine after pass_reorder_blocks?'
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/gcc/aeDBXwFw5HnhP77F@tucnak
bugzilla_url: null
date: '2026-04-16'
---

On Thu, Apr 16, 2026 at 12:58:09PM +0200, Richard Biener wrote:
> > Any thoughts?
> 
> Did you check other places to schedule the pass?  Did you try
> moving the existing postreload late_combine later
