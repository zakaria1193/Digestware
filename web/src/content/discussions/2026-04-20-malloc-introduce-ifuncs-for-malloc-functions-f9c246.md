---
project: glibc
subsystem: malloc
patch_id: null
tags:
- malloc
- ifunc
- glibc
- performance
- ABI
discussion_id: aeXpUaZLnmRN1wbk@arm.com
source_type: public_inbox
title: 'Re: [PATCH 2/2] malloc: introduce ifuncs for malloc functions'
headline: 'malloc: introduce ifuncs for malloc functions'
tldr: Prepare malloc functions for ifunc-based dynamic resolution, renaming the core
  implementations with a `_core` suffix.
stakes: This change could impact performance and ABI stability of malloc, a core component
  of glibc.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Renaming core functions may break backwards compatibility if external code relies
  on the old names.
- Introducing ifuncs can improve performance by allowing for runtime optimization.
- Increased complexity in the code base.
primer: Malloc is the memory allocator in the C standard library. ifuncs provide a
  mechanism for resolving function calls at runtime, allowing for optimized versions
  of functions to be selected based on CPU features or other factors. This can improve
  performance but may also introduce ABI compatibility issues if not handled carefully.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXpUaZLnmRN1wbk@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces ifuncs (indirect functions) for malloc functions in glibc. To achieve this, the core implementations are renamed by adding the `_core` suffix. The author is planning to send a v2 with fixes based on the feedback received.
