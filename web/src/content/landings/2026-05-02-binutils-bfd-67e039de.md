---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- build
- maintenance
commit_hash: 67e039de0fbcddf62e4d8a9440f26143ecbf5d24
source_type: public_inbox
author: GDB Administrator
headline: Update date in version.in
tldr: The build date has been updated in `bfd/version.h`.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is used to track the
  build date. It is updated automatically.  This commit does not change any functional
  code.
primer_general: The build date in the `version.h` file has been updated. This is a
  standard part of the build process and doesn't change how the software works.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260502000043.CAB5C4371D6F@sourceware.org
date: '2026-05-02'
is_stub: true
stub_reason: low-score
---

The `BFD_VERSION_DATE` macro in `bfd/version.h` was automatically updated to `20260502`. This change is part of the regular maintenance of the build system. It does not affect functionality.
