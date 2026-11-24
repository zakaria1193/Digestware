---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- xcoff
- debugging
- patch
discussion_id: 20261123172042.2271304-1-harshit7kr@gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] bfd: xcofflink: validate line-number offsets'
headline: 'bfd: xcofflink: validate line-number offsets'
tldr: Gentle ping on v2 of a patch for xcofflink to validate line-number offsets,
  incorporating review feedback and applying cleanly to master.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Gives a gentle ping on a patch (v2) that validates line-number offsets
    in xcofflink, confirming it incorporates review feedback and applies cleanly.
  quote: 'Gentle ping on v2.  It makes the changes from your review of v1:

    linoff is a bfd_size_type in both places, the checks use your forms,

    pass 2 also checks alignment, and the bfd_zmalloc change is gone.  It

    still applies cleanly to master (a2f37c50c7).'
primer_expert: This is a follow-up on a patch for `bfd/xcofflink.c` concerning the
  validation of line number offsets. The patch, in its second version, incorporates
  review comments and ensures that `linoff` uses the correct type (`bfd_size_type`),
  checks are applied as requested, and alignment is validated in pass 2. The author
  is seeking confirmation for the revised patch.
primer_glossary:
- term: bfd
  definition: Binary File Descriptor library; a low-level library used by GNU Binutils
    to abstract the details of various object file formats.
- term: xcofflink
  definition: Part of the binutils library that handles linking for XCOFF (eXtended
    Common Object File Format) files, which is an object file format used on AIX systems.
- term: line-number offsets
  definition: Information stored in object files that maps machine code addresses
    back to source code line numbers, used by debuggers.
- term: bfd_size_type
  definition: A data type within the BFD library used to represent sizes or counts,
    typically an unsigned integer type suitable for file offsets or buffer sizes.
- term: master branch
  definition: The primary line of development in a version control system like Git,
    often representing the latest stable or in-progress version of the codebase.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261123172042.2271304-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

Harshit Kumar is following up on a patch (v2) for the `xcofflink` component within binutils' BFD library, which aims to validate line-number offsets. He confirms that the changes address feedback from a previous review, specifically regarding `linoff` type, check forms, pass 2 alignment checks, and removal of `bfd_zmalloc` changes. The patch is confirmed to apply cleanly to the master branch.
