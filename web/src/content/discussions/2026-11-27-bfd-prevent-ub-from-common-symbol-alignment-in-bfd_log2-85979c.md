---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- bugfix
- security
- undefined behavior
discussion_id: d21f595f-2b5f-496b-a30f-70248ad7627c@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] bfd: Validate common symbol alignment before bfd_log2 to avoid
  UB [PR binutils/34996]'
headline: 'bfd: Prevent UB from common symbol alignment in bfd_log2'
tldr: A contributor's second version of a patch to binutils' bfd library is rejected
  due to unreadable email formatting and incorrect submission practice; the mainta…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring correct handling of symbol alignment prevents undefined behavior and potential
  security vulnerabilities.
- The submission process and email formatting are critical for effective code review
  and merging.
exchanges:
- author: jelly
  role: proposer
  position: Submitted version 2 of a patch to validate common symbol alignment before
    calling `bfd_log2`, aiming to prevent undefined behavior.
  quote: 'A common symbol (SHN_COMMON) with a very large or non-power-of-two st_value
    can cause bfd_log2 to return 64, which then triggers undefined behaviour when
    used as a shift count: [...] Cap the alignment result of bfd_log2 at 63 [...]
    so 64-bit shifts are safe...'
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Rejected the patch submission due to unreadable formatting and requested
    plain text emails and separate threads for future submissions.
  quote: As you can see your reply is completely unreadable. Please send plain-text
    mails only. And please start a new thread for submitting new versions of a patch.
primer_expert: This thread discusses a patch for the `binutils` BFD library concerning
  common symbols and alignment validation. The core issue is that an excessively large
  `st_value` (symbol value) for a common symbol can lead `bfd_log2` to return an out-of-bounds
  value (64), causing undefined behavior when used as a shift count in subsequent
  calculations. The patch aims to cap this value to prevent such issues. However,
  the discussion is derailed by an unreadable email format, leading to the rejection
  of the patch submission itself, despite the technical merit of the proposed fix.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a part of GNU binutils that provides
    a common interface to read and write various object file formats.
- term: common symbol
  definition: A type of symbol, often used for global variables, that is not allocated
    a specific address until link time. It typically has an alignment requirement.
- term: st_value
  definition: The 'value' field in a symbol table entry, its meaning depends on the
    symbol type. For common symbols, it often represents alignment.
- term: bfd_log2
  definition: A function within the BFD library that computes the base-2 logarithm
    of a number, often used to determine the power of two for alignment.
- term: undefined behavior (UB)
  definition: Behavior produced by a program that violates the C/C++ standards, for
    which the C/C++ standards impose no requirements. The results of UB are unpredictable.
- term: SHN_COMMON
  definition: A special section number used in ELF symbol tables to indicate a common
    symbol.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d21f595f-2b5f-496b-a30f-70248ad7627c@suse.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

A maintainer rejected a resubmitted patch (v2) for binutils' BFD library due to formatting issues in the submission email, which rendered the content unreadable. The maintainer explicitly requested plain-text emails and separate threads for new patch versions. The original patch aimed to prevent undefined behavior in `bfd_log2` by validating common symbol alignment before its use, particularly addressing issues with large or non-power-of-two alignment values.
