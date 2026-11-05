---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
commit_hash: 4368eb5c82526aefdd24691ea8f1658096590c98
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Binutils version date updated for 2026-11-05
tldr: The BFD version date in binutils has been updated to 20261105.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Updates the release date macro in `bfd/version.h` as part of a release
  branch maintenance. This is a standard practice for tracking release versions and
  is applied across multiple branches (`binutils-gdb/binutils-2_47-branch`, `binutils-gdb/gdb-18-branch`,
  and the main `binutils-gdb` branch).
primer_glossary:
- term: BFd
  definition: Binary File Descriptor library. It's a core component of GNU Binutils
    that provides an abstraction layer for reading and writing various object file
    formats.
- term: version date
  definition: A macro that stores the date associated with a specific release or build
    of the software, used for version tracking and identification.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261105000026.AAC664BA2E23@sourceware.org
date: '2026-11-05'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` from `20261104` to `20261105`. This is a routine update for the release versioning of the Binutils library.
