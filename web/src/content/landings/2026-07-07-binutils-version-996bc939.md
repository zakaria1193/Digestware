---
project: binutils
subsystem: binutils/version
patch_id: null
tags:
- release
- binutils
commit_hash: 996bc939b97e50ae9172f954270eb1ee516d30a5
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for gdb-17 branch
tldr: The BFD version date in version.h is updated to July 7, 2026 for the gdb-17
  branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the `gdb-17-branch`. This is a routine release engineering change to advance
  the date stamp, and it mirrors similar commits on other branches.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils for reading and writing object file formats.
- term: macro
  definition: A predefined identifier in source code that is replaced by its defined
    value during preprocessing. Used here to define the version date.
- term: version.h
  definition: A header file that contains versioning information for the BFD library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260707000025.B45A14BA2E09@sourceware.org
date: '2026-07-07'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to `20260707` for the `gdb-17-branch`. This is a standard update for release engineering to reflect the current day's development.
