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
tldr: Suggests using debuginfod as an alternative to a new objdump option for specifying
  debug info directories.
stakes: Changing how debug information is located can impact debugging workflows and
  tool integration.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a new command-line option increases the complexity of `objdump`.
- Using `debuginfod` requires setting up and configuring a separate service.
exchanges:
- author: fche@redhat.com
  role: other
  position: Suggests using a local `debuginfod` server as a workaround, configuring
    it with the build directories.
  quote: By the way, you can handle this scenario easily enough by running a local
    temporary copy of elfutils debuginfod, giving it a list of your build subdirectories
primer_expert: '`objdump` needs to locate debuginfo for stripped binaries. The proposal
  adds a command-line option to specify a search path, which is an alternative to
  using `debuginfod`.'
primer_general: '`objdump` is a tool for inspecting object files and executables,
  often used in debugging.  Debug information, crucial for symbolic debugging, can
  be stored separately from the main executable. This discussion concerns how `objdump`
  locates these separate debug information files. The standard approaches involve
  searching pre-defined locations, but this proposal considers adding a command-line
  option to specify a directory to search. An alternative approach involves using
  `debuginfod`, a server that provides debug information for binaries.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/871pg9385i.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Nick Clifton proposed adding a `--debug-dir` option to `objdump` to specify directories for finding separate debug information files. Frank Eigler suggests using a local `debuginfod` instance instead, pointing it to the relevant build subdirectories.
