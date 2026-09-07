---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- binutils
commit_hash: 7b8c6ea33be8823867c74af0a78ac1c2f5955e9d
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for GDB branch
tldr: Binutils BFD library's version date is updated for the GDB branch release.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the BFD_VERSION_DATE macro in the Binutils BFD
  library for the gdb-18-branch. This is a routine update for release tagging, ensuring
  the version string reflects the current build date.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260907000027.A19414BC054E@sourceware.org
date: '2026-09-07'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h for the binutils-gdb-18-branch. This is a standard update for release tagging, ensuring the version information accurately reflects the current build date. The change is applied to the GDB branch of the binutils-gdb repository.
