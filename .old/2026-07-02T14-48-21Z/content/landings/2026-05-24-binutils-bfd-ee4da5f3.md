---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- build
- version
commit_hash: ee4da5f3ae22aaf65db3adf1f3d9ab9c047e4178
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Automatic date update in version.in
tldr: Updates the build date in `bfd/version.h`.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates `BFD_VERSION_DATE` in `bfd/version.h`. This is
  an automated change typically done by the build system to keep the version information
  current. It doesn't affect the functionality of BFD itself.
primer_general: The Binary File Descriptor (BFD) library handles different executable
  file formats.  This commit updates the date in the BFD version file. This is just
  a routine update to keep the build date current and doesn't change how BFD works.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260524000011.959D44BAE7ED@sourceware.org
date: '2026-05-24'
is_stub: true
stub_reason: low-score
---

This commit automatically updates the build date in the `bfd/version.h` file. This ensures the version information is accurate.
