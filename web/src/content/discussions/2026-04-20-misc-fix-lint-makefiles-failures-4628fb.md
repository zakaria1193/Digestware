---
project: glibc
subsystem: misc
patch_id: null
tags:
- makefile
- lint
- build
- glibc
discussion_id: aeXhrdc8BxCy0vsH@arm.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] misc: fix lint-makefiles failures'
headline: 'misc: fix lint-makefiles failures'
tldr: This patch fixes failures reported by lint-makefiles, with a possible reversion
  of a change from '=' to '+='.
stakes: This relates to build system hygiene and maintainability. Developers benefit
  from a clean and consistent build process.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Changing '=' to '+=' can affect how variables are defined and potentially introduce
  unintended side effects in other parts of the build system.
- Splitting long lines in Makefiles improves readability but can also increase the
  size of the file.
primer: '`lint-makefiles` is a tool used to check the consistency and correctness
  of Makefiles. Makefiles are used to automate the build process. In glibc, they define
  how the library is compiled and linked.  Incorrect Makefiles can lead to build failures
  or inconsistencies.'
series_id: 'glibc:misc: fix lint-makefiles failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeXhrdc8BxCy0vsH@arm.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses failures identified by the `lint-makefiles` tool.  The author is considering reverting a change where `=` was replaced with `+=` in the Makefile, after a reviewer pointed out the potential impact on macro definitions in other Makefiles. Other changes, like splitting lines for readability, are also being discussed.
