---
project: glibc
subsystem: dlconf
patch_id: null
tags:
- glibc
- dynamic linker
- ld.so
- configuration
- containerization
discussion_id: 20260421090020.59726-2-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 1/3] dlconf: Add support for config file for ld.so'
headline: 'dlconf: Add support for config file for ld.so'
tldr: Introduce a configuration file for ld.so that allows specifying which ld.so.cache
  file to use for dependencies of libraries or binaries from specific paths.
stakes: Enables containerization with minimal overhead by allowing separation of execution
  environments and custom dependency resolution.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the dynamic linking process by introducing configuration files
  and parsing logic.
- Provides increased flexibility and control over library dependencies, enabling isolation
  and custom environments.
- May introduce performance overhead due to the need to parse configuration files
  and manage multiple caches.
exchanges: []
primer_expert: This patch introduces configuration files for `ld.so`, the dynamic
  linker. These config files allow specifying alternative `ld.so.cache` files for
  different paths, enabling a form of library isolation.  The configuration is INI-like
  and supports sections for defining paths, caches, isolation levels, and `dlopen`
  restrictions. This mechanism complements existing methods for controlling dynamic
  linking such as `LD_LIBRARY_PATH` and `RUNPATH`.
primer_general: When a program starts, it often relies on shared libraries for common
  functions. The dynamic linker (`ld.so`) is responsible for finding and loading these
  libraries. To speed up this process, the system maintains a cache (`ld.so.cache`)
  of library locations.  This patch introduces a way to configure the dynamic linker
  using configuration files. These files let you specify which cache to use for libraries
  in particular directories, and also control how libraries can depend on each other.
  This is useful for creating isolated environments where different programs can use
  different versions of the same libraries without interfering with each other, similar
  to containerization.
series_id: '20260421090020.59726'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-2-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces a configuration file, `/etc/ldconfig.conf` and `/etc/ldconfig.conf.d/*`, to specify which `ld.so.cache` file should be used when resolving dependencies for libraries or binaries located in specific paths. The configuration uses an INI-like format to define paths, cache files, isolation settings, and `dlopen` restrictions.  This configuration is ignored if `LD_LIBRARY_PATH` or `RUNPATH` are set.
