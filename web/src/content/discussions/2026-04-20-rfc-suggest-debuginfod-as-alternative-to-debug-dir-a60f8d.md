---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- objdump
- readelf
- debugging
- debuginfod
discussion_id: 87zf35d098.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: objdump: Add --debug-dir=<DIR> option'
headline: 'RFC: Suggest debuginfod as alternative to --debug-dir'
tldr: Frank Ch. Eigler suggests using `debuginfod` as an alternative to the proposed
  `--debug-dir` option for `objdump` and `readelf`.
stakes: This discussion explores alternative approaches to locating debug information,
  which affects the usability of debugging tools. `debuginfod` can provide a more
  comprehensive and automated solution compared to a simple directory search.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The discussion introduces an alternative solution (debuginfod)
  to the problem, neither strongly supporting nor rejecting the original proposal.
technical_tradeoffs:
- The `--debug-dir` option provides a simple way to specify a directory to search,
  but it requires manual configuration.
- '`debuginfod` offers a more automated solution, but it requires setting up and running
  a `debuginfod` server.'
- '`debuginfod` might have a higher overhead compared to a simple directory search,
  but it can provide a more comprehensive solution.'
exchanges:
- author: fche@redhat.com
  role: proposer
  position: Suggests using `debuginfod` as an alternative to the `--debug-dir` option,
    providing instructions on how to configure and use it.
  quote: "By the way, you can handle this scenario easily enough by running a local\
    \ temporary copy of elfutils debuginfod, giving it a list of your build subdirectories:\n\
    \n   debuginfod -p 8003 -d :memory: -F /build/tree/1 /build/tree/2 &\n   export\
    \ DEBUGINFOD_URLS=http://localhost:8003/"
- author: Nick Clifton <nickc@redhat.com>
  role: contributor
  position: Acknowledges the suggestion of using debuginfod.
  quote: null
primer_expert: This discussion revolves around the problem of locating separate debug
  information files for binaries.  The RFC proposes a `--debug-dir` option for `objdump`
  and `readelf`.  Frank suggests using `debuginfod`, which is a system for automatically
  retrieving ELF objects and their associated debugging information over HTTP.  `debuginfod`
  indexes build artifacts and debug information, and makes them available to debugging
  tools.  The key is the `DEBUGINFOD_URLS` environment variable which tells the toolchain
  where to find a `debuginfod` instance.
primer_general: When debugging a program, debug information is needed to map machine
  code back to the original source code. This information is often stored in separate
  files.  The `objdump` and `readelf` utilities are used to inspect binary files.
  This discussion is about how to make it easier for these tools to find the debug
  information. One suggestion is to add a `--debug-dir` option, which tells the tools
  where to look for the debug information files. Another suggestion is to use `debuginfod`,
  a system that automatically finds and provides debug information for programs. `debuginfod`
  can be more convenient because it eliminates the need to manually specify the location
  of the debug information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/871pg9385i.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

In response to Nick Clifton's RFC for adding a `--debug-dir` option to `objdump` and `readelf`, Frank Ch. Eigler suggests using a local temporary copy of `elfutils debuginfod` instead.  He outlines how to configure `debuginfod` to search specific build subdirectories and then use the `DEBUGINFOD_URLS` environment variable to enable the toolchain to find sources, binaries, and debuginfo.
