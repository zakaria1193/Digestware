---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- versioning
- bfd
commit_hash: 633ae02c4ea8f87c670f7192804349860cfa291d
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Binutils BFD version date updated for upcoming release
tldr: Binutils BFD version date in version.h updated to 20261123.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This is a routine version update for the main binutils branch. The
  `BFD_VERSION_DATE` macro in `bfd/version.h` is incremented from `20261122` to `20261123`.
  This macro is typically used in release builds to denote the date of the release,
  and is excluded from sonames.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to handle
    various object file formats.
- term: version.h
  definition: A header file that contains versioning information for the BFD library.
- term: BFD_VERSION_DATE
  definition: A preprocessor macro defined in `version.h` that specifies the release
    date of the BFD library.
- term: soname
  definition: Shared object name. A field in shared library metadata that helps the
    dynamic linker resolve library dependencies.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123000013.116654AB0F8F@sourceware.org
date: '2026-11-23'
is_stub: true
stub_reason: low_score
---

The `BFD_VERSION_DATE` macro in `bfd/version.h` has been updated to reflect the current date, 20261123. This change is part of the routine process for versioning and releasing the binutils-gdb project.
