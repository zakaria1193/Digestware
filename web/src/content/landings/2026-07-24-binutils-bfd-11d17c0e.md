---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags: []
commit_hash: 11d17c0e1b7084c82174d9d4b6271aba8cb40092
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: Updates the BFD version date in version.h for the 2.47 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Updates the `BFD_VERSION_DATE` macro in `bfd/version.h` from `20260723`
  to `20260724`. This change applies to the `binutils-2_47-branch` and is part of
  the release process where the date is updated to reflect the current release day.
primer_glossary:
- term: BFDMajor
  definition: The source code repository for the Binary File Descriptor library, which
    provides a level of indirection to the various object file formats.
- term: version.h
  definition: A header file that contains version information for the Binutils project,
    including dates and version strings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260724000104.680384BA2E32@sourceware.org
date: '2026-07-24'
is_stub: true
stub_reason: low_score
---

The version date in `bfd/version.h` has been updated from `20260723` to `20260724` for the `binutils-gdb/binutils-2_47-branch`. This is a routine maintenance update for release versioning.
