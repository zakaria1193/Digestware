---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
- binutils
commit_hash: b81be8ba1d2492467f1705ed9db98f334d76e145
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date to August 13, 2026.
tldr: Binutils version date updated in version.h.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is updated as part
  of release maintenance. This commit increments the date from 20260812 to 20260813,
  reflecting the current date for the `binutils-gdb/binutils-2_47-branch` release.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils and GDB to handle various executable file formats.
- term: version.h
  definition: A header file that typically contains versioning information and macros
    for a software project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260813000040.F3AE84BA5435@sourceware.org
date: '2026-08-13'
is_stub: true
stub_reason: low_score
---

The BFD library's version date has been updated to 20260813 in the `version.h` file. This is a routine update for release branching.
