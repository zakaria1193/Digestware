---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
commit_hash: 002e6fb956c0be93efc91a8c16077eb3d4259dfc
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date for binutils-gdb branch
tldr: Updates the version date in BFD for the binutils-gdb branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Updates the BFD_VERSION_DATE macro in bfd/version.h for the main binutils-gdb
  branch to reflect the current date.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level component of GNU Binutils
    used for reading and writing various object file formats.
- term: version.h
  definition: A header file within the BFD library that defines version-related macros,
    including the release date.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260905000012.A979E4BB58A5@sourceware.org
date: '2026-09-05'
is_stub: true
stub_reason: low_score
---

The BFD version date in `version.h` has been updated from `20260904` to `20260905`. This change is applied to the main `binutils-gdb` development branch.
