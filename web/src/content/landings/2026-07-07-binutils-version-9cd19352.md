---
project: binutils
subsystem: binutils/version
patch_id: null
tags:
- release
- binutils
commit_hash: 9cd19352014eb4b3b75158d2aa14315966258cdb
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for main branch
tldr: The BFD version date in version.h on the main branch is updated to July 7, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the main `binutils-gdb` branch. This is a routine release engineering change
  to advance the date stamp.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils for reading and writing object file formats.
- term: macro
  definition: A predefined identifier in source code that is replaced by its defined
    value during preprocessing. Used here to define the version date.
- term: version.h
  definition: A header file that contains versioning information for the BFD library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260707000011.BFB944BA2E0E@sourceware.org
date: '2026-07-07'
is_stub: true
stub_reason: low_score
---

This commit advances the `BFD_VERSION_DATE` in `bfd/version.h` from `20260706` to `20260707`. This is a standard update for the main development branch to reflect the current date.
