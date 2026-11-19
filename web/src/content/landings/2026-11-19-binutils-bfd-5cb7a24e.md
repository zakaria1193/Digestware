---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- maintenance
commit_hash: 5cb7a24e5cff99d1e47ac3bb444d813c1937df3a
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update BFD version date
tldr: The BFD library's version date is updated to November 19, 2026.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `BFD_VERSION_DATE` macro in `bfd/version.h`
  for the `binutils-2.47` branch. This is a routine update to reflect the current
  date in the versioning information and does not alter any functional code or ABI.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    responsible for handling object file formats.
- term: version date
  definition: A macro defining the release date of the software, used in version strings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261119000042.DA5954BA2E13@sourceware.org
date: '2026-11-19'
is_stub: true
stub_reason: low_score
---

The version date for the BFD library has been updated from November 18, 2026, to November 19, 2026. This change is part of routine maintenance for the binutils-2.47 branch and does not affect functionality.
