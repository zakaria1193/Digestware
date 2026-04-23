---
project: glibc
subsystem: ldconfig
patch_id: null
tags:
- glibc
- ldconfig
- ld.so.cache
- library paths
- isolation
discussion_id: 20260421090020.59726-3-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 2/3] ldconfig: Add an option to ignore standard path during ld.so.cache
  generation'
headline: 'ldconfig: Add an option to ignore standard path during ld.so.cache generation'
tldr: Adds a -I/--ignore-standard-dirs option to ldconfig to generate ld.so.cache
  files that exclude standard library paths.
stakes: Facilitates creation of isolated environments with custom library sets, essential
  for containerization and embedded systems.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Provides greater control over the contents of the `ld.so.cache` file.
- May require more manual configuration to ensure that all necessary libraries are
  included in the cache.
- Can reduce the size of the `ld.so.cache` file and improve performance in isolated
  environments.
exchanges: []
primer_expert: This patch modifies `ldconfig` to add a flag that skips the default
  system library directories during cache generation. This allows creating `ld.so.cache`
  files containing only libraries from specified directories, useful for custom environments.  This
  is important for environments where isolation/sandboxing is needed and the system
  libraries are not desired.
primer_general: '`ldconfig` is a utility that creates the `ld.so.cache` file, which
  is used by the dynamic linker (`ld.so`) to quickly locate shared libraries. By default,
  `ldconfig` includes libraries from standard system directories like `/lib` and `/usr/lib`.  This
  patch adds an option to `ldconfig` to skip these standard directories.  This is
  useful when you want to create a custom environment with only a specific set of
  libraries, such as in a container or an embedded system where you don''t want to
  include all the system''s default libraries.'
series_id: '20260421090020.59726'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-3-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces the `-I` or `--ignore-standard-dirs` option to `ldconfig`.  When used, `ldconfig` will generate an `ld.so.cache` file that only includes libraries from directories specified in the configuration file, excluding standard paths like `/lib` and `/usr/lib`. This is useful for creating isolated environments where only specific libraries are available.
