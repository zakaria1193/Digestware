---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- maintenance
- binutils
commit_hash: 90ba9a3a87362ab3fd5d648c34e4985c05b562e2
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'bfd: Update release date in version.h'
tldr: Binutils release date in version.h updated to August 3, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  from `20260802` to `20260803`. This is a standard maintenance update for release
  branches (`binutils-gdb/binutils-2_47-branch`, `binutils-gdb/gdb-17-branch`, and
  the main `binutils-gdb` repository) to reflect the current date for the build.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to provide a common interface for reading and writing various executable file
    formats.
- term: version.h
  definition: A header file that typically contains version information and macros
    for a software project. In Binutils, it defines version strings and dates.
- term: macro
  definition: A piece of code in C/C++ that is given a name. When the code is compiled,
    the preprocessor replaces the name with the contents of the macro. Often used
    for constants or small code snippets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260803000042.541414BA2E20@sourceware.org
date: '2026-08-03'
is_stub: true
stub_reason: low_score
---

The release date macro `BFD_VERSION_DATE` in `bfd/version.h` has been updated to reflect August 3, 2026. This change is part of the routine maintenance for upcoming releases, ensuring version information is current.
