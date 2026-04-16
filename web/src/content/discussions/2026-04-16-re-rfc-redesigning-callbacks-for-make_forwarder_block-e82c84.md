---
project: gcc
subsystem: unknown
patch_id: null
discussion_id: a516d6b5-5111-4408-a732-42de90e92fdd@baylibre.com
source_type: public_inbox
title: 'Re: [RFC] redesigning callbacks for make_forwarder_block'
proposer: Andrew Stubbs <ams@baylibre.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/gcc/a516d6b5-5111-4408-a732-42de90e92fdd@baylibre.com
bugzilla_url: null
date: '2026-04-16'
---

On 15/04/2026 01:44, Andrew Pinski via Gcc wrote:
> Hi all,
>    Right now make_forwarder_block takes two callbacks functions. The
> second one (new_bb_cbk) looks unused; from what I can tell the last
