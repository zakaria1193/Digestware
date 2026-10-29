---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- maintenance
commit_hash: dcc9b44ad55b998573dac76f249c921ddd50b593
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update release date in version header for gdb-18 branch
tldr: Updates the BFD version date from 20261028 to 20261029 in version.h for the
  gdb-18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the `gdb-18-branch`. This is a standard maintenance activity to reflect the
  current date in the versioning information for the BFD library.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to parse and manipulate various object file formats.
- term: version.h
  definition: A header file that contains macros defining the version information
    for the Binutils library.
- term: macro
  definition: A piece of code in a program that is given a name. During compilation,
    the macro is replaced by its contents.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261029000027.096464BA2E1D@sourceware.org
date: '2026-10-29'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h` from `20261028` to `20261029`. This change is applied to the `gdb-18-branch` and is a routine update for the release versioning of the Binutils BFD library.
