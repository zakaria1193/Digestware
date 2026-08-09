---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
- versioning
commit_hash: d751acfd1439a4deaea2a0e1cde7fb44f8d3f952
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for gdb-18 branch.
tldr: The BFD version date in version.h is updated to August 9, 2026 for the gdb-18
  branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bfd/version.h` file, part of the Binary File Descriptor library,
  is updated to reflect a new release date. This commit targets the `gdb-18-branch`
  of the binutils-gdb repository, modifying the `BFD_VERSION_DATE` macro.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level module in the GNU Binutils
    project that provides a standardized interface for reading and writing object
    file formats.
- term: macro
  definition: A preprocessor directive in C/C++ that defines a symbolic name or a
    piece of code that is substituted at compile time. `BFD_VERSION_DATE` is a macro
    used for versioning.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260809000028.100064BA79A3@sourceware.org
date: '2026-08-09'
is_stub: true
stub_reason: low_score
---

This commit updates the `BFD_VERSION_DATE` in `bfd/version.h` to `20260809` for the `gdb-18-branch`. This change is part of the routine version management process within the binutils-gdb project.
