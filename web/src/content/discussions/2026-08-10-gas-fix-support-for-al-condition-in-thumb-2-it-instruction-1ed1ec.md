---
project: binutils
subsystem: gas
patch_id: null
tags: []
discussion_id: 17bd91bb-3649-47d7-8d36-8cf52f39d94a@arm.com
source_type: public_inbox
title: 'Re: [PATCH] gas: Fix support for AL condition in Thumb-2 IT instruction'
headline: 'gas: Fix support for AL condition in Thumb-2 IT instruction'
tldr: Reviewer Christophe Lyon requests additional comments on Brendan Fletcher's
  patch for Thumb-2 IT instruction handling.
proposer: Christophe Lyon <christophe.lyon@arm.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Christophe Lyon
  role: proposer
  position: Requests additional comments on the patch for Thumb-2 IT instruction handling.
  quote: "It generally looks good, but I'd like to request you to add a few \ncomments,\
    \ see below:"
- author: Brendan Fletcher
  role: reviewer
  position: Submitted a patch to fix support for the AL condition in Thumb-2 IT instructions.
  quote: 'Using the AL condition in the IT instruction is designed to allow

    encoding unconditional 16-bit instructions which do not affect flags.

    GAS currently allows specifying the AL condition, but rejects any

    following unconditional instructions because they are not considered

    to be part of an IT block.


    This change makes unconditional instructions allowed inside a

    manually-specified IT AL block. Note,…'
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/17bd91bb-3649-47d7-8d36-8cf52f39d94a@arm.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

Christophe Lyon has reviewed Brendan Fletcher's patch that aims to fix support for the AL condition in Thumb-2 IT instructions within GAS. While the patch is generally well-received, Lyon requests that Fletcher add more comments to the code for better understanding.
