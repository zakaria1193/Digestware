---
project: binutils
subsystem: libiberty
patch_id: null
tags:
- libiberty
- sync
- gcc
- build system
- bug fix
discussion_id: 20261103012525.1143918-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: 'libiberty: sync with GCC'
headline: 'libiberty: sync with GCC'
tldr: Updates libiberty by syncing with recent GCC commits, including changes to Makefiles,
  configuration, and function implementations.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Pietro Monteiro <pietro@sociotechnical.xyz>
  role: proposer
  position: Pushed updates to `libiberty` by syncing with GCC commits, including build
    system adjustments and a fix for a signed integer overflow.
  quote: 'Sync the libiberty/ directory with gcc commit

    be07ead43d9d980584b745ee6e06c5d4309ced1d.  This pulls in the following

    gcc commits and the associated updates to ''libiberty/ChangeLog'':


    2612b60e5b6 libiberty: Update Makefile dependencies

    d58a2bf4760 config: mmap: Avoid the sanitizer configure check failure

    f5e51990065 libiberty: drop obsolete C functionality tests

    db890f7a7d3 configury: replace auto…'
primer_expert: This change synchronizes the `libiberty` subdirectory within binutils
  with the corresponding code in GCC. `libiberty` contains various utility functions
  used by both binutils and GCC. The sync pulls in recent GCC commits that modify
  `libiberty`'s build system (Makefiles, autoconf macros) and internal functions,
  ensuring consistency between the projects. It also integrates a GCC changelog entry
  for a bug fix.
primer_glossary:
- term: libiberty
  definition: A collection of utility functions used by GNU Binutils and GCC, often
    providing common functionality like string manipulation, memory allocation, and
    parsing.
- term: Makefile
  definition: A file used by the `make` utility to automate the build process of software
    projects, specifying dependencies and compilation rules.
- term: autoconf
  definition: A tool that automatically configures source code packages to adapt to
    a specific operating system or environment by generating shell scripts that check
    for system features and dependencies.
- term: signed integer overflow
  definition: A condition that occurs when an arithmetic operation on signed integers
    produces a result that is outside the range of values that can be represented
    by the integer type, leading to unpredictable behavior or incorrect results.
- term: d_compact_number
  definition: Likely a function within libiberty responsible for compacting or formatting
    numbers, possibly related to symbolic information or debugging data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261103012525.1143918-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This commit synchronizes the `libiberty` directory with recent changes from GCC, incorporating updates to build system files like `Makefile.in` and `configure.ac`, as well as modifications to `functions.texi` and specific object file compilations. It also brings in a changelog entry for a signed integer overflow fix in `d_compact_number`.
