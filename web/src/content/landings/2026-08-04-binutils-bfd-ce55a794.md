---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- gdb
commit_hash: ce55a794855b1abb92c665c251d1607a742a30db
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update GDB release date.
tldr: GDB version date updated for the 17 branch release.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the BFD_VERSION_DATE macro in `bfd/version.h` for
  the GDB project's 17 branch. This macro is used to embed the release date into version
  strings and sonames. The update reflects the new release date for this branch.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A library within binutils that provides
    a common interface for reading and writing various object file formats.
- term: Soname
  definition: Shared Object Name. A name embedded in a shared library that indicates
    its compatibility and is used by the dynamic linker to find the correct version
    of the library at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260804000027.66C444BB1C29@sourceware.org
date: '2026-08-04'
is_stub: true
stub_reason: low_score
---

The version date in `bfd/version.h` has been updated to 20260804 for the gdb-17 branch. This is a routine update for release management and does not affect functionality.
