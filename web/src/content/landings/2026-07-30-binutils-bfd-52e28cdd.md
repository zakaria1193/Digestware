---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
commit_hash: 52e28cdd62873a2e0285177f3854bd1d0050bc5f
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'Binutils: Update version date for binutils-gdb/binutils-2_47-branch'
tldr: The version date in `bfd/version.h` is updated for the binutils-2_47 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is updated from `20260729`
  to `20260730`. This is a routine update for the `binutils-2_47-branch` to reflect
  the current build or release date in the versioning information.
primer_glossary:
- term: BFD_VERSION_DATE
  definition: A preprocessor macro defined in `bfd/version.h` that holds the date
    associated with a particular release or build of the Binutils BFD library. It's
    used for version tracking.
- term: macro
  definition: A fragment of code defined by a preprocessor directive, typically used
    to substitute a name for a token sequence. Macros are expanded before compilation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260730000040.C76904BB5912@sourceware.org
date: '2026-07-30'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to reflect the current date. This change is part of the regular maintenance for the binutils-2_47 branch, ensuring version information is up-to-date.
