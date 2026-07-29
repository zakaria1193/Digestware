---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
commit_hash: 5ec4837c9c3122b7f9c4eafaf1dae2a5555b46cb
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date.
tldr: Updates the BFD version date in version.h for the binutils-2.47 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`.
  This macro is used to embed a release date into version strings and sonames. The
  change reflects the progression of the `binutils-2_47-branch` towards a release.
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
url: https://inbox.sourceware.org/binutils-cvs/20260729000041.75A334BB3BCC@sourceware.org
date: '2026-07-29'
is_stub: true
stub_reason: low_score
---

The release date used in the BFD versioning has been updated from 20260728 to 20260729. This change is part of the release process and ensures the versioning information is accurate for the binutils-2.47 branch.
