---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- containerization
- ld.so
- dynamic linker
- embedded systems
discussion_id: 20260421090020.59726-1-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 0/3] Use multiple ld.so caches to separate execution environments'
headline: Use multiple ld.so caches to separate execution environments
tldr: This RFC series proposes using multiple ld.so caches and config files to isolate
  execution environments, primarily for embedded devices.
stakes: This series enables better containerization and isolation of applications
  and libraries, particularly in embedded systems with vendor-provided components.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in managing multiple ld.so caches and configurations.
- Potential performance overhead due to more complex library lookup procedures.
- Improved isolation and reduced dependency conflicts.
exchanges: []
primer_expert: This patch series introduces a mechanism to isolate execution environments
  within glibc by using multiple `ld.so` caches and configuration files. This involves
  modifications to `elf/dl-*.c` files, the introduction of `elf/dlconf*.c` files,
  and changes to `ldconfig`. The primary goal is to support containerization and separation
  of vendor-provided libraries in embedded systems.
primer_general: This series of patches aims to improve how Linux systems manage shared
  libraries, which are collections of code that multiple programs can use.  The core
  idea is to allow different parts of the system to use different sets of libraries,
  preventing conflicts and improving security.  This is achieved by allowing multiple
  `ld.so` caches (which tell the system where to find libraries) and using configuration
  files to specify which libraries should be used in different environments. This
  is particularly useful in embedded systems, where different vendors might provide
  different versions of the same libraries.
series_id: 20260421090020.59726-1-l.stelmach@samsung.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-1-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

Łukasz Stelmach introduces a series of patches designed to improve containerization with minimal overhead, targeting embedded devices where components are delivered by hardware vendors. The patches introduce configuration files for `ld.so`, an option to ignore standard paths during `ld.so.cache` generation, and a mechanism to prevent symbol conflicts between dependencies. This approach aims to keep vendor-provided components separate from the rest of the platform, similar to `chroot` but without restricting access to data outside the designated directory.
