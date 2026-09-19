---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- binutils
commit_hash: 9cadb12f6d5c74fa4946f8116b579c81a29fa2bb
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: Updates the BFD version date macro in version.h.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates a hardcoded date in a version header file for the
  BFD library, which is part of the GNU Binutils project. The date is used in version
  strings and sonames during releases.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260919000029.65C424B99F66@sourceware.org
date: '2026-09-19'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h to reflect the current date. This is a routine update for release management.
