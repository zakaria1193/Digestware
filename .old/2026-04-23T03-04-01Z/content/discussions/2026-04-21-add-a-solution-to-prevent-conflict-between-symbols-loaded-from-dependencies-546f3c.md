---
project: glibc
subsystem: glibc
patch_id: null
tags:
- symbol resolution
- dynamic linker
- dependency management
- glibc
discussion_id: 20260421090020.59726-4-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 3/3] Add a solution to prevent conflict between symbols loaded from dependencies'
headline: Add a solution to prevent conflict between symbols loaded from dependencies
tldr: Isolate symbols from different libraries to prevent conflicts by assigning unique
  identifiers based on dlconf configuration sections.
stakes: Symbol conflicts can lead to unpredictable behavior and crashes.  This change
  improves application stability, especially in environments with multiple versions
  of the same library.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in the symbol resolution process.
- Potential performance overhead due to additional checks during symbol lookup.
- Requires careful design to avoid unintended isolation and breakage of legitimate
  dependencies.
- May introduce ABI compatibility issues if not implemented carefully.
- Impacts the dynamic linking process and requires thorough testing.
exchanges: []
primer_expert: This patch modifies the symbol resolution process in the dynamic linker
  by introducing a section-based isolation mechanism. Each ``link_map`` structure
  is assigned a unique identifier based on the ``dlconf`` configuration, and symbol
  resolution is restricted based on these identifiers and the DT_NEEDED list. This
  affects the ``elf/dl-lookup.c`` and related files.
primer_general: When multiple libraries are loaded into a program, they might define
  the same symbols (e.g., function names, global variables). This can lead to symbol
  conflicts, where the program uses the wrong symbol, leading to unexpected behavior
  or crashes. This patch aims to prevent these conflicts by isolating symbols from
  different libraries. It assigns each library a unique identifier and restricts symbol
  resolution to allow only symbols from the same library or direct dependencies to
  be used.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-4-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patchset introduces a mechanism to prevent symbol conflicts between libraries loaded from different paths, achieved by assigning each section in the ``dlconf`` configuration file a unique number. During linking, each object is assigned the number of its corresponding section, and the symbol resolution process checks if an object is allowed to use a symbol from another object based on these section numbers and direct dependencies.
