---
project: binutils
subsystem: binutils
patch_id: null
tags:
- documentation
- avr
- gas
- manual
discussion_id: 010e6027-fa3f-4474-997d-15130e366644@gjlay.de
source_type: public_inbox
title: 'Re: [patch, avr] Overhaul section AVR modifiers and document gs()'
headline: Overhaul section AVR modifiers and document gs()
tldr: Updated documentation for AVR modifiers in GAS manual, including gs().
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Updates the AVR documentation in gas/doc/c-avr.texi, focusing on modifiers
  and adding documentation for the `gs()` function, addressing PR gas/13129.
primer_general: This patch updates the documentation for the GNU assembler (GAS) related
  to the AVR microcontroller architecture. It improves the explanation of AVR-specific
  assembly directives and adds information about a function named `gs()`, making the
  manual more comprehensive for developers using AVR.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/010e6027-fa3f-4474-997d-15130e366644@gjlay.de
bugzilla_url: null
date: '2026-06-28'
is_stub: false
stub_reason: ''
---

This is an updated version of a patch that overhauls the "AVR modifiers" section of the GAS manual. It specifically adds documentation for the `gs()` function, which was previously missing. The changes aim to improve the clarity and completeness of the manual.
