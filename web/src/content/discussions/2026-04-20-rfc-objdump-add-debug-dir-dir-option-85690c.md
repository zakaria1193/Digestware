---
project: binutils
subsystem: rfc
patch_id: null
tags:
- objdump
- debuginfo
- elfutils
- debuginfod
discussion_id: 871pg9385i.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: objdump: Add --debug-dir=<DIR> option'
headline: 'RFC: objdump: Add --debug-dir=<DIR> option'
tldr: Suggests using elfutils debuginfod as an alternative to the proposed `--debug-dir`
  option for objdump.
stakes: Suggests an alternative approach to finding debug information, potentially
  impacting debugging workflows.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Using debuginfod requires setting up and configuring a separate service.
- The proposed --debug-dir option would be simpler for local, one-off debugging scenarios.
- debuginfod provides a more centralized and scalable solution for managing debug
  information.
exchanges: []
primer_expert: The RFC proposes a change to `objdump` to find separate debug files.
  This response suggests using `debuginfod` instead. `debuginfod` is part of `elfutils`
  and serves debug information (sources, binaries, and debuginfo) over HTTP.  A local
  instance can be configured to search specific directories, and the `DEBUGINFOD_URLS`
  environment variable can point toolchain tools to the local instance.
primer_general: '`objdump` is a command-line utility for displaying information about
  object files. Debug information is often stored separately from the main executable
  to reduce its size.  `elfutils debuginfod` is a tool that serves debug information
  over HTTP. This allows debuggers to automatically find the correct debug information
  for a program, even if it''s stored in a non-standard location.  The message suggests
  using `debuginfod` as a system-wide solution for locating debug information, rather
  than adding a specific option to `objdump` itself.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/871pg9385i.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This message responds to an RFC proposing a `--debug-dir` option for objdump to specify a directory for searching separate debug information files. The author suggests using a local temporary copy of elfutils debuginfod instead, configured to search the build subdirectories. This approach allows the toolchain to find sources, binaries, and debuginfo.
