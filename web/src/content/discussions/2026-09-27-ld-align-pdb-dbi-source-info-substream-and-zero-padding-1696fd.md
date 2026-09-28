---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- pdb
- debugging
- windows
discussion_id: CACcXsZgsfTHQwsBoBp655jzVUpyXSx_0D_jsenvwgH6bRqvS1g@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld: Align the PDB DBI source-info substream'
headline: 'ld: Align PDB DBI source-info substream and zero padding'
tldr: A patch aligning the PDB DBI source-info substream size to a multiple of 4 and
  zeroing padding has been committed.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures adherence to PDB format specifications.
- Minor increase in substream size due to padding, if necessary.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges and approves the patch.
  quote: Okay.
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: proposer
  position: Confirms patch commitment and requests closure of a related bug report.
  quote: 'Thanks for committing the patch. I just found this PR

    https://sourceware.org/bugzilla/show_bug.cgi?id=34605. Can you close

    it? Thanks.'
primer_expert: This is a brief follow-up confirming the commitment of a patch to the
  `ld` component that aligns the PDB DBI source-info substream size to a multiple
  of 4 bytes and zeroes padding, as per the `pdb-rs` documentation. The discussion
  also includes a request to close a related Bugzilla issue.
primer_glossary:
- term: PDB
  definition: Program Database file format, used by Microsoft for storing debugging
    and project information. Used in Windows development.
- term: DBI
  definition: Debug Buffer Interface, a component within PDB files that stores debugging
    information.
- term: source-info substream
  definition: A specific part of the DBI stream within a PDB file that contains information
    about the source code files used to build the program.
- term: alignment padding
  definition: Extra bytes added to data to ensure it starts at a memory address that
    is a multiple of a specific number (e.g., 4 bytes), which can improve performance
    on some architectures.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
series_id: CACcXsZgsfTHQwsBoBp655jzVUpyXSx_0D_jsenvwgH6bRqvS1g@mail.gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CACcXsZgsfTHQwsBoBp655jzVUpyXSx_0D_jsenvwgH6bRqvS1g@mail.gmail.com
bugzilla_url: null
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

This discussion confirms the commitment of a patch that aligns the PDB DBI source-info substream size to a multiple of four bytes and ensures any padding bytes are zeroed. This change adheres to specifications from the Microsoft pdb-rs project. The author thanks Jan Beulich for committing the patch and subsequently requests the closure of a related Bugzilla issue (PR ld/34605).
