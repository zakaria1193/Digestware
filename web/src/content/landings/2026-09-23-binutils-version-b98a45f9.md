---
project: binutils
subsystem: binutils/version
patch_id: null
tags:
- binutils
- gdb
- release
- versioning
commit_hash: b98a45f9f9630c43cc7872f34a90d42d2e82b0c3
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'binutils: Update BFD_VERSION_DATE for GDB 18 branch'
tldr: Updates the version date in bfd/version.h for the GDB 18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is updated to `20260923`
  from `20260922`. This is part of the release process for the GDB 18 branch, ensuring
  that the versioning information embedded within the library reflects the latest
  build date.
primer_glossary:
- term: BFD_VERSION_DATE
  definition: A preprocessor macro in the Binary File Descriptor (BFD) library that
    defines the date associated with a specific version of the library.
- term: gdb-18-branch
  definition: A specific development branch for the GNU Debugger (GDB) project, corresponding
    to version 18.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260923000028.0C6554BB1C1C@sourceware.org
date: '2026-09-23'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to reflect the current date. This is a routine update for the `gdb-18-branch` to ensure version information is accurate.
