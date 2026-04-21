---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- debuginfo
- split debuginfo
- profiling
- performance
discussion_id: 877bq13a6w.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: gprof support for split debuginfo
tldr: This patch enables gprof to work with binaries stripped of debug information
  by utilizing split debuginfo files.
stakes: This enhancement allows developers to profile stripped binaries using gprof,
  improving performance analysis workflows.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases the complexity of gprof by adding support for split debuginfo.
- Adds a dependency on finding and loading the split debuginfo file.
- May increase the memory footprint of gprof when processing split debuginfo.
exchanges: []
primer_expert: The patch modifies gprof to use a separate debug BFD when a split debuginfo
  file is found. This is necessary because stripped binaries lack the symbol and line
  information required by gprof. Split debuginfo, typically stored in `.debug` directories
  or files, provides this information separately. The change allows gprof to function
  without requiring binaries to contain embedded debug information.
primer_general: gprof is a performance analysis tool that helps developers identify
  where a program spends its time. To do this, gprof needs debug information, which
  maps machine code to source code.  The `strip` command removes debug information
  from binaries to reduce their size.  Split debuginfo is a way to store this debug
  information separately from the main executable, allowing developers to debug or
  profile stripped binaries. This patch allows gprof to find and use this split debuginfo,
  enabling performance analysis on smaller, stripped binaries.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch enables `gprof` to utilize split debuginfo, allowing it to function correctly with binaries that have been stripped of their debug information using `strip -g`.  It uses the debug BFD (Binary File Descriptor) to access symbol and line information from the separated debuginfo file. This change is presented as a step towards potential future support for debuginfod/dwz.
