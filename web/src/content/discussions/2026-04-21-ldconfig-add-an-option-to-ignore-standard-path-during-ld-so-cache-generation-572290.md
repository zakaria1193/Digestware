---
project: glibc
subsystem: ldconfig
patch_id: null
tags:
- ldconfig
- ld.so.cache
- dynamic linker
- shared libraries
- contenerization
discussion_id: 20260421090020.59726-3-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 2/3] ldconfig: Add an option to ignore standard path during ld.so.cache
  generation'
headline: 'Ldconfig: Add an option to ignore standard path during ld.so.cache generation'
tldr: Add an option to ldconfig to generate an ld.so.cache file that excludes standard
  library paths.
stakes: This allows for creating isolated environments with custom library paths,
  useful for contenerization and testing specific library versions.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in ldconfig usage.
- Potential for misconfiguration if the option is used incorrectly.
- Requires careful consideration of library dependencies when excluding standard paths.
- May impact application compatibility if standard libraries are not included in the
  cache.
- Could lead to unexpected behavior if the cache is not properly updated.
exchanges: []
primer_expert: This patch introduces a new option to ``ldconfig`` that modifies the
  generation of the ``ld.so.cache`` file. This affects the dynamic linking process
  by allowing the creation of cache files that exclude standard library paths. The
  relevant file is ``elf/ldconfig.c``.
primer_general: The ``ldconfig`` utility is used to create and update the ``ld.so.cache``
  file, which the dynamic linker uses to locate shared libraries. By default, ``ldconfig``
  includes standard library paths (e.g., ``/lib``, ``/usr/lib``) in the cache. This
  patch adds an option to exclude these standard paths, allowing for the creation
  of a cache file that only contains libraries from specific directories. This is
  useful for creating isolated environments or for testing with custom library versions.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-3-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch adds the ``-I/--ignore-standard-dirs`` option to ``ldconfig``.  When used, ``ldconfig`` will generate an ``ld.so.cache`` file that only includes libraries from the directories specified in the configuration, excluding standard paths like ``/lib`` and ``/usr/lib``.
