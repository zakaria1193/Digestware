---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- gdb
- release
- version
commit_hash: fb99af7b74225d5a66b34034c8e24959392f1821
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update GDB version date
tldr: The release date in `bfd/version.h` has been updated.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: An automated update to `BFD_VERSION_DATE` within `bfd/version.h` for
  the `gdb-18-branch`. This macro is part of the release versioning system and is
  incremented to reflect the current date of the release engineering cycle.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to support reading and writing various executable file formats.
- term: version.h
  definition: A header file containing version information macros for a library or
    tool.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261012000027.9BFC74BA2E39@sourceware.org
date: '2026-10-12'
is_stub: true
stub_reason: low_score
---

This commit automatically updates the release date in `bfd/version.h` for the gdb-18-branch. The date changes from October 11, 2026, to October 12, 2026, as part of the release process.
