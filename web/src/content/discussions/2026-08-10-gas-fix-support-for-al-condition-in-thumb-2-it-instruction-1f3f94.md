---
project: binutils
subsystem: gas
patch_id: null
tags: []
discussion_id: 20260810215933.1215107-2-calc84maniac@gmail.com
source_type: public_inbox
title: '[PATCH v2] gas: Fix support for AL condition in Thumb-2 IT instruction'
headline: 'gas: Fix support for AL condition in Thumb-2 IT instruction'
tldr: Patch allows unconditional instructions within IT AL blocks in GAS for Thumb-2,
  fixing incorrect rejection.
proposer: Brendan Fletcher <calc84maniac@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Brendan Fletcher
  role: proposer
  position: Proposes a change to allow unconditional instructions within IT AL blocks
    in GAS for Thumb-2.
  quote: 'Using the AL condition in the IT instruction is designed to allow

    encoding unconditional 16-bit instructions which do not affect flags.

    GAS currently allows specifying the AL condition, but rejects any

    following unconditional instructions because they are not considered

    to be part of an IT block.


    This change makes unconditional instructions allowed inside a

    manually-specified IT AL block. Note,…'
- author: Christophe Lyon
  role: reviewer
  position: Approves of the patch but requests additional comments for clarity.
  quote: "It generally looks good, but I'd like to request you to add a few \ncomments,\
    \ see below:"
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260810215933.1215107-2-calc84maniac@gmail.com
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in GAS where unconditional instructions following an IT AL (Always) instruction in Thumb-2 were incorrectly rejected. The change allows these unconditional instructions, as they are designed to not affect flags and can be encoded as 16-bit instructions. It also adds error handling for illegal Else conditions within IT AL blocks.
