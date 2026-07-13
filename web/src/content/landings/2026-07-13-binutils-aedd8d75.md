---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- release
- versioning
commit_hash: aedd8d75177e35fe94a1b462869da373a839bd32
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'binutils: Update release date in version.h'
tldr: Release date in binutils version information updated for July 13, 2026.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the BFD_VERSION_DATE macro in `bfd/version.h`.
  This macro is used to embed the release date into the binary's version information.
  The update affects builds branched from binutils-gdb/binutils-2_46-branch, binutils-gdb/gdb-17-branch,
  and the main binutils-gdb repository.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    that provides an abstraction for handling various object file formats.
- term: version.h
  definition: A header file containing version information macros for the Binutils
    project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260713000011.4C7664BA5436@sourceware.org
date: '2026-07-13'
is_stub: true
stub_reason: low_score
---

The BFD library's version file has been updated to reflect the current release date of July 13, 2026. This is a routine update for version tracking and does not affect functionality.
