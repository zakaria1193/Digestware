---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- binutils
commit_hash: 46ba221b3cd6ea6ac483a241630a48f8119ce480
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: Binutils BFD library's version date is updated to reflect the current release.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the BFD_VERSION_DATE macro in the Binutils BFD
  library. This is a routine update for release tagging, ensuring the version string
  reflects the current build date. The change is applied to multiple release branches.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260907000043.B0F324BC054E@sourceware.org
date: '2026-09-07'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h. This change is part of the release process, ensuring that the version information accurately reflects the date of the release. The update is applied across multiple branches of the binutils-gdb repository.
