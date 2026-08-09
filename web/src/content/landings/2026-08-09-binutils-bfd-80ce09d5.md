---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
- versioning
commit_hash: 80ce09d5cacff8eedb0ec3c8fb7b8acbc6a8331e
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date.
tldr: The BFD version date in version.h is updated to August 9, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bfd/version.h` file contains versioning information for the BFD
  library. This commit updates the `BFD_VERSION_DATE` macro, which is used to track
  releases. The change is applied to the `2_47-branch` of binutils-gdb.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level module in the GNU Binutils
    project that provides a standardized interface for reading and writing object
    file formats.
- term: macro
  definition: A preprocessor directive in C/C++ that defines a symbolic name or a
    piece of code that is substituted at compile time. `BFD_VERSION_DATE` is a macro
    used for versioning.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260809000042.07F094BA79A3@sourceware.org
date: '2026-08-09'
is_stub: true
stub_reason: low_score
---

The BFD library's version information has been updated. The `BFD_VERSION_DATE` macro in `bfd/version.h` is now set to `20260809`, reflecting the current date. This is a routine update for version tracking.
