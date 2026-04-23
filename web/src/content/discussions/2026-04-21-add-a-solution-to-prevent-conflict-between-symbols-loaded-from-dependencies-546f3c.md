---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- dynamic linker
- symbol resolution
- symbol conflict
- dlconf
discussion_id: 20260421090020.59726-4-l.stelmach@samsung.com
source_type: public_inbox
title: '[RFC 3/3] Add a solution to prevent conflict between symbols loaded from dependencies'
headline: Add a solution to prevent conflict between symbols loaded from dependencies
tldr: Implements symbol isolation based on dlconf sections, preventing conflicts between
  dependencies loaded from different environments.
stakes: Enables the use of different versions of the same library by different components
  of a system, avoiding conflicts and ensuring compatibility.
proposer: Łukasz Stelmach <l.stelmach@samsung.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increases the complexity of the symbol resolution process, potentially adding performance
  overhead.
- Provides a powerful mechanism for isolating library dependencies and preventing
  conflicts.
- Requires careful configuration to ensure that dependencies are correctly isolated.
exchanges: []
primer_expert: This patch modifies the dynamic linker to implement symbol isolation
  based on `dlconf` sections. Each `link_map` is tagged with a section number derived
  from the `dlconf` configuration. Symbol resolution is then constrained by these
  section numbers and the DT_NEEDED list, allowing libraries to use private versions
  of dependencies. This is a form of fine-grained symbol versioning, controlled by
  configuration rather than symbol attributes.
primer_general: When a program uses multiple libraries, those libraries might depend
  on other libraries, and sometimes those dependencies can conflict. For example,
  two libraries might both need different versions of the same underlying library.
  This patch introduces a way to isolate the symbols (functions, variables) provided
  by different libraries, preventing these conflicts.  The `dlconf` configuration
  is used to define different "sections" or environments, and the dynamic linker ensures
  that libraries within a section only use symbols from other libraries in the same
  section or from their direct dependencies. This allows different parts of a system
  to use different versions of the same library without causing problems.
series_id: '20260421090020.59726'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421090020.59726-4-l.stelmach@samsung.com
bugzilla_url: null
date: '2026-04-21'
---

This patch adds a mechanism to prevent symbol conflicts between libraries loaded from different environments, configured via `dlconf`. Each section in the `dlconf` configuration is assigned a unique number, and each loaded object (`link_map`) inherits the section number. During symbol resolution, the linker checks whether an object is allowed to use a symbol from another object based on these section numbers and the `DT_NEEDED` list, allowing a library to use its own version of a dependency while still using a different version for another dependency.
