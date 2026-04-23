---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- objdump
- readelf
- debug information
- debuginfod
discussion_id: 60031e0e-1d9a-441c-b66d-f2418abd338f@redhat.com
source_type: public_inbox
title: 'Re: RFC: objdump: Add --debug-dir=<DIR> option'
headline: 'RFC: objdump: Add --debug-dir=<DIR> option'
tldr: A request for comments on adding a `--debug-dir` option to objdump is met with
  a suggestion to use `debuginfod` instead.
stakes: The ability to locate debug information easily is crucial for effective debugging.
  This impacts developer productivity and the ability to diagnose issues quickly.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a `--debug-dir` option simplifies the process for users who don't have or
  want to use debuginfod.
- Using debuginfod provides a more centralized and automated way to manage debug information,
  but requires setting up and configuring the service.
- A `--debug-dir` option would be specific to objdump/readelf, while debuginfod is
  a system-wide solution.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Acknowledges the suggestion to use `debuginfod`.
  quote: Thanks for the tip :-).
primer_expert: '`objdump` is a binutils utility for displaying information about object
  files. `readelf` displays the content of ELF format files. Separate debug information
  files store debugging information outside of the main executable, typically to reduce
  the size of the deployed binary. `debuginfod` is a service that provides access
  to debug information.'
primer_general: Objdump and readelf are tools used to inspect the contents of compiled
  programs and libraries. "Debug information" is extra data added to compiled programs
  that helps link the machine code back to the original source code, which helps debuggers
  understand the code in the file.  Often, this debug information is stored in separate
  files to reduce the size of the main program. Debuginfod is a service that helps
  locate these separate debug information files. This discussion is about a proposal
  (RFC) to make it easier for objdump to find these debug information files, and a
  suggestion to use debuginfod instead.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/60031e0e-1d9a-441c-b66d-f2418abd338f@redhat.com
bugzilla_url: null
date: '2026-04-21'
---

This discussion revolves around a proposed patch to enhance `objdump` and `readelf` by adding a command-line option (`--debug-dir`) to specify a directory to search for separate debug information files.  In response, Frank suggests using `debuginfod` as an alternative, which can handle this scenario by creating a local temporary server.
