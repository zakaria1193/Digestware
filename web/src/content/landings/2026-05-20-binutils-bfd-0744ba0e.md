---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- versioning
- maintenance
commit_hash: 0744ba0e36195a9e6a95e55b9522a90142d65e60
source_type: public_inbox
author: GDB Administrator
headline: 'bfd: Update date in version.in'
tldr: The build date in bfd/version.h has been automatically updated.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`.
  This macro is used to embed the build date into the Binary File Descriptor (BFD)
  library. This is an automated change. BFD is the library providing a common interface
  to various object file formats; it is not exposed as an API to end-users.
primer_general: This commit updates the build date in a version file for the Binary
  File Descriptor (BFD) library. The BFD library is a part of the GNU binutils, and
  it allows programs to work with different types of object files (like executables
  and libraries) in a uniform way. This change is a routine update to keep the version
  information accurate.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260520000038.B47ED4BB5888@sourceware.org
date: '2026-05-20'
is_stub: false
---

The build date in `bfd/version.h` was automatically updated from 20260519 to 20260520. This change is part of the regular maintenance to keep version information current.
