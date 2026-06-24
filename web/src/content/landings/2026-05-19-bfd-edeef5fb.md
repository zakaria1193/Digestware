---
project: binutils
subsystem: bfd
patch_id: null
tags:
- build
- bfd
commit_hash: edeef5fb9c2dac72899322c66a1132501729bede
source_type: public_inbox
author: GDB Administrator <gdbadmin@sourceware.org>
headline: Update date in version.in.
tldr: The build date in bfd/version.h was updated.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The BFD library includes a version date in `bfd/version.h`, which is
  updated automatically. This does not affect the ABI or functionality.
primer_general: BFD is the Binary File Descriptor library, which provides a generic
  interface to various object file formats. The library includes a version date, which
  is updated automatically. This change doesn't affect functionality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260519000012.E2AD14BB24F2@sourceware.org
date: '2026-05-19'
is_stub: true
stub_reason: low-score
---

The build date in bfd/version.h was updated from 20260518 to 20260519. This change is part of an automated process.
