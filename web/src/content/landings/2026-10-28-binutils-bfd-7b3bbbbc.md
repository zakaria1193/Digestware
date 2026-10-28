---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- release engineering
- binutils
commit_hash: 7b3bbbbc8aabce6009c26da06dc62f408f9a0d64
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Binutils BFD version date updated to October 28, 2026.
tldr: The BFD_VERSION_DATE macro in binutils is updated for the new release.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`.
  This macro is used to embed a date stamp into the BFD library, typically for release
  identification. The change reflects a new day in the release cycle.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a component of GNU Binutils that
    provides a standardized interface for reading and writing various executable file
    formats.
- term: BFD_VERSION_DATE
  definition: A preprocessor macro used to define the date associated with a specific
    BFD library version.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028000044.816B84BA2E39@sourceware.org
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

The BFD_VERSION_DATE macro in `bfd/version.h` has been updated to reflect the current date of October 28, 2026. This is a routine update for release versioning and does not affect functionality.
