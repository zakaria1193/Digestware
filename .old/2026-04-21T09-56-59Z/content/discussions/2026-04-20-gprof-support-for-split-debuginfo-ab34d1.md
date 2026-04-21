---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- profiling
- debugging
- debuginfo
- split debuginfo
discussion_id: 877bq13a6w.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: Gprof support for split debuginfo
tldr: Frank Eigler pings for a review of his patch adding support for split debuginfo
  to gprof.
stakes: This patch enables gprof to work correctly with binaries that have been stripped
  of debug information and have separate debuginfo files.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to `gprof` to support split debuginfo.
- Enables `gprof` to work with stripped binaries, which can be smaller and faster.
- Potentially increases the time required to profile a program, as `gprof` needs to
  locate and process the separate debuginfo files.
exchanges:
- author: fche@redhat.com
  role: proposer
  position: Pings for review of the patch.
  quote: Ping.
primer_expert: '`gprof` needs to find debuginfo to map samples to function names and
  line numbers.  When binaries are stripped and debuginfo is split, `gprof` needs
  to be able to locate the external debuginfo files.'
primer_general: '`gprof` is a performance analysis tool that profiles the execution
  of a program to determine where it spends its time. This information is used to
  identify performance bottlenecks and optimize the program''s code.  `gprof` uses
  debugging information to correlate execution samples with source code lines and
  function names. Stripping debug information reduces the size of the executable,
  but requires `gprof` to locate separate debuginfo files to function correctly.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Frank Eigler is requesting a review for his patch that adds split debuginfo support to gprof, allowing it to function correctly with stripped binaries that have separate debuginfo files.
