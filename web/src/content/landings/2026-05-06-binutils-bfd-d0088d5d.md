---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- versioning
commit_hash: d0088d5d5ad5b3b7bc02d95699a096073098d844
source_type: public_inbox
author: GDB Administrator
headline: Automatic date update in version.in
tldr: Updates the date in `bfd/version.h` to 20260506.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bfd/version.h` file in the Binary File Descriptor (BFD) library
  contains versioning information, including `BFD_VERSION_DATE`. This commit is a
  routine update to keep the date current.
primer_general: The Binary File Descriptor (BFD) library is a part of the binutils
  project that provides a generic interface for handling different object file formats.
  The `version.h` file contains version information for the BFD library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260506000039.438D74BA23C2@sourceware.org
date: '2026-05-06'
is_stub: true
stub_reason: low-score
---

This commit automatically updates the `BFD_VERSION_DATE` macro in `bfd/version.h` to `20260506`. This date is used internally for versioning and bug reporting.
