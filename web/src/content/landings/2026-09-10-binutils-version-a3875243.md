---
project: binutils
subsystem: binutils/version
patch_id: null
tags:
- release
- versioning
commit_hash: a3875243449f506137113bad29a5365d721c20c3
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update release date in binutils version information
tldr: The release date in binutils' version information has been updated to September
  10, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is updated to reflect
  the current release date. This macro is used in constructing version strings and
  sonames, although it is typically excluded from release artifacts themselves. The
  change simply advances the date by one day.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    and GDB to provide a common interface for reading and writing various object file
    formats.
- term: Version string
  definition: A human-readable string that identifies the specific version of a software
    package.
- term: SONAME
  definition: Shared Object Name. A name embedded within a shared library that indicates
    its compatibility. Used by the dynamic linker to find the correct library version.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260910000043.A3D0F4BB58B1@sourceware.org
date: '2026-09-10'
is_stub: true
stub_reason: low_score
---

This commit updates the version date defined in `bfd/version.h` from `20260909` to `20260910`. This change reflects the current date for the latest release or development snapshot, ensuring accurate version tracking.
