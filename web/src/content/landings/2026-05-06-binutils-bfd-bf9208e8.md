---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- versioning
commit_hash: bf9208e8cf468aae6dda331112bdc24ad72ddb80
source_type: public_inbox
author: GDB Administrator
headline: Automatic date update in version.in
tldr: Updates the date in `bfd/version.h` to 20260506 on the gdb-17-branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: As in the trunk, the `bfd/version.h` file in the Binary File Descriptor
  (BFD) library's `gdb-17-branch` requires a date update to `BFD_VERSION_DATE`. This
  change mirrors the one on the trunk.
primer_general: The Binary File Descriptor (BFD) library is a part of the binutils
  project, offering a generic interface for handling various object file formats.
  The `version.h` file maintains version information, specific to the `gdb-17` branch.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260506000026.277F64BA799F@sourceware.org
date: '2026-05-06'
---

This commit updates the `BFD_VERSION_DATE` macro within `bfd/version.h` to `20260506` on the `gdb-17-branch`. This macro is used for internal version tracking and bug reporting.
