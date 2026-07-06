---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- versioning
- build
commit_hash: 11beac04de6368895006ded8a99de0047feb3d70
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Automatic date update in version.in
tldr: Binutils versioning automatically updates the build date.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `BFD_VERSION_DATE` macro in `bfd/version.h` is updated by one day.
  This macro is typically used during the build process to embed a timestamp into
  the version information of the Binutils library. In release builds, this date is
  often omitted from the final version string and soname, but it serves as a reference
  during development and for internal tracking.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A core component of Binutils used for
    reading and writing various object file formats.
- term: version.in
  definition: A template file used in build systems (like Autoconf/Automake) that
    contains version information. It is processed during the configure or build stage
    to generate the final version header file.
- term: BFD_VERSION_DATE
  definition: A preprocessor macro defined in `bfd/version.h` that specifies the release
    date of the Binutils library.
- term: soname
  definition: Shared Object Name. A name embedded in a shared library that indicates
    its compatibility version, used by the dynamic linker.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260706000039.3B9564BA2E09@sourceware.org
date: '2026-07-06'
is_stub: true
stub_reason: low_score
---

The build date for the Binutils versioning information has been automatically updated. This commit changes the `BFD_VERSION_DATE` macro in `bfd/version.h` from `20260705` to `20260706`, reflecting the current build date in the versioning system.
