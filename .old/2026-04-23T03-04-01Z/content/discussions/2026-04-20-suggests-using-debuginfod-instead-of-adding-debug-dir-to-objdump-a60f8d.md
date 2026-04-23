---
project: binutils
subsystem: rfc
patch_id: null
tags:
- objdump
- debuginfo
- debuginfod
- DWARF
- elfutils
discussion_id: 87zf35d098.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: objdump: Add --debug-dir=<DIR> option'
headline: Suggests using debuginfod instead of adding --debug-dir to objdump
tldr: Instead of adding a new `--debug-dir` option to objdump, consider using a local
  debuginfod instance to manage debug information.
stakes: Discusses alternative approaches to finding debug information for objdump,
  impacting user convenience and the overall design of debugging tools.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding `--debug-dir` simplifies usage for simple cases but duplicates functionality
  that debuginfod already provides.
- Using debuginfod requires setting up and configuring a separate service.
- debuginfod offers a more centralized and standardized approach to managing debug
  information.
exchanges:
- author: fche@redhat.com
  role: proposer
  position: Suggests using a local debuginfod instance as an alternative to the proposed
    `--debug-dir` option, providing a centralized way to locate debug information.
  quote: By the way, you can handle this scenario easily enough by running a local
    temporary copy of elfutils debuginfod, giving it a list of your build subdirectories
- author: Nick Clifton
  role: other
  position: No position presented in this exchange.
  quote: null
primer_expert: objdump uses DWARF debug information to display source code and other
  debugging-related data. When debug information is stored in separate files, objdump
  needs a way to locate them. Debuginfod is a service that provides debug information
  over HTTP. This discussion considers using debuginfod as an alternative to adding
  a `--debug-dir` option to specify where to search for these separate files.  This
  approach leverages a standardized service rather than adding tool-specific options.
primer_general: objdump is a command-line tool that displays information about object
  files, including disassembled code and debugging information. Debugging information
  helps developers understand the relationship between the compiled code and the original
  source code. Sometimes, this debug information is stored separately from the main
  executable file. This discussion explores different ways for objdump to find these
  separate debug information files, either by adding a new command-line option or
  by using a dedicated service called debuginfod.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/871pg9385i.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Frank Eigler suggests using a local, temporary instance of elfutils debuginfod as an alternative to Nick Clifton's proposed `--debug-dir` option for objdump. Debuginfod can be configured to search a list of build subdirectories, providing a centralized way to locate debug information. This approach avoids modifying objdump directly.
