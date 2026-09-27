---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release
- binutils
commit_hash: b94ddc3e19bd25f1341c998b13e1841ebef5aa55
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: Update the BFD_VERSION_DATE macro in version.h to reflect the current date.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates the BFD_VERSION_DATE macro in bfd/version.h. This
  macro is used in release versioning for the BFD library. The update is a routine
  increment for the release process, ensuring the version date reflects the current
  release.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library. It provides a common interface for
    handling various object file formats.
- term: BFD_VERSION_DATE
  definition: A preprocessor macro in bfd/version.h that stores the release date of
    the BFD library in YYYYMMDD format.
- term: macro
  definition: A piece of code defined with a name. In C, the preprocessor replaces
    macro names with their corresponding definitions before compilation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260927000013.72C2A4BA9002@sourceware.org
date: '2026-09-27'
is_stub: true
stub_reason: low_score
---

The BFD_VERSION_DATE macro in bfd/version.h was updated to 20260927. This change automatically advances the version date as part of the release process for binutils-gdb.
