---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- versioning
- gdb
commit_hash: cbfea6fd23b78e582df2eb9e5e1c854665a1182f
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: BFD version date automatically updated on gdb-17-branch.
tldr: Updates the BFD version date in `version.h` to the current date on the gdb-17-branch.
why_it_matters: Keeps the version information up to date for the gdb-17-branch.
impact_score: 1
impact_rationale: Cosmetic update of the version date.
performance_win: false
breaking_change: false
outcome: committed
primer: BFD (Binary File Descriptor) is a library for working with different object
  file formats in a uniform way. The version date is a build-time constant for the
  library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260419000023.EBBD54BA9000@sourceware.org
date: '2026-04-19'
---

This commit automatically updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to the current date on the gdb-17-branch.  This macro is used to track the build date of the BFD library.
