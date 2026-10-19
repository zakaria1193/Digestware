---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
- maintenance
commit_hash: fbdd5bb625b861f5359da29b0541ddcee8d705ec
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'bfd: Update version date for gdb-18 branch'
tldr: Updates the release date in bfd/version.h for the gdb-18 branch.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: ''
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    responsible for reading and writing various object file formats.
- term: BFD_VERSION_DATE
  definition: A preprocessor macro in BFD that defines the release date of the library,
    typically used for versioning purposes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261019000025.1967F4BA2E1E@sourceware.org
date: '2026-10-19'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h from 20261018 to 20261019. This change is part of the regular maintenance for the gdb-18 branch, ensuring the version information reflects the current build date.
