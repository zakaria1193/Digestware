---
project: binutils
subsystem: c6x
patch_id: null
tags:
- c6x
- binutils
- gas
- unwinding
- cfa_offset
discussion_id: 20251227213101.3502073-1-rbraun@sceen.net
source_type: public_inbox
title: 'Re: [PATCH] c6x: fix unwinding instructions for some values of cfa_offset'
headline: 'c6x: fix unwinding instructions for some values of cfa_offset'
tldr: Corrects a bug in C6000 stack unwinding instructions to handle larger cfa_offset
  values.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 6
technical_tradeoffs:
- Ensures correct stack unwinding for the C6000 architecture.
- Minor code adjustment for accuracy.
exchanges:
- author: Richard Braun
  role: proposer
  position: Proposes a fix for C6000 stack unwinding instructions by adjusting the
    calculation of the cfa_offset.
  quote: "See C6000 EABI (SPRAB89A) Table 21. Stack unwinding instructions.\n\ngas/\n\
    \t* config/tc-tic6x.c (tic6x_output_unwinding): Fix unwinding\n\tbyte value."
- author: Jan Beulich
  role: contributor
  position: Forwards the patch and requests maintainer review.
  quote: 'Cc-ing the maintainer to (hopefully) approve this.


    Joseph,


    would you please take a moment to indicate whether this is okay to go in?'
- author: Joseph Myers
  role: maintainer
  position: Acknowledges the forwarded patch and awaits further review or confirmation.
  quote: null
primer_expert: The c6x target's unwinding mechanism, implemented in `gas/config/tc-tic6x.c`,
  incorrectly calculates byte values for `cfa_offset` when it exceeds 0x40. This patch
  adjusts the calculation to align with the C6000 EABI specification, specifically
  Table 21, ensuring correct dwarf unwinding information generation.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/928a310c-6319-4565-9ad6-cc62c668e2c9@suse.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch series addresses an issue in the C6000 stack unwinding instructions related to the cfa_offset. The original implementation had a bug when handling cfa_offset values greater than 0x40. This change corrects the calculation for such offsets, ensuring proper stack unwinding according to the C6000 EABI.
