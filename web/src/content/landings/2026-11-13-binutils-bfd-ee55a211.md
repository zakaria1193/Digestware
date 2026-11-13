---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- release
commit_hash: ee55a2113ff022b4da1c1b1cd27919c9cdab9fdf
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Binutils version date updated for the GDB 18 branch.
tldr: Binutils version date updated for the GDB 18 branch to 20261113.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the GDB 18 branch. This macro is part of the versioning scheme for the Binutils
  and GDB projects, and its update reflects the progression of the release cycle.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library within Binutils
    that provides a common interface for reading and writing various executable file
    formats.
- term: Macro
  definition: A piece of code that has been pre-defined to be replaced with a particular
    piece of code prior to compilation. In C/C++, these are typically defined using
    '#define'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261113000029.836364B920AB@sourceware.org
date: '2026-11-13'
is_stub: true
stub_reason: low_score
---

The version date in `bfd/version.h` for the binutils-gdb-18 branch has been updated from 20261112 to 20261113. This is a routine update to reflect the current date in the release process.
