---
project: glibc
subsystem: dlconf
patch_id: null
tags:
- glibc
- dynamic linker
- ld.so
- configuration
- library isolation
discussion_id: 20260421090020.59726-2-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 1/3] dlconf: Add support for config file for ld.so'
headline: 'RFC: Glibc''s dynamic linker will gain configuration file support.'
tldr: The dynamic linker will support config files to specify ld.so.cache files for
  specific paths, enabling better library isolation.
stakes: Allows library isolation and vendor-provided library separation, useful for
  embedded systems.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the dynamic linker but enables library isolation.
- Requires parsing configuration files, which may introduce overhead.
- May impact performance if not implemented efficiently.
exchanges:
- author: Łukasz Stelmach <l.stelmach@samsung.com>
  role: proposer
  position: Proposes adding support for configuration files that allow specifying
    cache files and isolation levels for libraries.
  quote: Configuration allows to specify which ld.so.cache file to use when looking
    for dependencies for a library or binary from a specific path (note that setting
    LD_LIBRARY_PATH or RUNPATH will result in the following configuration not being
    used).
primer_expert: This patch introduces configuration file support for `ld.so`, the dynamic
  linker. The config files allow specifying alternate `ld.so.cache` files and isolation
  settings per path. This is relevant to `elf/dl-load.c`, `elf/dl-lookup.c`, and other
  files involved in dynamic linking. This feature allows for better library isolation,
  especially in environments where different parts of the system may require different
  versions of the same library.
primer_general: When a program starts on a Linux system, the dynamic linker (`ld.so`)
  is responsible for loading the libraries that the program depends on.  This patch
  series introduces a way to configure the dynamic linker using configuration files.
  This allows administrators to specify different search paths and caches for libraries,
  which can be useful for creating isolated environments or managing dependencies
  in complex systems.  The configuration files allow specifying which `ld.so.cache`
  file to use for libraries in specific directories, and also control how libraries
  are loaded using `dlopen`.
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-2-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This RFC proposes adding support for configuration files to the dynamic linker (`ld.so`).  The configuration files  `/etc/ldconfig.conf` and files under `/etc/ldconfig.conf.d/*` allow specifying which `ld.so.cache` file to use when resolving dependencies for libraries or binaries located in specific paths.  The configuration supports specifying isolation levels, restricting `dlopen` paths, and extending existing sections.
