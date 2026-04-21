---
project: glibc
subsystem: ldconfig
patch_id: null
tags:
- glibc
- ldconfig
- ld.so.cache
- dynamic linker
- isolation
discussion_id: 20260421090020.59726-3-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 2/3] ldconfig: Add an option to ignore standard path during ld.so.cache
  generation'
headline: ldconfig gains option to ignore standard library paths
tldr: This patch adds a -I/--ignore-standard-dirs option to ldconfig, allowing generation
  of ld.so.cache files without including standard library paths.
stakes: Excluding standard library paths provides greater control over the contents
  of the ld.so.cache, useful for creating isolated or custom environments.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reduced flexibility in the cache, as standard libraries are not included by default.
- Requires careful configuration to ensure all necessary libraries are included in
  the custom cache.
- Improved isolation and control over the library environment.
exchanges: []
primer_expert: This patch modifies `ldconfig` to add the `-I` option, which prevents
  the inclusion of standard library paths during `ld.so.cache` generation. This facilitates
  the creation of custom caches for specific environments. This interacts with `elf/ldconfig.c`
  and the overall dynamic linking setup in glibc.
primer_general: '`ldconfig` is a utility that creates the `ld.so.cache` file, which
  the dynamic linker uses to quickly locate shared libraries. By default, `ldconfig`
  includes libraries from standard system directories like `/lib` and `/usr/lib`.
  This patch adds an option to exclude these standard directories, allowing the creation
  of a cache that only contains libraries from explicitly specified directories. This
  is useful when creating isolated environments or containers, where you only want
  the program to see a specific set of libraries.'
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-3-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

Łukasz Stelmach proposes adding a `-I/--ignore-standard-dirs` option to `ldconfig`.  This allows generating an `ld.so.cache` file containing only libraries from specified configuration files, excluding libraries from standard paths such as `/lib` and `/usr/lib`. This is useful for creating isolated environments where only specific libraries are available.
