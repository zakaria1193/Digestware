---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- maintenance
- release
- binutils
commit_hash: c8db80abf72784711df8f011d6477ea4207ad7ec
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update release date in version header
tldr: Binutils version header date updated for the new release.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is used to track the
  release date of Binutils. This commit updates the macro from `20260918` to `20260919`,
  reflecting the current date. This change is part of the release tagging process
  and does not affect the functionality or ABI of Binutils.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a backend for Binutils that provides
    a common interface for reading and writing various object file formats.
- term: version header
  definition: A header file that contains version information and macros for a software
    project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260919000045.19DA34B99F66@sourceware.org
date: '2026-09-19'
is_stub: true
stub_reason: low_score
---

The release date in the Binutils version header file (`bfd/version.h`) has been automatically updated from 20260918 to 20260919. This is a routine maintenance update for tracking release information.
