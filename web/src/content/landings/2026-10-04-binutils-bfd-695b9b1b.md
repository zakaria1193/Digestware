---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- maintenance
- versioning
commit_hash: 695b9b1b7992c66a63081195c4209e2e0596d1d2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: The BFD version date is updated for the 2.47 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is incremented from
  `20261003` to `20261004` for the `binutils-2_47-branch`.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261004000044.0BA104BA7992@sourceware.org
date: '2026-10-04'
is_stub: true
stub_reason: low_score
---

The `BFD_VERSION_DATE` macro in `bfd/version.h` has been updated to reflect the current date for the binutils-2.47 branch. This is a routine maintenance update for version tracking.
