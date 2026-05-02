---
project: binutils
subsystem: libsframe
patch_id: null
tags:
- binutils
- libsframe
- versioning
- build system
- configure
discussion_id: ceb2fbaed4926227f68be6941c6273f5.mforney@mforney.org
source_type: public_inbox
title: '[PATCH v2] libsframe: include bfd/version.m4 for BFD_VERSION'
headline: 'Libsframe: include bfd/version.m4 for BFD_VERSION'
tldr: Fixes the libsframe package version by including `bfd/version.m4` in `configure.ac`.
proposer: Michael Forney <mforney@mforney.org>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures accurate versioning of libsframe.
- No apparent downsides.
exchanges: []
primer_expert: libsframe is a support library for handling stack frames. This patch
  fixes the package version in the `configure` script, ensuring that it's correctly
  derived from the BFD version. This is important for consistent versioning across
  the binutils project.
primer_general: This patch corrects the version number reported for the libsframe
  library. Libsframe is a component of the binutils project. The build system uses
  the `configure` script to determine various settings, including the version number.
  This patch ensures that the version number is correctly obtained from a central
  definition, ensuring consistency.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ceb2fbaed4926227f68be6941c6273f5.mforney@mforney.org
bugzilla_url: null
date: '2026-04-30'
---

Michael Forney proposes a patch to fix the package version of libsframe by including `bfd/version.m4` in `configure.ac`. This ensures that `BFD_VERSION` is properly defined during the configuration process. The patch also regenerates `configure` and `Makefile.in` to reflect the change.
