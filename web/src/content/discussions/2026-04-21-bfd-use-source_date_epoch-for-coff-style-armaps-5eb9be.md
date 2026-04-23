---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- ar
- coff
- reproducible builds
discussion_id: 02396452-9f30-4de5-be65-8bce20ffd23a@suse.com
source_type: public_inbox
title: 'Re: [PATCH 1/1] BFD: Use SOURCE_DATE_EPOCH for COFF style armaps.'
headline: 'BFD: Use SOURCE_DATE_EPOCH for COFF style armaps'
tldr: The patch updates the ar command to use SOURCE_DATE_EPOCH for timestamps in
  COFF armaps, ensuring reproducible builds.
stakes: Ensures that archive maps (armaps) within COFF archives are reproducible,
  contributing to overall build reproducibility.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensuring consistency in timestamping for reproducible builds.
- Potential impact on existing build systems that rely on the old timestamping behavior
  (though unlikely).
exchanges:
- author: Manuel Jacob <me@manueljacob.de>
  role: proposer
  position: Proposes to use SOURCE_DATE_EPOCH for COFF style armaps.
  quote: This change ensures that the armap has a timestamp corresponding to SOURCE_DATE_EPOCH
    as well (if set).
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch.
  quote: Okay.
primer_expert: The Binary File Descriptor (BFD) library is used by binutils to abstract
  access to different object file formats.  COFF (Common Object File Format) is a
  format used on Windows.  `ar` creates archives, and armaps are table-of-contents
  structures within those archives, encoded with COFF conventions. `SOURCE_DATE_EPOCH`
  is an environment variable used to ensure reproducible builds by forcing tools to
  use a specific timestamp instead of the current time.
primer_general: When software is built, timestamps are often embedded in the resulting
  files.  This can make it difficult to reproduce the exact same build output, as
  the timestamps will always be different.  The `SOURCE_DATE_EPOCH` environment variable
  is a standard way to address this, by providing a fixed timestamp to be used during
  the build process. This patch ensures that the `ar` command, which creates archives
  (collections of files), uses this fixed timestamp when creating a table of contents
  inside the archive, improving build reproducibility.
series_id: 'binutils:bfd: use source_date_epoch for coff style armaps'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/02396452-9f30-4de5-be65-8bce20ffd23a@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `ar` command to use the `SOURCE_DATE_EPOCH` environment variable for setting timestamps in COFF-style archive maps (armaps). Previously, the armap had a timestamp corresponding to the current system time, while the files within the archive used the `SOURCE_DATE_EPOCH` if set. This change aligns the armap timestamp with `SOURCE_DATE_EPOCH` to comply with reproducible builds specifications.  Jan Beulich Acked the patch.
