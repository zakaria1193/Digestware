---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- debuginfo
- split debuginfo
- profiling
- bfd
discussion_id: 877bq13a6w.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: gprof support for split debuginfo
tldr: Pings a patch that adds support for split debuginfo to gprof.
stakes: Enables gprof to work with stripped binaries that have separate debuginfo
  files, improving profiling capabilities.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to gprof by requiring it to handle separate debuginfo files.
- May increase the time it takes gprof to process binaries with split debuginfo.
- Improves the usability of gprof for binaries that have been stripped of debug information.
exchanges: []
primer_expert: This patch modifies `gprof` to handle split debuginfo, which is when
  debug information is separated from the main executable binary. This separation
  is often done using `strip -g`. The patch uses the debug BFD (Binary File Descriptor)
  to locate symbol and line information in the separate debuginfo file. This is a
  step towards potential future `debuginfod`/`dwz` support.
primer_general: '`gprof` is a performance analysis tool that profiles the execution
  of a program to identify performance bottlenecks. Debug information, which maps
  machine code to source code, is necessary for `gprof` to produce human-readable
  profiling results.  Split debuginfo is a technique where debug information is stored
  in a separate file, allowing the main executable to be smaller. This patch enhances
  `gprof` to correctly utilize these separate debug information files, allowing developers
  to profile programs even when debug information has been split.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This is a ping for a patch that adds support for split debuginfo to gprof. The patch allows gprof to use the debug BFD for symbol and line information when a separate debuginfo file is found, enabling gprof to work correctly with binaries stripped with `strip -g`.
