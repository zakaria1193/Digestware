---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- reproducible builds
- coff
- armap
discussion_id: 02396452-9f30-4de5-be65-8bce20ffd23a@suse.com
source_type: public_inbox
title: 'Re: [PATCH 1/1] BFD: Use SOURCE_DATE_EPOCH for COFF style armaps.'
headline: 'BFD: Use SOURCE_DATE_EPOCH for COFF style armaps'
tldr: Ensures COFF armaps timestamp matches SOURCE_DATE_EPOCH for reproducible builds.
stakes: Ensures archive maps have timestamps matching the source epoch for reproducible
  builds.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensures consistency of timestamps within archives for reproducible builds.
- Relies on the presence and correct setting of the `SOURCE_DATE_EPOCH` environment
  variable.
- Only affects COFF archive maps.
exchanges:
- author: Manuel Jacob <me@manueljacob.de>
  role: proposer
  position: Proposes to use SOURCE_DATE_EPOCH for COFF style armaps to ensure consistency
    in archive creation for reproducible builds.
  quote: Previously, ar created archives where the files have timestamps corresponding
    to SOURCE_DATE_EPOCH (if set), but the armap has a timestamp corresponding to
    the current system time. This change ensures that the armap has a timestamp corresponding
    to SOURCE_DATE_EPOCH as well (if set).
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and approves it.
  quote: Okay.
primer_expert: This patch modifies the binutils `bfd` library to ensure that COFF
  archive maps (armaps) use the `SOURCE_DATE_EPOCH` environment variable for timestamps,
  consistent with file timestamps within the archive. This is relevant for reproducible
  builds. The change affects `bfd/archive.c` (likely indirectly called via `ar`).
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that provides a generic interface for working with different object file formats.
  COFF (Common Object File Format) is a file format used mainly on Windows systems.
  Archive maps (`armaps`) within archives (created by `ar`) are indexes of the archive
  contents. `SOURCE_DATE_EPOCH` is an environment variable used to ensure reproducible
  builds, setting a fixed timestamp for files created during the build process.
series_id: 'binutils:bfd: use source_date_epoch for coff style armaps'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/02396452-9f30-4de5-be65-8bce20ffd23a@suse.com
bugzilla_url: null
date: '2026-04-21'
---

Manuel Jacob proposed a patch to ensure that COFF armaps (archive maps) have timestamps corresponding to the `SOURCE_DATE_EPOCH` environment variable, if set. This ensures consistency in archive creation for reproducible builds. Jan Beulich reviewed and approved the patch.
