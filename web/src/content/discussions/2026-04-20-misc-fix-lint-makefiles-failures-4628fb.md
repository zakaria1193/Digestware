---
project: glibc
subsystem: misc
patch_id: null
tags:
- glibc
- Makefile
- lint
- build system
discussion_id: aeXhrdc8BxCy0vsH@arm.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] misc: fix lint-makefiles failures'
headline: 'misc: fix lint-makefiles failures'
tldr: Discussion about Makefile changes to fix lint-makefiles failures in glibc, including
  concerns about using '+=' vs '='.
stakes: Ensures that the glibc Makefiles pass the lint-makefiles checks, maintaining
  build system integrity and consistency.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: The discussion is focused on Makefile syntax and style, with
  a proactive approach to ensuring consistency.
technical_tradeoffs: []
primer: Glibc is the GNU C Library. Makefiles are used to automate the build process.
  lint-makefiles is a tool that checks Makefiles for common errors and stylistic issues.
  This patch is about changes to the Makefiles.
series_id: 'glibc:misc: fix lint-makefiles failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXhrdc8BxCy0vsH@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This thread discusses changes to the glibc Makefiles to address lint-makefiles failures. The discussion focuses on whether to use `+=` or `=` when defining the `sysdep_malloc_debug_routines` macro, and on splitting lines for readability. The proposer plans to double-check the `+=` change.
