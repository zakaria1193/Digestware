---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- release
- version
commit_hash: fd04b6c893204fc99fe3067a8d18dfedbfc6c4d2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: The release date in `bfd/version.h` has been updated.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is automatically incremented
  as part of the release process. This commit reflects that change for the main `binutils-gdb`
  repository.
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
url: https://inbox.sourceware.org/binutils-cvs/20261012000012.E9E7D4BA2E39@sourceware.org
date: '2026-10-12'
is_stub: true
stub_reason: low_score
---

This commit updates the release date in `bfd/version.h` from October 11, 2026, to October 12, 2026, for the main binutils-gdb repository. This is a routine automated update for version tracking.
