---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- release
- versioning
- gdb
commit_hash: 53ff0f0d6196d1f07cd085250b5e61eebb4f4e95
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Automatic date update in version.in
tldr: Updates the release date in binutils' version header for the GDB 18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro within `bfd/version.h`
  specifically for the `gdb-18-branch`. This macro is utilized to incorporate the
  release date into version strings or sonames. The change ensures that the version
  information accurately reflects the current date for this particular development
  branch.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a part of GNU Binutils, which provides
    a standardized interface for reading and writing various object file formats.
- term: version.h
  definition: A header file containing version information macros for a software project,
    such as version numbers, dates, and release identifiers.
- term: macro
  definition: A piece of code in a program that is given a name. During compilation,
    the macro name is replaced by its corresponding code. `#define` is used to create
    macros in C/C++.
- term: soname
  definition: Shared object name. A string embedded in a shared library that identifies
    the library in a way that is usable by the linker and dynamic loader.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260902000028.07CB14BA2E2B@sourceware.org
date: '2026-09-02'
is_stub: true
stub_reason: low_score
---

The release date embedded in the `bfd/version.h` file for the GDB 18 branch has been updated from September 1, 2026, to September 2, 2026. This is a routine update to reflect the current date in versioning information.
