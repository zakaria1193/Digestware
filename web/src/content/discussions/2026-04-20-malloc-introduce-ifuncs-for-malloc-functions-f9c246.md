---
project: glibc
subsystem: malloc
patch_id: null
tags:
- glibc
- malloc
- ifunc
- performance
discussion_id: aeXpUaZLnmRN1wbk@arm.com
source_type: public_inbox
title: 'Re: [PATCH 2/2] malloc: introduce ifuncs for malloc functions'
headline: 'malloc: introduce ifuncs for malloc functions'
tldr: Discussion about introducing ifuncs for malloc functions in glibc, including
  naming conventions and compatibility concerns.
stakes: Discusses the implementation of ifuncs in glibc's malloc, which can improve
  performance by allowing the selection of optimized malloc implementations at runtime.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The discussion is mostly technical, with some questions raised
  about naming and compatibility.
technical_tradeoffs:
- Increased code complexity with the introduction of ifuncs.
- Potential overhead from the ifunc resolution process at runtime.
primer: Glibc is the GNU C Library, providing standard functions for C programs. Malloc
  is the memory allocation function in C. Ifuncs (indirect functions) are a mechanism
  in glibc that allows resolving a function call to different implementations at runtime,
  depending on the CPU or other system capabilities. This patch is about using ifuncs
  in the malloc implementation.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXpUaZLnmRN1wbk@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This thread discusses the introduction of ifuncs (indirect functions) for malloc functions in glibc. The discussion covers naming conventions for the core implementations (using `_core` vs `_generic` suffix) and ensuring that the published symbol list remains the same before and after the change. The proposer responds to feedback and plans to send a v2 with fixes.
