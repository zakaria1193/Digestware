---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- dynamic linker
- dlconf
- symbol resolution
- conflict prevention
discussion_id: 20260421090020.59726-4-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 3/3] Add a solution to prevent conflict between symbols loaded from dependencies'
headline: Prevent symbol conflicts with dlconf sections
tldr: This patch prevents symbol conflicts between dependencies by assigning each
  dlconf section a unique number and checking symbol resolution against direct depend…
stakes: Preventing symbol conflicts ensures that libraries can safely use their own
  versions of dependencies without interfering with other libraries in the system.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in the dynamic linker's symbol resolution process.
- Potential performance overhead due to additional checks during symbol lookup.
- Improved isolation of libraries and prevention of symbol conflicts.
exchanges: []
primer_expert: This patch extends the dlconf functionality by adding symbol conflict
  prevention. Each dlconf section gets a unique number. During linking, each object
  (`link_map`) is assigned the section number. Symbol resolution checks are performed
  against objects in the same section or direct dependencies (DT_NEEDED). This avoids
  symbol clashes when different libraries use different versions of the same dependency.
primer_general: When multiple libraries are loaded into a program, they might depend
  on the same underlying libraries but different versions. This can lead to symbol
  conflicts, where the program uses the wrong version of a function or variable. This
  patch prevents such conflicts by isolating libraries loaded from different configuration
  sections.  Each library is tagged with a section number, and the dynamic linker
  ensures that symbols are resolved within the same section or from direct dependencies,
  avoiding accidental mixing of symbols from incompatible versions.
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-4-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

Łukasz Stelmach proposes assigning a unique number to each section in the dlconf configuration file and using this number during symbol resolution to prevent conflicts.  The goal is to allow libraries to use their own versions of dependencies (e.g., libpng.so) without conflicting with other libraries that might require a different version of the same dependency. Symbol resolution is checked against objects within the same section or direct dependencies.
