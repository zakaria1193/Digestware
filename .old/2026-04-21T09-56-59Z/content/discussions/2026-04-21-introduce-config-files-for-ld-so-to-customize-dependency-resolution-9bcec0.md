---
project: glibc
subsystem: dlconf
patch_id: null
tags:
- glibc
- dynamic linker
- ld.so
- dependency resolution
- configuration
discussion_id: 20260421090020.59726-2-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 1/3] dlconf: Add support for config file for ld.so'
headline: Introduce config files for ld.so to customize dependency resolution
tldr: This patch introduces configuration files for ld.so, allowing users to specify
  which ld.so.cache file to use for libraries from specific paths.
stakes: This feature enables better isolation and customization of library dependencies,
  potentially improving security and simplifying deployment in complex environments.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in configuration and maintenance.
- Potential performance overhead due to more complex lookup logic.
- Improved isolation and customization of library dependencies.
exchanges: []
primer_expert: This patch introduces dlconf, enabling configuration files for ld.so.
  This facilitates specifying ld.so.cache files for specific library paths, offering
  finer-grained control over dependency resolution. The configuration files use an
  INI-like format. The patch series touches on `link_map` structures and symbol resolution
  within glibc's dynamic linking process.
primer_general: The dynamic linker (ld.so) is responsible for loading shared libraries
  that a program depends on when the program is executed. This proposal introduces
  configuration files that allow administrators to control how ld.so finds these libraries.  Currently,
  ld.so searches standard locations and uses a cache file (`ld.so.cache`) to speed
  up the process.  These config files would allow specifying different cache files
  and search paths for different libraries, enabling more flexible and isolated environments.
  This can be useful for containerization or for managing libraries provided by different
  vendors.
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-2-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

Łukasz Stelmach proposes adding configuration files for ld.so, the dynamic linker. This allows specifying which ld.so.cache file to use when searching for library dependencies based on the path of the library or binary. The configuration, similar to INI format, is stored in `/etc/ldconfig.conf` and `/etc/ldconfig.conf.d/*`.  Settings like `isolation` and `dlopen_isolation` can restrict dependency resolution and `dlopen` to specific paths.
