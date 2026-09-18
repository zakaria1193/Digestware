---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- debugging
- PDB
- alignment
discussion_id: 32d4f425-958c-49af-b728-9f9f478a0af8@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Align the PDB DBI source-info substream'
headline: 'ld: Align the PDB DBI source-info substream'
tldr: Align PDB DBI source-info substream to 4 bytes and fix integer type in alignment
  calculation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures proper formatting of PDB debug information.
- Requires adding a reference to specification for the alignment rule.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Requests a reference for the 4-byte alignment requirement and suggests
    omitting a blank line and correcting the integer type in the alignment calculation.
  quote: 'Please can you add a reference here to where this is specified?


    Please omit the blank line between the comment and the new statement.

    (Ftoad the other blank line you add should indeed stay.)


    Oh, and: The ~3u wants to be just ~3, to be correct regardless of

    the type "size" points to.'
- author: Oleg Tolmatcev
  role: contributor
  position: Submitted a patch to round the source-info substream size up to four bytes
    and zero the padding, extending the test.
  quote: 'Round the source-info substream size up to four bytes and zero the

    padding.  Extend the test to exercise this case.'
primer_expert: This change modifies `ld/pdb.c` to ensure that the source-info substream
  within PDB (Program Database) files is 4-byte aligned. This is a common requirement
  for structured debugging information formats to maintain consistency and facilitate
  parsing by debuggers.
primer_glossary:
- term: PDB
  definition: Program Database file format, used by Microsoft Windows for storing
    debugging and type information for executable files.
- term: DBI
  definition: Debug Support Information, a component of the PDB format.
- term: substream
  definition: A distinct section or chunk of data within a larger file format, such
    as PDB.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/32d4f425-958c-49af-b728-9f9f478a0af8@suse.com
bugzilla_url: null
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

Jan Beulich requests a reference for the 4-byte alignment requirement of PDB DBI substreams and suggests code refinements. The proposed changes aim to align the source-info substream and correct the integer type used in the alignment calculation, ensuring proper formatting for debugging information.
