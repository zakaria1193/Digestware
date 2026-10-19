---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- release
- maintenance
commit_hash: 13e5bf5c6725e24eb2fa9c396f3f7b76db4a18c1
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: 'bfd: Update version date for 2.47 branch'
tldr: Updates the release date in bfd/version.h for the binutils-2.47 branch.
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
url: https://inbox.sourceware.org/binutils-cvs/20261019000039.A6C1B4BA2E23@sourceware.org
date: '2026-10-19'
is_stub: true
stub_reason: low_score
---

This commit updates the BFD_VERSION_DATE macro in bfd/version.h from 20261018 to 20261019. This change is part of the regular maintenance for the binutils-2.47 branch, ensuring the version information reflects the current build date.
