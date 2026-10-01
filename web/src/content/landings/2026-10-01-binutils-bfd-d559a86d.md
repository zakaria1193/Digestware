---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- BFD
- versioning
- release
commit_hash: d559a86dcdbb2b0e6fc375624e3025b8d516b8b2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'binutils: Update BFD version date'
tldr: Updates the BFD version date to October 1, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the `binutils-gdb/binutils-2_47-branch`. The date is advanced from `20260930`
  to `20261001`. This is a routine update for release branches to track the current
  build date, separate from the version string itself.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a part of GNU binutils that provides
    a common interface for handling various executable and object file formats.
- term: macro
  definition: A fragment of code that represents a longer, predefined piece of code.
    Macros are typically used for code substitution.
- term: version string
  definition: A string that identifies a specific release of a software project, often
    including version numbers and sometimes dates or build information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261001000047.663314BB58B0@sourceware.org
date: '2026-10-01'
is_stub: true
stub_reason: low_score
---

The version control file for the BFD library within binutils has been updated to reflect the current date. The `BFD_VERSION_DATE` macro in `bfd/version.h` has been changed from September 30, 2026, to October 1, 2026.
