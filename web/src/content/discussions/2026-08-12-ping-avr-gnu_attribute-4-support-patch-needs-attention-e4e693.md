---
project: binutils
subsystem: avr
patch_id: null
tags:
- binutils
- avr
- patch
- review
- attributes
discussion_id: 04fc2779-c173-4b51-b748-eacf6151668a@suse.com
source_type: public_inbox
title: 'Re: [patch, ping] AVR: Add support for .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)'
headline: 'Ping: AVR .gnu_attribute 4 support patch needs attention'
tldr: Follow-up on a patch adding support for AVR .gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS),
  reminding the author to Cc both binutils maintainers.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: under_review
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Reminds the patch author to Cc both binutils maintainers for better visibility
    and review potential.
  quote: Besides Cc-ing one of the two maintainers, perhaps it increases chances (slightly)
    if you also Cc the other one.
primer_expert: This is a follow-up on a patch for the AVR target in binutils that
  adds support for `.gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)`. The sender is nudging
  the author to ensure they have included all relevant maintainers in the CC list
  for the patch, as this is crucial for getting timely reviews and merging in busy
  projects.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel, commonly used in embedded
    systems. Binutils provides toolchain support for them.
- term: .gnu_attribute
  definition: A section in an ELF object file used to store GNU-specific attributes
    about the code or data.
- term: Tag_GNU_AVR_VTABLE_AS
  definition: A specific GNU attribute tag for AVR targets, likely related to virtual
    table support or address space information.
- term: patch
  definition: A piece of code that modifies an existing program, typically to fix
    a bug or add a new feature.
- term: maintainer
  definition: A person responsible for overseeing and approving changes to a specific
    part of a software project.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/04fc2779-c173-4b51-b748-eacf6151668a@suse.com
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This email is a follow-up ping regarding a patch to add support for the `.gnu_attribute 4 (Tag_GNU_AVR_VTABLE_AS)` to the AVR target in binutils. The sender reminds the original author to Cc both of the binutils maintainers, suggesting it might increase the chances of the patch being reviewed.
