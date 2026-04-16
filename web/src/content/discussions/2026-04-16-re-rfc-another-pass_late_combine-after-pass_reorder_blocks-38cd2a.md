---
project: gcc
subsystem: unknown
patch_id: null
discussion_id: qp0225n0-4169-1259-08qr-q7n6s0oqq6po@fhfr.qr
source_type: public_inbox
title: 'Re: RFC: Another pass_late_combine after pass_reorder_blocks?'
proposer: Richard Biener <rguenther@suse.de>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/gcc/qp0225n0-4169-1259-08qr-q7n6s0oqq6po@fhfr.qr
bugzilla_url: null
date: '2026-04-16'
---

On Thu, 16 Apr 2026, Uros Bizjak wrote:

> Hello!
> 
> After pass_reorder_blocks, there remain some propagating opportunities
> for late_combine.  Looking at gcc.target/i386/pr90178.c, we get a
> triv
