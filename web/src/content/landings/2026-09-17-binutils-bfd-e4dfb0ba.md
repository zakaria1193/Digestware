---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
- gdb
commit_hash: e4dfb0ba45ef80c53df01083eb68e4ea18d9f855
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for GDB branch
tldr: Updates the BFD version date in version.h for the GDB 18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates the compile-time date stamp in BFD's versioning
  header, specifically for the GDB 18 development branch. The BFD_VERSION_DATE macro
  is used to embed a release date into version strings and sonames, and this update
  reflects the current date for that branch's release cycle.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260917000029.D54394BA23FB@sourceware.org
date: '2026-09-17'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h from 20260916 to 20260917. This is part of the routine release preparation for the GDB 18 branch, ensuring accurate versioning information.
