---
project: glibc
subsystem: ldconfig
patch_id: null
tags:
- glibc
- ldconfig
- ld.so.cache
- library paths
- dynamic linker
discussion_id: 20260421090020.59726-3-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 2/3] ldconfig: Add an option to ignore standard path during ld.so.cache
  generation'
headline: 'RFC: ldconfig gains option to ignore standard paths when generating ld.so.cache.'
tldr: The ldconfig utility will have a new option to ignore standard library paths
  when generating the ld.so.cache file.
stakes: Allows creation of isolated ld.so.cache files, useful in containers or specialized
  environments.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Allows for smaller, more isolated caches but may require more manual configuration.
- May increase the risk of missing dependencies if not configured correctly.
exchanges:
- author: Łukasz Stelmach <l.stelmach@samsung.com>
  role: proposer
  position: Proposes adding an option to ldconfig to ignore standard library paths
    during cache generation.
  quote: Add -I/--ignore-standard-dirs option to ignore standard library paths.
primer_expert: This patch modifies `elf/ldconfig.c` to add a new command-line option.  The
  `-I` option allows generating an `ld.so.cache` file that excludes the standard system
  library paths. This is relevant for creating isolated environments where only a
  specific set of libraries should be visible, and avoids pulling in system-wide dependencies.
  This complements the `dlconf` series by allowing custom caches to be created.
primer_general: '`ldconfig` is a utility used to manage the dynamic linker''s cache
  file (`ld.so.cache`).  The dynamic linker uses this cache to quickly locate shared
  libraries at runtime. By default, `ldconfig` includes all shared libraries found
  in standard system directories (like `/lib` and `/usr/lib`) in the cache.  This
  patch introduces a new option that allows excluding these standard directories,
  which can be useful for creating minimal or isolated cache files, for instance inside
  containers.'
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-3-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This RFC proposes adding a new option, `-I/--ignore-standard-dirs`, to the `ldconfig` utility. This option allows users to generate an `ld.so.cache` file that only includes libraries from the directories specified in the configuration file, excluding libraries from standard paths like `/lib` and `/usr/lib`.
