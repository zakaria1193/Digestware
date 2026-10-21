---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- binutils
- bfd
commit_hash: c83b914c015a8b324d3926ac81e71a4b31265cb2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'binutils: Update BFD version date'
tldr: Updates the release date stamp in BFD's version header.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the main binutils branch. This macro is part of the versioning information for
  the Binary File Descriptor library and is incremented to reflect the current development
  or release day.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, which handles various object file
    formats.
- term: version.h
  definition: A header file containing version information for a library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261021000013.7D3804BA2E16@sourceware.org
date: '2026-10-21'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in `bfd/version.h` from October 20, 2026, to October 21, 2026. This is a routine update for the main binutils branch to reflect the current date.
