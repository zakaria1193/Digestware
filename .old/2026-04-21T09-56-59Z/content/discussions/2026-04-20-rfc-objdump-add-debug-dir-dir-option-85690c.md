---
project: binutils
subsystem: rfc
patch_id: null
tags:
- objdump
- debugging
- debuginfo
- debuginfod
discussion_id: 871pg9385i.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: objdump: Add --debug-dir=<DIR> option'
headline: 'RFC: objdump: Add --debug-dir=<DIR> option'
tldr: Suggests using a local debuginfod instance as an alternative to adding a `--debug-dir`
  option to objdump.
stakes: This discussion is relevant to developers who debug binaries with split debug
  information, as it affects how debuggers and related tools locate the necessary
  debug symbols.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a `--debug-dir` option would simplify the command-line usage of `objdump`
  for some users, but could also lead to inconsistencies if the specified directory
  is not up-to-date.
- Using `debuginfod` requires setting up and configuring a `debuginfod` server, but
  provides a more robust and scalable solution for managing debug information.
exchanges:
- author: fche@redhat.com
  role: other
  position: Suggests using a local debuginfod instance as an alternative to the proposed
    `--debug-dir` option.
  quote: By the way, you can handle this scenario easily enough by running a local
    temporary copy of elfutils debuginfod, giving it a list of your build subdirectories
primer_expert: '`objdump` and `readelf` need to locate split debuginfo files (.dwo)
  when the main binary is stripped.  The traditional approach is a fixed search path
  or environment variables. `debuginfod` is a modern alternative.'
primer_general: '`objdump` is a command-line utility for displaying various information
  about object files, including debugging information.  Separate debug files are used
  to store debugging information outside of the main executable, typically to reduce
  the size of the deployed binary. The location of these separate files needs to be
  discoverable by debuggers and related tools. `debuginfod` is a tool that provides
  a centralized way to locate debug information files.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/871pg9385i.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Nick Clifton proposed adding a `--debug-dir` option to objdump to specify a directory to search for separate debug information files. Frank Eigler suggests using a local temporary instance of elfutils debuginfod instead.
