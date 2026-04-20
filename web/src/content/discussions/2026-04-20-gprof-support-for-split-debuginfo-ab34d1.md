---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gprof
- debuginfo
- profiling
- elf
discussion_id: 877bq13a6w.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: Gprof support for split debuginfo
tldr: Pings a patch adding gprof support for split debuginfo, enabling it to work
  with stripped binaries.
stakes: Enables gprof to profile binaries even when debug information is separated,
  which is common in distribution packaging.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to gprof's logic to handle split debuginfo.
- May require changes to how gprof locates debug information files.
- Improves gprof's usability in environments where debug information is separated.
primer_expert: '`gprof` is a profiling tool. Split debuginfo is a method of separating
  debugging information from the main executable. This patch likely modifies `gprof`
  to locate and utilize the separated debuginfo files when present. This addresses
  a common scenario when binaries are stripped for distribution.'
primer_general: '`gprof` is a tool used to profile programs, providing insights into
  where the program spends its time. Debug information, like symbol names and line
  numbers, is often stripped from production binaries to reduce their size. Split
  debuginfo stores this information in a separate file, allowing debugging without
  bloating the main executable. This patch enables `gprof` to find and use this separate
  debug information, allowing profiling of stripped binaries.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This is a ping for a patch that adds gprof support for split debuginfo. This allows gprof to work correctly with binaries that have been stripped of debug information using `strip -g`, where the debug information is stored in a separate file. The patch is aimed at improving gprof's usability in environments where debug information is not embedded in the main binary.
