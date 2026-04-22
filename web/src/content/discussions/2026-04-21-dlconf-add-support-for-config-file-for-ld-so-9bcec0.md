---
project: glibc
subsystem: dlconf
patch_id: null
tags:
- dynamic linker
- ld.so
- shared libraries
- containerization
discussion_id: 20260421090020.59726-2-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 1/3] dlconf: Add support for config file for ld.so'
headline: 'Dlconf: Add support for config file for ld.so'
tldr: Introduce a configuration file for ld.so to specify which ld.so.cache file to
  use for libraries/binaries from specific paths.
stakes: This change allows for better isolation of shared libraries, potentially improving
  security and managing dependencies in complex environments.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in configuration management.
- Potential performance overhead due to additional configuration file parsing.
- Possible conflicts between different configuration files.
- Requires careful handling of configuration precedence.
- May introduce new security considerations related to configuration file access.
exchanges: []
primer_expert: This patch introduces a new configuration file for ``ld.so``, similar
  to an INI format, which affects the dynamic linking process. It allows specifying
  different caches and isolation settings for libraries based on their paths, potentially
  impacting symbol resolution and dependency loading. The configuration is stored
  in ``/etc/ldconfig.conf`` and ``/etc/ldconfig.conf.d/*``.
primer_general: The dynamic linker (``ld.so``) is responsible for loading shared libraries
  when a program is executed. It uses a cache file (``ld.so.cache``) to quickly locate
  these libraries. This proposal introduces a configuration file that allows specifying
  which ``ld.so.cache`` file to use for libraries/binaries from specific paths. This
  can be useful for isolating different execution environments or for using custom
  library versions. The configuration is stored in ``/etc/ldconfig.conf`` and ``/etc/ldconfig.conf.d/*``.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-2-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces a configuration file (``/etc/ldconfig.conf`` and ``/etc/ldconfig.conf.d/*``) for the dynamic linker (``ld.so``). The configuration file allows specifying which ``ld.so.cache`` file to use when looking for dependencies for a library or binary from a specific path. This configuration uses an INI-like format to define paths, caches, isolation settings, and ``dlopen`` paths.
