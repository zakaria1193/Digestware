---
project: glibc
subsystem: malloc
patch_id: null
tags:
- malloc
- ifunc
- performance
- ABI
discussion_id: xntst9492g.fsf@greed.delorie.com
source_type: public_inbox
title: 'Re: [PATCH 2/2] malloc: introduce ifuncs for malloc functions'
headline: 'malloc: Introduce ifuncs for malloc functions'
tldr: A patch introduces ifuncs for malloc functions, renaming core implementations
  with a `_core` suffix. Discussion questions the suffix choice.
stakes: May impact performance and ABI by introducing ifuncs for malloc functions,
  potentially allowing for target-specific optimizations.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The discussion raises a valid API naming question, indicating
  a neutral but engaged review process.
technical_tradeoffs:
- Introduces ifuncs for potential performance benefits via target-specific implementations.
- Renaming core functions requires careful consideration of naming conventions.
- Targets without ifunc support will alias external functions to their respective
  *_core symbols.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/xntst9492g.fsf@greed.delorie.com
bugzilla_url: null
date: '2026-04-17'
---

This patch introduces ifuncs and resolvers for malloc-related functions. Core implementations are renamed with the `_core` suffix, and a generic resolver is provided. The patch includes an AArch64-specific resolver as an example.  A question is raised about the choice of the `_core` suffix vs. the `_generic` suffix.
