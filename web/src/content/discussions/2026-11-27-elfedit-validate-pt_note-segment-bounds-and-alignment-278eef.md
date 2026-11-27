---
project: binutils
subsystem: elfedit
patch_id: null
tags:
- binutils
- elfedit
- security
- validation
- elf
discussion_id: 3879d396-b67b-4bcc-b6d8-d9bff813f484@suse.com
source_type: public_inbox
title: 'Re: [PATCH] elfedit: validate PT_NOTE bounds and alignment'
headline: 'elfedit: Validate PT_NOTE segment bounds and alignment'
tldr: Reviewer suggests improvements to a patch that validates PT_NOTE segments in
  elfedit, specifically regarding alignment handling and ChangeLog formatting.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enhances security by preventing memory corruption through stricter validation of
  ELF note segments.
- Requires careful handling of alignment values to maintain correctness and avoid
  division-by-zero issues.
exchanges:
- author: mustafa
  role: proposer
  position: Submitted a patch to `elfedit` to validate `PT_NOTE` segment bounds and
    alignment, preventing crashes and potential corruption.
  quote: 'The program header table is checked against the file size, but the PT_NOTE
    segments themselves are not: p_offset and p_filesz are used as they are to compute
    "map + p_offset", so a note segment that points outside the file makes elfedit
    read and write past the end of the mapping. A crafted binary crashes it with SIGSEGV.


    Other fields in the same loop are also trusted: [...] p_align of 0 gives a…'
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Provided feedback on the patch, suggesting improvements to alignment handling
    and ChangeLog formatting, while agreeing with the necessity of the validation.
  quote: 'I fear what readelf does cannot be directly mirrored here, where we actually
    alter the file (but we don''t want to corrupt it). See also below.


    Nit: There''s a


    binutils/


    line missing ahead of the ChangeLog entry. Also the contents aren''t really

    ChangeLog-like; it rather repeats the patch description.'
primer_expert: 'This discussion revolves around security enhancements for `elfedit`,
  a tool for editing ELF files. The patch focuses on validating `PT_NOTE` (program
  segment notes) entries. It addresses two primary concerns: first, ensuring that
  the offset and file size of `PT_NOTE` segments do not point outside the file''s
  mapped region to prevent buffer overflows; second, normalizing and validating the
  `p_align` (alignment) field to avoid division-by-zero errors and ensure correct
  calculations. The reviewer also provides feedback on the code changes and commit
  message style.'
primer_glossary:
- term: elfedit
  definition: A tool for editing ELF (Executable and Linkable Format) files.
- term: PT_NOTE
  definition: A type of program header segment in an ELF file that contains arbitrary
    data, often used for versioning or other metadata.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: p_offset
  definition: The offset of the segment in the file.
- term: p_filesz
  definition: The size of the segment in the file.
- term: p_align
  definition: The alignment requirement of the segment.
- term: ChangeLog
  definition: A file that records changes made to a software project over time, typically
    organized by date and description of modifications.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/3879d396-b67b-4bcc-b6d8-d9bff813f484@suse.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

A reviewer discussed a patch for `elfedit` that aims to validate the bounds and alignment of `PT_NOTE` segments within ELF files. The original patch fixed issues where `elfedit` could read or write past file mappings due to unchecked `p_offset` and `p_filesz`, and also addressed division-by-zero and infinite loops caused by invalid `p_align` values. The reviewer agreed with the core fixes but suggested refining the alignment normalization logic and improving the ChangeLog entry's format, noting it repeated the patch description.
