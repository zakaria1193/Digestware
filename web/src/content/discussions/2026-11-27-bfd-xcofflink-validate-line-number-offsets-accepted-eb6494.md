---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- xcoff
- linker
- patch
discussion_id: awnvM36dbLHqYm6t@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH v2] bfd: xcofflink: validate line-number offsets'
headline: 'bfd: xcofflink: validate line-number offsets accepted'
tldr: Patch to validate line-number offsets in xcofflink is approved.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: reviewer
  position: Approves the patch after addressing review comments.
  quote: Yes, OK.
- author: Harshit Kumar
  role: proposer
  position: Submitted v2 of the patch, incorporating review feedback.
  quote: 'Gentle ping on v2. It makes the changes from your review of v1: linoff is
    a bfd_size_type in both places, the checks use your forms, pass 2 also checks
    alignment, and the bfd_zmalloc change is gone. It still applies cleanly to master
    (a2f37c50c7).

    Is it OK now?'
primer_expert: This patch addresses a validation issue in the BFD library's xcofflink
  utility, specifically concerning line-number offsets. The revision incorporates
  feedback on data types and alignment checks, suggesting a refinement of the linker's
  internal data handling for XCOFF object files.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils to parse and manipulate object file formats.
- term: xcofflink
  definition: A component within BFD that handles linking for XCOFF (eXecutable and
    Common Object File Format) object files, often used on IBM platforms.
- term: line-number offsets
  definition: Data within object files that maps machine code addresses to source
    code line numbers, used for debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/awnvM36dbLHqYm6t@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

Alan Modra has approved version 2 of the patch that validates line-number offsets within xcofflink. The patch addresses feedback from a previous review, including using the correct data type for offsets and incorporating alignment checks.
