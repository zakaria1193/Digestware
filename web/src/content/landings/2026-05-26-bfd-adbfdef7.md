---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- versioning
- maintenance
commit_hash: adbfdef7131011d1ec85060128a2467c4f18fe0a
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update date in version.in
tldr: The build date in `bfd/version.h` has been automatically updated to May 26,
  2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The BFD library is part of binutils and provides a generic interface
  to different object file formats. The `version.h` file contains version information,
  including the build date. This commit simply updates the `BFD_VERSION_DATE` macro,
  which is used in the version strings and sonames of the library.
primer_general: The Binary File Descriptor (BFD) library is a part of GNU binutils
  that allows programs to work with different object file formats in a uniform way.
  The `version.h` file stores version information about BFD. This commit automatically
  updates the build date within that file. This kind of update is typically done to
  keep track of when the software was built.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260526000010.F15C34BA23F1@sourceware.org
date: '2026-05-26'
is_stub: false
---

The `BFD_VERSION_DATE` macro in `bfd/version.h` was automatically updated to `20260526`. This change reflects the current date in the version information of the Binary File Descriptor (BFD) library. This update is part of the routine maintenance of the binutils project.
