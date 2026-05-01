---
project: binutils
subsystem: libsframe
patch_id: null
tags:
- libsframe
- bfd
- configure
- package version
discussion_id: ef693f78734ad647cb931ddd3eaedf2a.mforney@mforney.org
source_type: public_inbox
title: '[PATCH] libsframe: include bfd/version.m4 for BFD_VERSION'
headline: 'Libsframe: include bfd/version.m4 for BFD_VERSION'
tldr: The libsframe configure script is updated to correctly determine the package
  version by including bfd/version.m4.
proposer: Michael Forney <mforney@mforney.org>
consensus: Under Review
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- None apparent; this is a bug fix to ensure correct versioning.
exchanges:
- author: Michael Forney
  role: proposer
  position: Proposes including bfd/version.m4 in libsframe's configure script to fix
    the package version.
  quote: "libsframe/\n        * configure.ac: Fix package version by including bfd/version.m4.\n\
    \t* configure: Regenerate."
- author: H.J. Lu
  role: reviewer
  position: Reviewed and approved the patch.
  quote: null
primer_expert: This patch updates the libsframe configure script to correctly determine
  the package version. Libsframe is a library for creating and manipulating stack
  frames. The patch ensures that the `BFD_VERSION` macro is properly defined by including
  `bfd/version.m4`, which is part of the Binary File Descriptor (BFD) library.
primer_general: Libsframe is a library used by binary utilities to handle stack frames,
  which are data structures used to manage function calls in programs. This patch
  corrects how the version number of libsframe is determined during the configuration
  process (when the software is prepared for installation). By including a specific
  file (`bfd/version.m4`), the build process can accurately identify the version of
  libsframe being used.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ef693f78734ad647cb931ddd3eaedf2a.mforney@mforney.org
bugzilla_url: null
date: '2026-04-30'
---

Michael Forney proposes a patch to fix the libsframe package version in the configure script. The patch includes `bfd/version.m4` to correctly define `BFD_VERSION`. This ensures the package version is accurately reflected in the generated configuration files and output. H.J. Lu reviewed and approved the patch.
