---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- dynamic linker
- symbol conflicts
- dependency management
- library isolation
discussion_id: 20260421090020.59726-4-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 3/3] Add a solution to prevent conflict between symbols loaded from dependencies'
headline: 'RFC: Glibc will gain symbol conflict prevention for dependencies.'
tldr: Adds a mechanism to prevent symbol conflicts between dependencies by assigning
  unique IDs to dlconf sections and checking during symbol resolution.
stakes: Prevents symbol clashes when using multiple ld.so caches, improving application
  stability.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds overhead to symbol resolution but prevents conflicts.
- Requires changes to the dynamic linker's data structures and algorithms.
- May increase the complexity of debugging dynamic linking issues.
exchanges:
- author: Łukasz Stelmach <l.stelmach@samsung.com>
  role: proposer
  position: Proposes a solution to prevent symbol conflicts by assigning unique IDs
    to dlconf sections and checking during symbol resolution.
  quote: Based on these data, during the symbol resolution process, it is checked
    whether a given object can use a symbol from another object.
primer_expert: This patch adds symbol conflict prevention to glibc's dynamic linker.
  It assigns unique IDs to sections defined in the `dlconf` configuration and uses
  these IDs to control symbol visibility during resolution. This modifies `elf/dl-lookup.c`
  and related files. This is crucial for scenarios where multiple isolated environments
  are used, each with its own set of libraries and potential symbol clashes.
primer_general: This patch addresses the problem of symbol conflicts in the GNU C
  Library (glibc). When a program uses multiple libraries, it's possible that different
  libraries define the same symbol (e.g., a function with the same name). This can
  lead to unexpected behavior or crashes. This patch introduces a mechanism to prevent
  these conflicts by isolating libraries into different sections and controlling which
  symbols are visible to each library. This is particularly important in complex systems
  where different components may rely on different versions of the same library.
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-4-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This RFC introduces a solution to prevent symbol conflicts between dependencies when using multiple `ld.so` caches. Each section in the `dlconf` configuration file is assigned a unique number. During linking, each object (`struct link_map`) is assigned the section number and a list of its direct dependencies. The symbol resolution process checks whether an object can use a symbol from another object based on these data.
