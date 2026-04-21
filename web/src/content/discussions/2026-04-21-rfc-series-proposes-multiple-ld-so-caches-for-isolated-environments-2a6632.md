---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- dynamic linker
- containerization
- embedded systems
- library isolation
discussion_id: 20260421090020.59726-1-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 0/3] Use multiple ld.so caches to separate execution environments'
headline: 'RFC: Series proposes multiple ld.so caches for isolated environments.'
tldr: This series introduces changes to glibc to support multiple ld.so caches for
  separating execution environments, mainly for embedded systems.
stakes: Enables better contenerization and isolation of vendor-provided libraries
  in embedded systems, reducing conflicts and improving security.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in the dynamic linker.
- Potential performance overhead due to the need to manage multiple caches.
- Requires careful configuration to ensure proper isolation.
exchanges:
- author: Łukasz Stelmach <l.stelmach@samsung.com>
  role: proposer
  position: Proposes a series of patches to implement multiple ld.so caches for separating
    execution environments.
  quote: The following series of patches is our take on contenerization with as little
    overhead as possible. We developed this code to use in embedded devices where
    parts of the platform are delivered by a hardware vendor.
primer_expert: This series introduces significant changes to the dynamic linker in
  glibc. It involves modifications to `elf/dl-load.c`, `elf/dl-lookup.c`, `elf/ldconfig.c`
  and the introduction of new files like `elf/dlconf.c` and `elf/dlconf.h`. The core
  idea is to support multiple `ld.so.cache` files and isolate the symbol resolution
  process for different execution environments. This is particularly important for
  embedded systems with vendor-provided libraries that need to be isolated from the
  main system.
primer_general: This series of patches aims to improve how shared libraries are managed
  in the GNU C Library (glibc). Shared libraries are collections of code that can
  be used by multiple programs, saving disk space and memory.  The patches introduce
  a way to create isolated environments where different programs can use different
  versions of the same library without interfering with each other. This is achieved
  by using multiple caches of available libraries and controlling how symbols (functions
  and variables) are resolved. This is particularly useful in embedded systems where
  different vendors might provide different versions of the same libraries.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-1-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This RFC series proposes a solution for containerization with minimal overhead, targeted at embedded devices. The changes allow the runtime linker to collect dependencies of binaries from specific directories, effectively creating isolated environments. This is achieved by using multiple `ld.so` caches and preventing conflicts between symbols loaded from different caches.
