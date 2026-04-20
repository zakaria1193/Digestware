---
project: glibc
subsystem: malloc
patch_id: null
tags:
- malloc
- ifunc
- performance
discussion_id: aeXpUaZLnmRN1wbk@arm.com
source_type: public_inbox
title: 'Re: [PATCH 2/2] malloc: introduce ifuncs for malloc functions'
headline: 'Malloc: Introduce ifuncs for malloc functions'
tldr: This patch introduces ifuncs for malloc functions to improve performance by
  allowing the selection of optimized implementations at runtime.
stakes: This change could improve malloc performance, especially on systems with diverse
  hardware or software configurations. Incorrect symbol versioning could break compatibility.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Needs Revision
outcome: needs_revision
sentiment_score: 7
sentiment_rationale: The discussion is mostly positive with constructive feedback.
technical_tradeoffs:
- Introduces ifuncs, which may increase code complexity.
- Renames core malloc implementations, potentially affecting compatibility if not
  handled carefully.
- Requires careful symbol versioning to avoid breaking existing applications.
series_id: 'glibc:malloc: introduce ifuncs for malloc functions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXpUaZLnmRN1wbk@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces ifuncs and resolvers for malloc-related functions, renaming the core implementations with a '_core' suffix.  The goal is to enable runtime selection of optimized malloc implementations.  A developer has suggested using the '_generic' suffix instead, and the author is open to changing the suffix and will address other feedback in v2.
