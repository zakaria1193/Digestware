---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- build
- versioning
commit_hash: 5dc4b683e18c44c38e965bcc7003c83952a9e71d
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Automatic date update in version.in
tldr: The build date in bfd/version.h has been automatically updated.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '``bfd/version.h`` contains version and date information for the Binary
  File Descriptor library. This commit updates the ``BFD_VERSION_DATE`` macro.'
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that provides a generic interface for working with different object file formats.
  This commit updates the date in the BFD version information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260525000036.CCB184B9DB75@sourceware.org
date: '2026-05-25'
is_stub: true
stub_reason: low-score
---

The build date in `bfd/version.h` was automatically updated from 20260524 to 20260525. This is a routine update for the branch.
