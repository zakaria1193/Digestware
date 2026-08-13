---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
- binutils
commit_hash: 28fe282aac536b210aa7476c0f07bb073df831f2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date to August 13, 2026.
tldr: Binutils version date updated in version.h for main branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  from `20260812` to `20260813` for the main `binutils-gdb` branch.
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
url: https://inbox.sourceware.org/binutils-cvs/20260813000012.6F8E24BA5435@sourceware.org
date: '2026-08-13'
is_stub: true
stub_reason: low_score
---

The BFD library's version date has been updated to 20260813 in the `version.h` file. This commit is for the main `binutils-gdb` branch.
