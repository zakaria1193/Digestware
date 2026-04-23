---
project: glibc
subsystem: glibc
patch_id: null
tags:
- dynamic linker
- ld.so
- shared libraries
- contenerization
- embedded
discussion_id: 20260421090020.59726-1-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 0/3] Use multiple ld.so caches to separate execution environments'
headline: Use multiple ld.so caches to separate execution environments
tldr: This series introduces changes to use multiple ld.so caches for isolating execution
  environments, primarily targeting embedded devices.
stakes: This series enables better isolation of shared libraries, improving security
  and dependency management in complex, especially embedded, systems.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in managing multiple ld.so caches.
- Potential performance overhead due to additional configuration and lookup operations.
- Requires careful handling of configuration precedence and isolation levels.
- May introduce ABI compatibility issues if not implemented carefully.
- Impacts the dynamic linking process and requires thorough testing.
exchanges: []
primer_expert: This series of patches modifies the dynamic linker to support multiple
  ``ld.so`` caches and configuration files. This affects the dynamic linking process
  by allowing different execution environments to use different sets of shared libraries
  and configurations. The core changes are in ``elf/dl-*.c``, ``elf/ldconfig.c``,
  and the introduction of ``elf/dlconf.c``.
primer_general: The dynamic linker (``ld.so``) is responsible for loading shared libraries
  when a program is executed. It uses a cache file (``ld.so.cache``) to quickly locate
  these libraries. This patch series introduces changes to allow the use of multiple
  ``ld.so`` caches. This is useful for isolating different execution environments,
  ensuring that each environment uses its own set of libraries and configurations,
  preventing conflicts and improving security. It particularly targets embedded systems.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-1-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch series provides a way to isolate execution environments using multiple ``ld.so`` caches.  The primary use case is embedded devices where parts of the platform are delivered by a hardware vendor and need to be kept separate from the rest of the system. The series includes patches for configuring ``ld.so`` via a config file, ignoring standard paths during cache generation, and preventing symbol conflicts.
