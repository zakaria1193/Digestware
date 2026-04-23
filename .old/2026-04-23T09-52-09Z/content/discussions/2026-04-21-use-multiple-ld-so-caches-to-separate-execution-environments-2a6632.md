---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- containerization
- ld.so
- dynamic linking
- embedded systems
discussion_id: 20260421090020.59726-1-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 0/3] Use multiple ld.so caches to separate execution environments'
headline: Use multiple ld.so caches to separate execution environments
tldr: Introduce multiple ld.so caches and configuration options to isolate execution
  environments, aimed at embedded devices.
stakes: Enables isolation of vendor-provided components in embedded systems with minimal
  overhead, preventing conflicts and ensuring compatibility.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases complexity of the dynamic linking process.
- Provides better isolation and control over library dependencies.
- May introduce performance overhead.
exchanges: []
primer_expert: This series introduces a `dlconf` mechanism to glibc, allowing for
  multiple `ld.so` caches and isolated library environments. Patches modify `ldconfig`,
  `ld.so`, and related files to support configuration-driven linking. The primary
  goal is to isolate vendor libraries in embedded systems, avoiding conflicts with
  system libraries.  This is achieved through custom caches and symbol resolution
  rules.
primer_general: When a program runs, it depends on shared libraries for many functions.  The
  standard way to manage these libraries is through a global cache.  This patch series
  proposes a way to have multiple, separate caches for libraries.  This would allow
  different parts of a system to use different versions of the same library without
  interfering with each other. This is particularly useful in embedded systems where
  some components might be provided by a vendor and need to be isolated from the rest
  of the system to avoid conflicts.
series_id: '20260421090020.59726'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-1-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch series aims to provide containerization with minimal overhead, primarily targeting embedded devices. It introduces configuration options and multiple `ld.so` caches to isolate execution environments. The goal is to separate vendor-provided parts of the platform from the rest of the system, allowing dependencies to be resolved within a specific directory without restricting access to data outside that directory.
