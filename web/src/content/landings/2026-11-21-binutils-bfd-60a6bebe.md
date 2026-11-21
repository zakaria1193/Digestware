---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
commit_hash: 60a6bebe22bbb2e1c24c0ba147e7fe21eb003b36
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for main branch
tldr: The Binutils BFD library's version date has been updated for the main development
  branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit bumps the `BFD_VERSION_DATE` in `bfd/version.h` to reflect
  the current date, 20261121, for the main development line of binutils-gdb.
primer_glossary:
- term: BFd
  definition: The Binary File Descriptor library, a low-level library used by binutils
    and GDB to read and write various object file formats.
- term: version date
  definition: A timestamp embedded in library or application code to indicate when
    it was built or released, often used for versioning and tracking.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261121000012.9BF114007E48@sourceware.org
date: '2026-11-21'
is_stub: true
stub_reason: low_score
---

The version date in `bfd/version.h` has been updated from 20261120 to 20261121 for the main binutils-gdb development branch. This is a routine update for tracking release or build dates.
