---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- gdb
- release
commit_hash: 0d3bdbc0c736a0454fed5a65646eccfa48f1b0b5
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for gdb-17 branch.
tldr: Updates the BFD version date in version.h for the gdb-17 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the `gdb-17-branch`. This macro is used to embed a release date into version
  strings and sonames. This change reflects the progression of the `gdb-17-branch`.
primer_glossary:
- term: BFd
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    responsible for handling various object file formats.
- term: version.h
  definition: A header file that contains macros defining the version information
    for the Binutils project.
- term: soname
  definition: Shared object name. A field in an ELF shared library that specifies
    its public API version and is used by the dynamic linker to find the correct library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260729000027.0B8784BB3BCC@sourceware.org
date: '2026-07-29'
is_stub: true
stub_reason: low_score
---

The release date for the GDB component has been updated in `version.h` for the `gdb-17-branch`. The date changes from 20260728 to 20260729, reflecting the ongoing development and release cycle for GDB.
